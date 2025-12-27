import sys
import os

sys.path.append(os.path.abspath("DUT/BMU"))
from constants import MAX_MODULES_PER_BMU

from DUT_BMU_READ_DATA_LOCAL import DUT_BMU_READ_DATA_LOCAL, MAX_MODULES_PER_BMU

def GET_BIT(val: int, bit: int) -> bool:
    return bool(val & (1 << bit))

def MT_BMU_ABNORMALITY_DETAIL(code: int, local):
    """
    Decodes BMU_Abnormality_Detail into flags
    """
    local.BMU_substrate_Power_Failure = False
    local.BMU_substrate_Other_Failure = False
    local.CMU_Communication_failure = False
    local.CMU_Power_failure = False
    local.CMU_Ground_fault = False
    local.CMU_Circuite_Failure = False
    local.CMU_Other_Failure = False
    local.Current_sensor_Communication_failure = False
    local.Current_sensor_Power_failure = False
    local.Current_sensor_Circuite_Failure = False
    local.Ground_control_relay_Ground_fault = False
    local.Ground_control_relay_Short_circuit = False
    local.Ground_control_relay_Welding = False
    local.Main_contactor_P_Ground_fault = False
    local.Main_contactor_P_Short_circuit = False
    local.Main_contactor_P_Welding = False
    local.Main_contactor_N_Ground_fault = False
    local.Main_contactor_N_Short_circuit = False
    local.Main_contactor_N_Welding = False
    local.Pre_charge_contactor_Ground_fault = False
    local.Pre_charge_contactor_Short_circuit = False
    local.Non_volatile_memory_Other_Failure = False
    local.Other_components_Power_failure = False
    local.Other_components_Ground_fault = False
    local.Other_components_Circuite_Failure = False
    local.Main_circuit_Open = False
    local.Main_circuit_Other_Failure = False
    
    
    # PLC CASE mapping
    if code == 130:
        local.BMU_substrate_Power_Failure = True
    elif code == 143:
        local.BMU_substrate_Other_Failure = True
    elif code == 17:
        local.CMU_Communication_failure = True
    elif code == 18:
        local.CMU_Power_failure = True
    elif code == 19:
        local.CMU_Ground_fault = True
    elif code == 23:
        local.CMU_Circuite_Failure = True
    elif code == 31:
        local.CMU_Other_Failure = True
    elif code == 33:    
        local.Current_sensor_Communication_failure = True
    elif code == 34:
        local.Current_sensor_Power_failure = True
    elif code == 39:
        local.Current_sensor_Circuite_Failure = True
    elif code == 67:
        local.Ground_control_relay_Ground_fault = True
    elif code == 68:
        local.Ground_control_relay_Short_circuit = True
    elif code == 69:
        local.Ground_control_relay_Welding = True
    elif code == 83:
        local.Main_contactor_P_Ground_fault = True
    elif code == 84:
        local.Main_contactor_P_Short_circuit = True
    elif code == 85:
        local.Main_contactor_P_Welding = True
    elif code == 99:
        local.Main_contactor_N_Ground_fault = True
    elif code == 100:
        local.Main_contactor_N_Short_circuit = True
    elif code == 101:
        local.Main_contactor_N_Welding = True
    elif code == 115:
        local.Pre_charge_contactor_Ground_fault = True
    elif code == 116:
        local.Pre_charge_contactor_Short_circuit = True
    elif code == 159:
        local.Non_volatile_memory_Other_Failure = True
    elif code == 242:
        local.Other_components_Power_failure = True
    elif code == 243:
        local.Other_components_Ground_fault = True
    elif code == 247:
        local.Other_components_Circuite_Failure = True
    elif code == 54:
        local.Main_circuit_Open = True
    elif code == 63:
        local.Main_circuit_Other_Failure = True


