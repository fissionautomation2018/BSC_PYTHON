from dataclasses import dataclass, field
from typing import List

# MUST match PLC constant
MAX_MODULES_PER_BMU = 56   # adjust if different in your project


@dataclass
class DUT_BMU_READ_DATA_LOCAL:
    # ==========================================================
    # Status (decoded from Status byte)
    # ==========================================================
    Main_contactor_closed_status_normal_operation: bool = False
    Main_contactor_closing_waiting_status: bool = False
    Current_leak_detection_completed: bool = False
    Unit_preparation: bool = False
    BMU_abnormality: bool = False
    Pre_charge_circuit_abnormality: bool = False
    Current_leak_detection: bool = False
    BMU_life_signal_toggled_at_interval_of_960_ms: bool = False

    # ==========================================================
    # Final Charge / Discharge Info
    # ==========================================================
    Nearly_final_charge: bool = False
    Final_charge: bool = False
    Reserved_bit_01: bool = False
    Reserved_bit_02: bool = False
    Final_discharge: bool = False
    Overdischarge_warning: bool = False
    Nearly_final_discharge: bool = False
    Reserved_bit_03: bool = False

    # ==========================================================
    # Overcharge / Overdischarge / Overtemperature
    # ==========================================================
    Overcharge_alert: bool = False
    Overcharge_fault: bool = False
    Overdischarge_alert: bool = False
    Overdischarge_fault: bool = False
    High_temperature_protection: bool = False
    Over_temperature_alert: bool = False
    Reserved_bit_04: bool = False
    Reserved_bit_05: bool = False

    # ==========================================================
    # SOC / SOH / Voltage / Temperature (REAL)
    # ==========================================================
    Unit_SOC_Ah: float = 0.0
    Unit_SOH_Ah: float = 0.0
    Max_Cell_Voltage: float = 0.0
    Min_Cell_Voltage: float = 0.0
    Max_Cell_Temperature: float = 0.0
    Avg_Cell_Temperature: float = 0.0
    Min_Cell_Temperature: float = 0.0

    Max_Cell_Voltage_Module_No: int = 0
    Min_Cell_Voltage_Module_No: int = 0
    Max_Cell_Temperature_Module_No: int = 0
    Min_Cell_Temperature_Module_No: int = 0

    Unit_Charge_Current: float = 0.0
    Unit_Discharge_Current: float = 0.0
    Unit_Voltage: float = 0.0

    # ==========================================================
    # BMU Status Supplemental Information
    # ==========================================================
    Low_power_mode: bool = False
    Overcurrent: bool = False
    BMU_shutdown_permission: bool = False
    Pre_charge_contactor_state: bool = False
    Leak_detection: bool = False
    Reserved_bit_06: bool = False
    Service_disconnector_state: bool = False
    Non_volatile_storage_failure: bool = False

    # ==========================================================
    # Temperature (secondary values)
    # ==========================================================
    Max_Cell_Temperature_2: float = 0.0
    Average_Cell_Temperature_2: float = 0.0
    Min_Cell_Temperature_2: float = 0.0

    # ==========================================================
    # BMU Abnormality Detail (decoded bits)
    # ==========================================================
    CMU_Communication_failure: bool = False
    CMU_Power_failure: bool = False
    CMU_Ground_fault: bool = False
    CMU_Circuite_Failure: bool = False
    CMU_Other_Failure: bool = False

    Current_sensor_Communication_failure: bool = False
    Current_sensor_Power_failure: bool = False
    Current_sensor_Circuite_Failure: bool = False

    Main_circuit_Open: bool = False
    Main_circuit_Other_Failure: bool = False

    Ground_control_relay_Ground_fault: bool = False
    Ground_control_relay_Short_circuit: bool = False
    Ground_control_relay_Welding: bool = False

    Main_contactor_P_Ground_fault: bool = False
    Main_contactor_P_Short_circuit: bool = False
    Main_contactor_P_Welding: bool = False

    Main_contactor_N_Ground_fault: bool = False
    Main_contactor_N_Short_circuit: bool = False
    Main_contactor_N_Welding: bool = False

    Pre_charge_contactor_Ground_fault: bool = False
    Pre_charge_contactor_Short_circuit: bool = False

    BMU_substrate_Power_Failure: bool = False
    BMU_substrate_Other_Failure: bool = False

    Non_volatile_memory_Other_Failure: bool = False

    Other_components_Power_failure: bool = False
    Other_components_Ground_fault: bool = False
    Other_components_Circuite_Failure: bool = False

    Unit_SOC_Percentage: float = 0.0

    # ==========================================================
    # CMU / Cell failure & balance
    # ==========================================================
    CMU_Failure_Flag: List[bool] = field(
        default_factory=lambda: [False] * MAX_MODULES_PER_BMU
    )

    Cell_Failure_Flag: List[List[bool]] = field(
        default_factory=lambda: [
            [False] * 12 for _ in range(MAX_MODULES_PER_BMU)
        ]
    )

    Cell_Balance_Status: List[bool] = field(
        default_factory=lambda: [False] * MAX_MODULES_PER_BMU
    )

    Parallel_No_Of_Branch: int = 0
    Data_Aquisition_Location: int = 0

    # ==========================================================
    # Cell level data
    # ==========================================================
    Cell_Voltage: List[List[float]] = field(
        default_factory=lambda: [
            [0.0] * 12 for _ in range(MAX_MODULES_PER_BMU)
        ]
    )

    Cell_Temperature: List[List[float]] = field(
        default_factory=lambda: [
            [0.0] * 6 for _ in range(MAX_MODULES_PER_BMU)
        ]
    )

    Cell_Temperature_1: List[List[float]] = field(
        default_factory=lambda: [
            [0.0] * 13 for _ in range(MAX_MODULES_PER_BMU)
        ]
    )

    # ==========================================================
    # BMU abnormality detail 2 (modules > 28)
    # ==========================================================
    Current_sensor_abnormality_sensor_body: bool = False
    Current_sensor_abnormality_power_supply: bool = False
    Current_sensor_abnormality_signal_line: bool = False
    CMU_UART_communication_abnormality: bool = False
    CMU_abnormality: bool = False
    CMU_power_supply_abnormality: bool = False
    CMU_power_supply_shutdown_abnormality: bool = False
    CMU_CAN_communication_abnormality: bool = False
    Main_contactor_P_drive_circuit_short_circuit: bool = False
    Main_contactor_P_drive_circuit_ground_fault: bool = False
    GND_control_relay_welding: bool = False
    GND_control_relay_drive_circuit_short_circuit: bool = False
    GND_control_relay_drive_circuit_ground_fault: bool = False
    SDC_failure_or_Fusing_or_Cable_error_between_modules_open_or_Contacto_open_failure: bool = False
    Reserved_bit_07: bool = False
    SDC_open: bool = False
    Parallel_connection_configuration_abnormality: bool = False
    AD_reference_voltage_abnormality: bool = False
    Pre_charge_contactor_drive_circuit_short_circuit: bool = False
    Pre_charge_contactor_drive_circuit_ground_fault: bool = False
    Main_contactor_N_welding_1: bool = False
    Main_contactor_N_drive_circuit_short_circuit: bool = False
    Main_contactor_N_drive_circuit_ground_fault: bool = False
    Main_contactor_P_welding_1: bool = False
    Reserved_8: bool = False
    Current_leak_sensor_pre_check_circuit_abnormality: bool = False
    Cable_error_between_modules_ground_fault_or_current_leak_detection: bool = False
    Current_leak_sensor_power_supply_abnormality: bool = False
    Backup_abnormality: bool = False
    Reserved_9: bool = False

    # ==========================================================
    # Local calculated data
    # ==========================================================
    BMU_Cell_Balance_Status: bool = False

    # ==========================================================
    # CMU identification
    # ==========================================================
    CMU_ID: int = 0
    CMU_Serial_No: int = 0
    CMU_Lot_No: int = 0
