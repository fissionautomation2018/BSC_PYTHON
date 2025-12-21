from dataclasses import dataclass, field
from typing import List

# This must match your PLC constant
MAX_MODULES_PER_BMU = 56  # adjust if different in your PLC project

@dataclass
class DUT_BMU_READ_DATA_INPUT:
    # Counters / status
    syn_counter: int = 0                           # USINT
    Status: int = 0                                # USINT
    Final_Charge_or_Discharge_info: int = 0        # USINT
    Overcharge_or_Overdischarge_or_Overtemperature: int = 0  # USINT

    # SOC / SOH
    Unit_SOC: int = 0                              # UINT
    Unit_SOH: int = 0                              # UINT

    # Cell voltages
    Max_Cell_Voltage: int = 0                      # UINT
    Min_Cell_Voltage: int = 0                      # UINT

    # Cell temperatures (byte-based)
    Max_Cell_Temperature: int = 0                  # USINT
    Avg_Cell_Temperature: int = 0                  # USINT
    Min_Cell_Temperature: int = 0                  # USINT

    # Module numbers
    Max_Cell_Voltage_Module_No: int = 0            # USINT
    Min_Cell_Voltage_Module_No: int = 0            # USINT
    Max_Cell_Temperature_Module_No: int = 0        # USINT
    Min_Cell_Temperature_Module_No: int = 0        # USINT

    # Currents and voltage
    Unit_Charge_Current: int = 0                   # UINT
    Unit_Discharge_Current: int = 0                # UINT
    Unit_Voltage: int = 0                          # UINT

    # BMU supplemental status
    BMU_Status_Supplemental_Information: int = 0   # USINT

    # Signed temperatures (INT)
    Max_Cell_Temperature_2: int = 0                # INT
    Average_Cell_Temperature_2: int = 0            # INT
    Min_Cell_Temperature_2: int = 0                # INT

    # Abnormality details
    BMU_Abnormality_Detail: int = 0                # USINT
    Unit_SOC_Percentage: int = 0                   # USINT

    # CMU failure bitfields
    CMU_Failure_Status_Module_1to22: int = 0       # UDINT
    CMU_Failure_Status_Module_23to28: int = 0      # BYTE
    CMU_Failure_Status_Module_29to50: int = 0      # UDINT
    CMU_Failure_Status_Module_51to56: int = 0      # BYTE

    # Module cell failure / balancing status
    Module_Cell_Failure_or_Balance_Status: List[int] = field(
        default_factory=lambda: [0] * MAX_MODULES_PER_BMU
    )                                              # ARRAY[1..MAX] OF UINT

    # Additional abnormality bytes
    BMU_Abnormality_Detail_2_BYTE_2: int = 0       # USINT
    BMU_Abnormality_Detail_2_BYTE_3: int = 0       # USINT
    BMU_Abnormality_Detail_2_BYTE_4: int = 0       # USINT
    BMU_Abnormality_Detail_2_BYTE_5: int = 0       # USINT

    # Configuration
    Parallel_No_Of_Branch: int = 0                 # USINT
    Data_Aquisition_Location: int = 0              # USINT

    # Cell level data
    Cell_Voltage: List[int] = field(
        default_factory=lambda: [0] * 12
    )                                              # ARRAY[1..12] OF UINT

    Cell_Temperature: List[int] = field(
        default_factory=lambda: [0] * 6
    )                                              # ARRAY[1..6] OF SINT

    Cell_Temperature_1: List[int] = field(
        default_factory=lambda: [0] * 13
    )                                              # ARRAY[1..13] OF SINT

    # CMU identification
    CMU_ID: int = 0                                # BYTE
    CMU_Serial_No: int = 0                         # UDINT
    CMU_Lot_No: int = 0                            # UDINT