def BMU_READ_DATA_SCALING(BMU_DATA_INPUT):
    """
    BMU_DATA_INPUT  -> RAW decoded BMU frame structure
    RETURNS         -> DUT_BMU_READ_DATA_LOCAL
    """

    BMU_READ_DATA_LOCAL = DUT_BMU_READ_DATA_LOCAL()

    # ==========================================================
    # STATUS BYTE
    # ==========================================================
    s = BMU_DATA_INPUT.Status
    BMU_READ_DATA_LOCAL.Main_contactor_closed_status_normal_operation = GET_BIT(s, 0)
    BMU_READ_DATA_LOCAL.Main_contactor_closing_waiting_status = GET_BIT(s, 1)
    BMU_READ_DATA_LOCAL.Current_leak_detection_completed = GET_BIT(s, 2)
    BMU_READ_DATA_LOCAL.Unit_preparation = GET_BIT(s, 3)
    BMU_READ_DATA_LOCAL.BMU_abnormality = GET_BIT(s, 4)
    BMU_READ_DATA_LOCAL.Pre_charge_circuit_abnormality = GET_BIT(s, 5)
    BMU_READ_DATA_LOCAL.Current_leak_detection = GET_BIT(s, 6)
    BMU_READ_DATA_LOCAL.BMU_life_signal_toggled_at_interval_of_960_ms = GET_BIT(s, 7)

    # ==========================================================
    # FINAL CHARGE / DISCHARGE
    # ==========================================================
    f = BMU_DATA_INPUT.Final_Charge_or_Discharge_info
    BMU_READ_DATA_LOCAL.Nearly_final_charge = GET_BIT(f, 0)
    BMU_READ_DATA_LOCAL.Final_charge = GET_BIT(f, 1)
    BMU_READ_DATA_LOCAL.Final_discharge = GET_BIT(f, 4)
    BMU_READ_DATA_LOCAL.Overdischarge_warning = GET_BIT(f, 5)
    BMU_READ_DATA_LOCAL.Nearly_final_discharge = GET_BIT(f, 6)

    # ==========================================================
    # OVER CHARGE / DISCHARGE / TEMP
    # ==========================================================
    o = BMU_DATA_INPUT.Overcharge_or_Overdischarge_or_Overtemperature
    BMU_READ_DATA_LOCAL.Overcharge_alert = GET_BIT(o, 0)
    BMU_READ_DATA_LOCAL.Overcharge_fault = GET_BIT(o, 1)
    BMU_READ_DATA_LOCAL.Overdischarge_alert = GET_BIT(o, 2)
    BMU_READ_DATA_LOCAL.Overdischarge_fault = GET_BIT(o, 3)
    BMU_READ_DATA_LOCAL.High_temperature_protection = GET_BIT(o, 4)
    BMU_READ_DATA_LOCAL.Over_temperature_alert = GET_BIT(o, 5)

    # ==========================================================
    # SOC / SOH
    # ==========================================================
    # SOC IN AH
    BMU_READ_DATA_LOCAL.Unit_SOC_Ah = 0.0 if BMU_DATA_INPUT.Unit_SOC >= 65535 else BMU_DATA_INPUT.Unit_SOC / 1000.0
    # SOH IN AH
    BMU_READ_DATA_LOCAL.Unit_SOH_Ah = 0.0 if BMU_DATA_INPUT.Unit_SOH >= 65535 else BMU_DATA_INPUT.Unit_SOH / 1000.0

    # ==========================================================
    # VOLTAGE
    # ==========================================================
    # MAX CELL VOLTAGE
    BMU_READ_DATA_LOCAL.Max_Cell_Voltage = (
        0.0 if BMU_DATA_INPUT.Max_Cell_Voltage >= 65534
        else BMU_DATA_INPUT.Max_Cell_Voltage / 1000.0
    )
    # MIN CELL VOLTAGE
    BMU_READ_DATA_LOCAL.Min_Cell_Voltage = BMU_DATA_INPUT.Min_Cell_Voltage / 1000.0

    # ==========================================================
    # TEMPERATURE
    # ==========================================================
    # MAX CELL TEMPERATURE
    BMU_READ_DATA_LOCAL.Max_Cell_Temperature = (
        0.0 if BMU_DATA_INPUT.Max_Cell_Temperature >= 127
        else float(BMU_DATA_INPUT.Max_Cell_Temperature)
    )
    # AVG CELL TEMPERATURE
    BMU_READ_DATA_LOCAL.Avg_Cell_Temperature = (
        0.0 if BMU_DATA_INPUT.Avg_Cell_Temperature >= 127
        else float(BMU_DATA_INPUT.Avg_Cell_Temperature)
    )
    # MIN CELL TEMPERATURE
    BMU_READ_DATA_LOCAL.Min_Cell_Temperature = float(BMU_DATA_INPUT.Min_Cell_Temperature)

    # ==========================================================
    # MODULE NO
    # ==========================================================
    # MAX CELL VOLTAGE MODULE NO
    BMU_READ_DATA_LOCAL.Max_Cell_Voltage_Module_No = BMU_DATA_INPUT.Max_Cell_Voltage_Module_No
    # MIN CELL VOLTAGE MODULE NO
    BMU_READ_DATA_LOCAL.Min_Cell_Voltage_Module_No = BMU_DATA_INPUT.Min_Cell_Voltage_Module_No
    # MAX CELL TEMPERATURE MODULE NO
    BMU_READ_DATA_LOCAL.Max_Cell_Temperature_Module_No = BMU_DATA_INPUT.Max_Cell_Temperature_Module_No
    # MIN CELL TEMPERATURE MODULE NO
    BMU_READ_DATA_LOCAL.Min_Cell_Temperature_Module_No = BMU_DATA_INPUT.Min_Cell_Temperature_Module_No

    # ==========================================================
    # CURRENT
    # ==========================================================
    # UNIT CHRARGE CURRENT
    BMU_READ_DATA_LOCAL.Unit_Charge_Current = BMU_DATA_INPUT.Unit_Charge_Current / 100.0
    # UNIT DISCHARGE CURRENT
    BMU_READ_DATA_LOCAL.Unit_Discharge_Current = BMU_DATA_INPUT.Unit_Discharge_Current / 100.0

    # UNIT VOLTAGE
    BMU_READ_DATA_LOCAL.Unit_Voltage = BMU_DATA_INPUT.Unit_Voltage / 10.0

    # ================================================================
     # BMU STATUS SUPPLMENTAL INFORMATION
     # ================================================================
    l = BMU_DATA_INPUT.BMU_Status_Supplemental_Information
    BMU_READ_DATA_LOCAL.Low_power_mode = GET_BIT(l, 0)
    BMU_READ_DATA_LOCAL.Overcurrent = GET_BIT(l, 1)
    BMU_READ_DATA_LOCAL.BMU_shutdown_permission = GET_BIT(l, 2)
    BMU_READ_DATA_LOCAL.Pre_charge_contactor_state = GET_BIT(l, 3)
    BMU_READ_DATA_LOCAL.Leak_detection = GET_BIT(l, 4)
    BMU_READ_DATA_LOCAL.Reserved_bit_06 = GET_BIT(l, 5)
    BMU_READ_DATA_LOCAL.Service_disconnector_state = GET_BIT(l, 6)
    BMU_READ_DATA_LOCAL.Non_volatile_storage_failure = GET_BIT(l, 7)


    # MAX CELL TEMPERATURE 2
    BMU_READ_DATA_LOCAL.Max_Cell_Temperature_2 = (
        0.0 if BMU_DATA_INPUT.Max_Cell_Temperature_2 >= 32767
        else float(BMU_DATA_INPUT.Max_Cell_Temperature_2) / 10.0
    )

    # AVG CELL TEMPERATURE 2
    BMU_READ_DATA_LOCAL.Average_Cell_Temperature_2 = (
        0.0 if BMU_DATA_INPUT.Average_Cell_Temperature_2 >= 32767
        else float(BMU_DATA_INPUT.Average_Cell_Temperature_2) / 10.0
    )

    # MIN CELL TEMPERATURE 2
    BMU_READ_DATA_LOCAL.Min_Cell_Temperature_2 = BMU_DATA_INPUT.Min_Cell_Temperature_2 / 10.0

    # ==========================================================
    # ABNORMALITY DETAIL
    # ==========================================================
    MT_BMU_ABNORMALITY_DETAIL(
        BMU_DATA_INPUT.BMU_Abnormality_Detail,
        BMU_READ_DATA_LOCAL
    )

    # ==========================================================
    # SOC %
    # ==========================================================
    BMU_READ_DATA_LOCAL.Unit_SOC_Percentage = (
        0.0 if BMU_DATA_INPUT.Unit_SOC_Percentage >= 255
        else float(BMU_DATA_INPUT.Unit_SOC_Percentage)
    )

    # ==========================================================
    # CMU FAILURE FLAGS
    # ==========================================================
    for i in range(22):
        BMU_READ_DATA_LOCAL.CMU_Failure_Flag[i] = GET_BIT(
            BMU_DATA_INPUT.CMU_Failure_Status_Module_1to22, i
        )

    for i in range(6):
        BMU_READ_DATA_LOCAL.CMU_Failure_Flag[22 + i] = GET_BIT(
            BMU_DATA_INPUT.CMU_Failure_Status_Module_23to28, i
        )

    
    # ==========================================================
    # CELL FAILURE FLAGS
    # ==========================================================

    for MODULE_NO in range(MAX_MODULES_PER_BMU):
        word = BMU_DATA_INPUT.Module_Cell_Failure_or_Balance_Status[MODULE_NO]

        # Cell failure bits (0..11)
        for CELL_NO in range(12):
            BMU_READ_DATA_LOCAL.Cell_Failure_Flag[MODULE_NO][CELL_NO] = bool(
                (word >> CELL_NO) & 0x01
            )

        # Balance status (bit 15)
        BMU_READ_DATA_LOCAL.Cell_Balance_Status[MODULE_NO] = bool(
            (word >> 15) & 0x01
        )


        BMU_READ_DATA_LOCAL.Data_Aquisition_Location = BMU_DATA_INPUT.Data_Aquisition_Location
        
        # DATA ACQUISITION LOCATION (1-based)
        MODULE_NO = BMU_DATA_INPUT.Data_Aquisition_Location - 1

        if 0 <= MODULE_NO < MAX_MODULES_PER_BMU:
            for CELL_NO in range(12):
                raw = BMU_DATA_INPUT.Cell_Voltage[CELL_NO]
                BMU_READ_DATA_LOCAL.Cell_Voltage[MODULE_NO][CELL_NO] = (
                    0.0 if raw >= 65534 else raw / 1000.0
                )


        # CELL TEMPERATURE IN PARTICULAR MODULE
        for CELL_NO in range(6):
            if BMU_READ_DATA_LOCAL.Data_Aquisition_Location == MODULE_NO + 1:
                BMU_READ_DATA_LOCAL.Cell_Temperature[CELL_NO] = (
                    0.0 if BMU_DATA_INPUT.Cell_Temperature[CELL_NO] >= 127
                    else float(BMU_DATA_INPUT.Cell_Temperature[CELL_NO])
                )
                MODULE_NUMBER = BMU_READ_DATA_LOCAL.Data_Aquisition_Location
        # CELL TEMPERATURE 1 IN PARTICULAR MODULE
        for CELL_NO in range(13):
            if BMU_READ_DATA_LOCAL.Data_Aquisition_Location == MODULE_NO + 1:
                BMU_READ_DATA_LOCAL.Cell_Temperature_1[CELL_NO] = (
                    0.0 if BMU_DATA_INPUT.Cell_Temperature_1[CELL_NO] >= 127
                    else float(BMU_DATA_INPUT.Cell_Temperature_1[CELL_NO])
                )
                MODULE_NUMBER = BMU_READ_DATA_LOCAL.Data_Aquisition_Location



    # BMU ABNORMALITY DETAIL 2 BYTE 2
    BMU_READ_DATA_LOCAL.Current_sensor_abnormality_sensor_body = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 7
    )
    BMU_READ_DATA_LOCAL.Current_sensor_abnormality_power_supply = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 6
    )
    BMU_READ_DATA_LOCAL.Current_sensor_abnormality_signal_line = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 5
    )
    BMU_READ_DATA_LOCAL.CMU_UART_communication_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 4
    )
    BMU_READ_DATA_LOCAL.CMU_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 3
    )
    BMU_READ_DATA_LOCAL.CMU_power_supply_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 2
    )
    BMU_READ_DATA_LOCAL.CMU_power_supply_shutdown_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 1
    )
    BMU_READ_DATA_LOCAL.CMU_CAN_communication_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_2, 0
    )

    # BMU ABNORMALITY DETAIL 2 BYTE 3
    BMU_READ_DATA_LOCAL.Main_contactor_P_drive_circuit_short_circuit = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3, 7
    )
    BMU_READ_DATA_LOCAL.Main_contactor_P_drive_circuit_ground_fault = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3 , 6
    )
    BMU_READ_DATA_LOCAL.GND_control_relay_welding = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3, 5
    )
    BMU_READ_DATA_LOCAL.GND_control_relay_drive_circuit_short_circuit = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3, 4
    )
    BMU_READ_DATA_LOCAL.GND_control_relay_drive_circuit_ground_fault = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3, 3
    )
    BMU_READ_DATA_LOCAL.SDC_failure_or_Fusing_or_Cable_error_between_modules_open_or_Contacto_open_failure = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3, 2
    )
    BMU_READ_DATA_LOCAL.Reserved_bit_07 = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3, 1
    )
    BMU_READ_DATA_LOCAL.SDC_open = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_3 , 0
    )

    # BMU ABNORMALITY DETAIL 2 BYTE 4
    BMU_READ_DATA_LOCAL.Parallel_connection_configuration_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 7
    )
    BMU_READ_DATA_LOCAL.AD_reference_voltage_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 6
    )
    BMU_READ_DATA_LOCAL.Pre_charge_contactor_drive_circuit_short_circuit = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 5
    )
    BMU_READ_DATA_LOCAL.Pre_charge_contactor_drive_circuit_ground_fault = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 4
    )
    BMU_READ_DATA_LOCAL.Main_contactor_N_welding_1 = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 3
    )
    BMU_READ_DATA_LOCAL.Main_contactor_N_drive_circuit_short_circuit = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 2
    )
    BMU_READ_DATA_LOCAL.Main_contactor_N_drive_circuit_ground_fault = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 1
    )
    BMU_READ_DATA_LOCAL.Main_contactor_P_welding_1 = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_4, 0
    )

    # BMU ABNORMALITY DETAIL 2 BYTE 5
    BMU_READ_DATA_LOCAL.Current_leak_sensor_pre_check_circuit_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_5, 3
    )
    BMU_READ_DATA_LOCAL.Cable_error_between_modules_ground_fault_or_current_leak_detection = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_5, 2
    )
    BMU_READ_DATA_LOCAL.Current_leak_sensor_power_supply_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_5, 1
    )
    BMU_READ_DATA_LOCAL.Backup_abnormality = GET_BIT(
        BMU_DATA_INPUT.BMU_Abnormality_Detail_2_BYTE_5, 0
    )
  
    # ==========================================================
    # CMU IDENTIFICATION
    # ==========================================================
    BMU_READ_DATA_LOCAL.CMU_ID = BMU_DATA_INPUT.CMU_ID
    BMU_READ_DATA_LOCAL.CMU_Serial_No = BMU_DATA_INPUT.CMU_Serial_No
    BMU_READ_DATA_LOCAL.CMU_Lot_No = BMU_DATA_INPUT.CMU_Lot_No

    return BMU_READ_DATA_LOCAL
