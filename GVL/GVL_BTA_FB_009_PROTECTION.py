# alarms_globals.py
from BTA_A.constants import MAX_NUMBER_OF_BMU
from datetime import timedelta


# =========================
# Helper for BOOL arrays
# =========================
def bool_array():
    return [False] * MAX_NUMBER_OF_BMU


# =========================
# Charge
# =========================
BMU_SELF_Nearly_Final_Charge_Detect = bool_array()
BMU_SELF_Final_Charge_Detect = bool_array()
BMU_SELF_Over_Charge_Warning = bool_array()
BMU_SELF_Over_Charge_Alert = bool_array()
BMU_SELF_Over_Charge_Fault = bool_array()

BSC_SELF_Nearly_Final_Charge_Detect = bool_array()
BSC_SELF_Final_Charge_Detect = bool_array()
BSC_SELF_Over_Charge_Warning = bool_array()
BSC_SELF_Over_Charge_Alert = bool_array()
BSC_SELF_Over_Charge_Fault = bool_array()

BSC_SELF_Over_Charge_Power_Warning = False
BSC_SELF_Over_Charge_Power_Alert = False


# =========================
# Discharge
# =========================
BMU_SELF_Nearly_Final_Discharge_Detect = bool_array()
BMU_SELF_Final_Discharge_Detect = bool_array()
BMU_SELF_Over_Discharge_Warning = bool_array()
BMU_SELF_Over_Discharge_Alert = bool_array()
BMU_SELF_Over_Discharge_Fault = bool_array()

BSC_SELF_Nearly_Final_Discharge_Detect = bool_array()
BSC_SELF_Final_Discharge_Detect = bool_array()
BSC_SELF_Over_Discharge_Warning = bool_array()
BSC_SELF_Over_Discharge_Alert = bool_array()
BSC_SELF_Over_Discharge_Fault = bool_array()

BSC_SELF_Over_Discharge_Power_Warning = False
BSC_SELF_Over_Discharge_Power_Alert = False


# =========================
# Temperature
# =========================
BMU_SELF_Cell_High_Temperature_Warning = bool_array()
BMU_SELF_Cell_High_Temperature_Alert = bool_array()
BMU_SELF_Module_High_Temperature_Warning = bool_array()
BMU_SELF_Module_High_Temperature_Alert = bool_array()
BMU_SELF_Temperature_Deviation_Warning = bool_array()
BMU_SELF_Temperature_Deviation_Alert = bool_array()

BSC_SELF_Cell_High_Temperature_Warning = bool_array()
BSC_SELF_Cell_High_Temperature_Alert = bool_array()
BSC_SELF_Module_High_Temperature_Warning = bool_array()
BSC_SELF_Module_High_Temperature_Alert = bool_array()
BSC_SELF_Temperature_Deviation_Warning = bool_array()
BSC_SELF_Temperature_Deviation_Alert = bool_array()


# =========================
# Current Leak
# =========================
BMU_SELF_Current_Leak_Detection = bool_array()


# =========================
# BMU / CMU / Hardware
# =========================
BMU_ALARM = bool_array()
BMU_FAULT = bool_array()

CMU_ALARM = bool_array()
CMU_FAULT = bool_array()

ANY_CMU_FAILURE_ALARM = bool_array()
ANY_CMU_FAILURE_FAULT = bool_array()

ANY_CELL_FAILURE_ALARM = bool_array()
ANY_CELL_FAILURE_FAULT = bool_array()

PRECHARGE_CIRCUIT_ALARM = bool_array()
PRECHARGE_CIRCUIT_FAULT = bool_array()

MAIN_CONTACTORS_ALARM = bool_array()
MAIN_CONTACTORS_FAULT = bool_array()

CURRENT_SENSOR_ALARM = bool_array()
CURRENT_SENSOR_FAULT = bool_array()

MAIN_CIRCUIT_ALARM = bool_array()
MAIN_CIRCUIT_FAULT = bool_array()

CURRENT_LEAK_SENSOR_ALARM = bool_array()
CURRENT_LEAK_SENSOR_FAULT = bool_array()

GROUND_CONTROL_RELAY_ALARM = bool_array()
GROUND_CONTROL_RELAY_FAULT = bool_array()

OTHER_INFO = bool_array()
OTHER_WARNING = bool_array()
OTHER_ALARM = bool_array()
OTHER_FAULT = bool_array()


# =========================
# Scenario flags
# =========================
SCENARIO_A0 = bool_array()  # NORMAL
SCENARIO_A1 = bool_array()  # WARNING
SCENARIO_B = bool_array()   # ALERT
SCENARIO_C = bool_array()   # FAULT


# =========================
# TIME parameters (PLC TIME)
# =========================
BSC_SELF_Nearly_Final_Charge_Detect_TON_TIME = timedelta(milliseconds=300)
BSC_SELF_Nearly_Final_Charge_Detect_TOFF_TIME = timedelta(milliseconds=100)

BSC_SELF_Final_Charge_Detect_TON_TIME = timedelta(milliseconds=300)
BSC_SELF_Final_Charge_Detect_TOFF_TIME = timedelta(milliseconds=100)

BSC_SELF_Over_Charge_Warning_TON_TIME = timedelta(milliseconds=300)
BSC_SELF_Over_Charge_Warning_TOFF_TIME = timedelta(milliseconds=100)

BSC_SELF_Over_Charge_Alert_TON_TIME = timedelta(milliseconds=300)
BSC_SELF_Over_Charge_Alert_TOFF_TIME = timedelta(milliseconds=100)

BSC_SELF_Over_Charge_Fault_TON_TIME = timedelta(milliseconds=300)
BSC_SELF_Over_Charge_Fault_TOFF_TIME = timedelta(milliseconds=100)


# =========================
# Thresholds
# =========================
BSC_SELF_Nearly_Final_Charge_Detect_Max_Cell_Voltage = 2.67
BSC_SELF_Final_Charge_Detect_Max_Cell_Voltage = 2.67
BSC_SELF_Over_Charge_Warning_Max_Cell_Voltage = 2.67
BSC_SELF_Over_Charge_Alert_Max_Cell_Voltage = 2.67
BSC_SELF_Over_Charge_Fault_Max_Cell_Voltage = 2.67

BSC_SELF_Nearly_Final_Discharge_Detect_Min_Cell_Voltage = 1.5
BSC_SELF_Final_Discharge_Detect_Min_Cell_Voltage = 1.5
BSC_SELF_Over_Discharge_Warning_Min_Cell_Voltage = 1.5
BSC_SELF_Over_Discharge_Alert_Min_Cell_Voltage = 1.5
BSC_SELF_Over_Discharge_Fault_Min_Cell_Voltage = 1.5


# =========================
# C-Rate tables
# =========================
C_Rate_for_Below_One_Percent_SOH = 0.0
C_Rate_for_One_to_Twenty_Percent_SOH = 0.05
C_Rate_for_Twenty_to_Fourty_Percent_SOH = 0.2
C_Rate_for_Fourty_to_Sixty_Percent_SOH = 0.5
C_Rate_for_Sixty_to_Hundred_Percent_SOH = 1.0
