# bypass_globals.py
from BTA_A.constants import MAX_NUMBER_OF_BMU


# =========================
# Helper
# =========================
def bool_array():
    return [False] * MAX_NUMBER_OF_BMU


# =========================
# Charge – Bypass
# =========================
BMU_SELF_Nearly_Final_Charge_Detect_Bypass = bool_array()
BMU_SELF_Final_Charge_Detect_Bypass = bool_array()
BMU_SELF_Over_Charge_Warning_Bypass = bool_array()
BMU_SELF_Over_Charge_Alert_Bypass = bool_array()
BMU_SELF_Over_Charge_Fault_Bypass = bool_array()

BSC_SELF_Nearly_Final_Charge_Detect_Bypass = bool_array()
BSC_SELF_Final_Charge_Detect_Bypass = bool_array()
BSC_SELF_Over_Charge_Warning_Bypass = bool_array()
BSC_SELF_Over_Charge_Alert_Bypass = bool_array()
BSC_SELF_Over_Charge_Fault_Bypass = bool_array()


# =========================
# Discharge – Bypass
# =========================
BMU_SELF_Nearly_Final_Discharge_Detect_Bypass = bool_array()
BMU_SELF_Final_Discharge_Detect_Bypass = bool_array()
BMU_SELF_Over_Discharge_Warning_Bypass = bool_array()
BMU_SELF_Over_Discharge_Alert_Bypass = bool_array()
BMU_SELF_Over_Discharge_Fault_Bypass = bool_array()

BSC_SELF_Nearly_Final_Discharge_Detect_Bypass = bool_array()
BSC_SELF_Final_Discharge_Detect_Bypass = bool_array()
BSC_SELF_Over_Discharge_Warning_Bypass = bool_array()
BSC_SELF_Over_Discharge_Alert_Bypass = bool_array()
BSC_SELF_Over_Discharge_Fault_Bypass = bool_array()


# =========================
# Temperature – Bypass
# =========================
BMU_SELF_Cell_High_Temperature_Warning_Bypass = bool_array()
BMU_SELF_Cell_High_Temperature_Alert_Bypass = bool_array()
BMU_SELF_Module_High_Temperature_Warning_Bypass = bool_array()
BMU_SELF_Module_High_Temperature_Alert_Bypass = bool_array()
BMU_SELF_Temperature_Deviation_Warning_Bypass = bool_array()
BMU_SELF_Temperature_Deviation_Alert_Bypass = bool_array()

BSC_SELF_Cell_High_Temperature_Warning_Bypass = bool_array()
BSC_SELF_Cell_High_Temperature_Alert_Bypass = bool_array()
BSC_SELF_Module_High_Temperature_Warning_Bypass = bool_array()
BSC_SELF_Module_High_Temperature_Alert_Bypass = bool_array()
BSC_SELF_Temperature_Deviation_Warning_Bypass = bool_array()
BSC_SELF_Temperature_Deviation_Alert_Bypass = bool_array()


# =========================
# Current Leak – Bypass
# =========================
BMU_SELF_Current_Leak_Detection_Bypass = bool_array()


# =========================
# BMU – Bypass
# =========================
BMU_Abnormality_Bypass = bool_array()
BMU_substrate_Other_Failure_Bypass = bool_array()
BMU_substrate_Power_Failure_Bypass = bool_array()


# =========================
# CMU – Bypass
# =========================
CMU_Circuite_Failure_Bypass = bool_array()
CMU_Communication_failure_Bypass = bool_array()
CMU_Ground_fault_Bypass = bool_array()
CMU_Other_Failure_Bypass = bool_array()
CMU_Power_failure_Bypass = bool_array()


# =========================
# Precharge Circuit – Bypass
# =========================
Pre_charge_circuit_abnormality_Bypass = bool_array()
Pre_charge_contactor_Ground_fault_Bypass = bool_array()
Pre_charge_contactor_Short_circuit_Bypass = bool_array()


# =========================
# Main Contactors – Bypass
# =========================
Main_contactor_N_Ground_fault_Bypass = bool_array()
Main_contactor_N_Short_circuit_Bypass = bool_array()
Main_contactor_N_Welding_Bypass = bool_array()

Main_contactor_P_Ground_fault_Bypass = bool_array()
Main_contactor_P_Short_circuit_Bypass = bool_array()
Main_contactor_P_Welding_Bypass = bool_array()


# =========================
# Current Sensor – Bypass
# =========================
Current_sensor_Circuite_Failure_Bypass = bool_array()
Current_sensor_Communication_failure_Bypass = bool_array()
Current_sensor_Power_failure_Bypass = bool_array()


# =========================
# Service Disconnector – Bypass
# =========================
Main_circuit_Open_Bypass = bool_array()
Main_circuit_Other_Failure_Bypass = bool_array()


# =========================
# Current Leak Sensor – Bypass
# =========================
Current_leak_detection_Bypass = bool_array()
Current_leak_sensor_power_supply_abnormality_Bypass = bool_array()
Current_leak_sensor_pre_check_circuit_abnormality_Bypass = bool_array()


# =========================
# Ground Control Relay – Bypass
# =========================
Ground_control_relay_Ground_fault_Bypass = bool_array()
Ground_control_relay_Short_circuit_Bypass = bool_array()
Ground_control_relay_Welding_Bypass = bool_array()


# =========================
# Other – Bypass
# =========================
Non_volatile_memory_Other_Failure_Bypass = bool_array()
Non_volatile_storage_failure_Bypass = bool_array()
Other_components_Circuite_Failure_Bypass = bool_array()
Other_components_Ground_fault_Bypass = bool_array()
Other_components_Power_failure_Bypass = bool_array()
