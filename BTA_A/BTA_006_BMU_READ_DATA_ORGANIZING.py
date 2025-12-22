import sys
import os

sys.path.append(os.path.abspath("DUT/BMU"))

from DUT_BMU_READ_DATA_INPUT import DUT_BMU_READ_DATA_INPUT


###### helper functions ##################
def USINT_TO_UINT(lsb, msb):
    return (msb << 8) | lsb

def USINT_TO_SINT(val):
    return val - 256 if val > 127 else val

def GET_BIT(byte, bit):
    return (byte >> bit) & 0x01
###########################################


####### Safe frame/byte accessor ###########
def DF(bmu, frame, byte):
    """
    frame: 1..48
    byte : 1..8
    Missing frame -> return 0 (PLC-safe behavior)
    """
    f = bmu.can_frames[frame - 1]
    if f is None:
        return 0
    return f[byte - 1]
############################################


def BMU_READ_DATA_ORGANIZING(bmu_raw):
    BMU_INPUT_DATA = DUT_BMU_READ_DATA_INPUT()

    # ---------------- Frame 1 ----------------
    BMU_INPUT_DATA.syn_counter = DF(bmu_raw, 1, 1)
    BMU_INPUT_DATA.Status = DF(bmu_raw, 1, 2)
    BMU_INPUT_DATA.Final_Charge_or_Discharge_info = DF(bmu_raw, 1, 3)
    BMU_INPUT_DATA.Overcharge_or_Overdischarge_or_Overtemperature = DF(bmu_raw, 1, 4)

    BMU_INPUT_DATA.Unit_SOC = USINT_TO_UINT(DF(bmu_raw, 1, 5), DF(bmu_raw, 1, 6))
    BMU_INPUT_DATA.Unit_SOH = USINT_TO_UINT(DF(bmu_raw, 1, 7), DF(bmu_raw, 1, 8))

    # ---------------- Frame 2 ----------------
    BMU_INPUT_DATA.Max_Cell_Voltage = USINT_TO_UINT(DF(bmu_raw, 2, 2), DF(bmu_raw, 2, 3))
    BMU_INPUT_DATA.Min_Cell_Voltage = USINT_TO_UINT(DF(bmu_raw, 2, 4), DF(bmu_raw, 2, 5))

    BMU_INPUT_DATA.Max_Cell_Temperature = DF(bmu_raw, 2, 6)
    BMU_INPUT_DATA.Avg_Cell_Temperature = DF(bmu_raw, 2, 7)
    BMU_INPUT_DATA.Min_Cell_Temperature = DF(bmu_raw, 2, 8)
    # ---------------- Frame 3 ----------------
    BMU_INPUT_DATA.Max_Cell_Voltage_Module_No = DF(bmu_raw, 3, 2)
    BMU_INPUT_DATA.Min_Cell_Voltage_Module_No = DF(bmu_raw, 3, 3)
    BMU_INPUT_DATA.Max_Cell_Temperature_Module_No = DF(bmu_raw, 3, 4)
    BMU_INPUT_DATA.Min_Cell_Temperature_Module_No = DF(bmu_raw, 3, 5)

    # ---------------- Frame 4 ----------------
    BMU_INPUT_DATA.Unit_Charge_Current = USINT_TO_UINT(DF(bmu_raw, 4, 2), DF(bmu_raw, 4, 3))
    BMU_INPUT_DATA.Unit_Discharge_Current = USINT_TO_UINT(DF(bmu_raw, 4, 4), DF(bmu_raw, 4, 5))
    BMU_INPUT_DATA.Unit_Voltage = USINT_TO_UINT(DF(bmu_raw, 4, 6), DF(bmu_raw, 4, 7))
    BMU_INPUT_DATA.BMU_Status_Supplemental_Information = DF(bmu_raw, 4, 8)

    # ---------------- Frame 5 ----------------
    BMU_INPUT_DATA.Max_Cell_Temperature_2 = USINT_TO_UINT(DF(bmu_raw, 5, 2), DF(bmu_raw, 5, 3))
    BMU_INPUT_DATA.Average_Cell_Temperature_2 = USINT_TO_UINT(DF(bmu_raw, 5, 4), DF(bmu_raw, 5, 5))
    BMU_INPUT_DATA.Min_Cell_Temperature_2 = USINT_TO_UINT(DF(bmu_raw, 5, 6), DF(bmu_raw, 5, 7))
    BMU_INPUT_DATA.BMU_Abnormality_Detail = DF(bmu_raw, 5, 8)

    # ---------------- Frame 6 ----------------
    BMU_INPUT_DATA.Unit_SOC_Percentage = DF(bmu_raw, 6, 8)

    # ---------------- Frame 7 (CMU failure bits) ----------------
    BMU_INPUT_DATA.CMU_Failure_Status_Module_1to22 = (
        DF(bmu_raw, 7, 2)
        | (DF(bmu_raw, 7, 3) << 8)
        | (DF(bmu_raw, 7, 4) << 16)
    )

    BMU_INPUT_DATA.CMU_Failure_Status_Module_23to28 = DF(bmu_raw, 7, 5)
    # ---------------- Module Cell Failure / Balance Status ----------------
    def read_module(frame, b1, b2):
        return USINT_TO_UINT(DF(bmu_raw, frame, b1), DF(bmu_raw, frame, b2))

    idx = 27
    # Module 28 → fixed position
    BMU_INPUT_DATA.Module_Cell_Failure_or_Balance_Status[27] = read_module(7, 6, 7)

    # ---------------- Frame 8 ----------------
    idx = 0  # start from module index 0
    for f in range(8, 17):
        for pair in [(2, 3), (4, 5), (6, 7)]:

            # Skip reserved index for Module 28
            if idx == 27:
                idx += 1

            # Stop if array is full
            if idx >= len(BMU_INPUT_DATA.Module_Cell_Failure_or_Balance_Status):
                break

            BMU_INPUT_DATA.Module_Cell_Failure_or_Balance_Status[idx] = read_module(f, *pair)
            idx += 1

    BMU_INPUT_DATA.Parallel_No_Of_Branch = DF(bmu_raw, 8, 8)

    # ---------------- Cell Voltages (12) ----------------
    BMU_INPUT_DATA.Data_Aquisition_Location = DF(bmu_raw, 17, 8)

    # Cell index mapping
    cell_index = 0

    for frame in range(17, 21):          # Frames 17,18,19,20
        for byte_pair in [(2, 3), (4, 5), (6, 7)]:
            if cell_index >= 12:
                break

            BMU_INPUT_DATA.Cell_Voltage[cell_index] = read_module(
                frame, byte_pair[0], byte_pair[1]
            )

            cell_index += 1


    # ---------------- Cell Temperatures (6) ----------------
    for i in range(6):
        BMU_INPUT_DATA.Cell_Temperature[i] = USINT_TO_SINT(DF(bmu_raw, 21, 2 + i))

    # ---------------- Cell Temperatures (13) ----------------
    temps = [
        (22,2),(22,3),(22,4),(22,5),(22,6),(22,7),(22,8),
        (23,2),(23,3),(23,4),(23,5),(23,6),(23,7)
    ]
    for i, (f, b) in enumerate(temps):
        BMU_INPUT_DATA.Cell_Temperature_1[i] = USINT_TO_SINT(DF(bmu_raw, f, b))

    # ---------------- Frame 44 ----------------
    BMU_INPUT_DATA.BMU_Abnormality_Detail_2_BYTE_2 = DF(bmu_raw, 44, 2)
    BMU_INPUT_DATA.BMU_Abnormality_Detail_2_BYTE_3 = DF(bmu_raw, 44, 3)
    BMU_INPUT_DATA.BMU_Abnormality_Detail_2_BYTE_4 = DF(bmu_raw, 44, 4)
    BMU_INPUT_DATA.BMU_Abnormality_Detail_2_BYTE_5 = DF(bmu_raw, 44, 5)

    # ---------------- Frame 45 ----------------
    BMU_INPUT_DATA.CMU_ID = DF(bmu_raw, 45, 2)

    BMU_INPUT_DATA.CMU_Serial_No = (
        DF(bmu_raw, 45, 3)
        | (DF(bmu_raw, 45, 4) << 8)
        | (DF(bmu_raw, 45, 5) << 16)
        | (DF(bmu_raw, 45, 6) << 24)
    )

    BMU_INPUT_DATA.CMU_Lot_No = (
        DF(bmu_raw, 45, 6)
        | (DF(bmu_raw, 45, 7) << 8)
        | (DF(bmu_raw, 45, 8) << 16)
    )

    return BMU_INPUT_DATA
