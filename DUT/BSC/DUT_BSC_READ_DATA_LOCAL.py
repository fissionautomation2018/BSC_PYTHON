from dataclasses import dataclass

@dataclass
class DUT_BSC_READ_DATA_LOCAL:
    # Heartbeat & modes
    BSC_Heartbeat: int = 0                  # UINT
    BSC_Mode: int = 0                       # 0: No Op, 1: Idle, 2: Normal, 3: Fault
    BSC_Contactor_Control: int = 0          # 0: No Op, 1: Open, 2: Close
    BSC_Operation_State: int = 0            # 0: No Op, 1: Charging, 2: Discharging

    # Rack counts
    BSC_Total_Rack_Count: int = 0
    BSC_Online_Rack_Count: int = 0
    BSC_Alarm_Rack_Count: int = 0
    BSC_Warning_Rack_Count: int = 0
    BSC_Alert_Rack_Count: int = 0
    BSC_Fault_Rack_Count: int = 0
    BSC_Normal_Rack_Count: int = 0
    BSC_Cell_Balance_Rack_Count: int = 0

    # SOC / SOH (online)
    BSC_SOC: float = 0.0
    BSC_Min_SOC: float = 0.0
    BSC_Min_SOC_Rack_ID: int = 0
    BSC_Max_SOC: float = 0.0
    BSC_Max_SOC_Rack_ID: int = 0

    BSC_SOH: float = 0.0
    BSC_Min_SOH: float = 0.0
    BSC_Min_SOH_Rack_ID: int = 0
    BSC_Max_SOH: float = 0.0
    BSC_Max_SOH_Rack_ID: int = 0

    # System level values (online)
    BSC_System_SOC: float = 0.0
    BSC_Voltage: float = 0.0
    BSC_Charge_Current: float = 0.0
    BSC_Discharge_Current: float = 0.0
    BSC_Power_KW: float = 0.0

    # Power limits & deration
    BSC_Charge_Power_Limit_KW: float = 0.0
    BSC_Charge_Power_Deration_State: int = 0
    BSC_Discharge_Power_Limit_KW: float = 0.0
    BSC_Discharge_Power_Deration_State: int = 0

    # Cell voltage (online)
    BSC_Min_Cell_Voltage: float = 0.0
    BSC_Min_Cell_Voltage_Rack_No: int = 0
    BSC_Min_Cell_Voltage_Module_No: int = 0

    BSC_Max_Cell_Voltage: float = 0.0
    BSC_Max_Cell_Voltage_Rack_No: int = 0
    BSC_Max_Cell_Voltage_Module_No: int = 0

    BSC_Avg_Cell_Voltage: float = 0.0

    # Cell temperature (online)
    BSC_Min_Cell_Temperature: float = 0.0
    BSC_Min_Cell_Temperature_Rack_No: int = 0
    BSC_Min_Cell_Temperature_Module_No: int = 0

    BSC_Max_Cell_Temperature: float = 0.0
    BSC_Max_Cell_Temperature_Rack_No: int = 0
    BSC_Max_Cell_Temperature_Module_No: int = 0

    BSC_Avg_Cell_Temperature: float = 0.0

    # System averages (on/off)
    Average_SOC: float = 0.0
    Average_SOH: float = 0.0
    Average_DC_Voltage: float = 0.0

    # Cell voltage (on/off)
    Min_Cell_Voltage: float = 0.0
    Min_Cell_Voltage_Rack_No: int = 0
    Min_Cell_Voltage_Module_No: int = 0

    Max_Cell_Voltage: float = 0.0
    Max_Cell_Voltage_Rack_No: int = 0
    Max_Cell_Voltage_Module_No: int = 0

    # Cell temperature (on/off)
    Min_Cell_Temperature: float = 0.0
    Min_Cell_Temperature_Rack_No: int = 0
    Min_Cell_Temperature_Module_No: int = 0

    Max_Cell_Temperature: float = 0.0
    Max_Cell_Temperature_Rack_No: int = 0
    Max_Cell_Temperature_Module_No: int = 0
