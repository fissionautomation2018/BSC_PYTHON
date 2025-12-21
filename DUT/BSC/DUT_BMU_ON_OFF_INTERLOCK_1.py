from dataclasses import dataclass

@dataclass
class DUT_BMU_ON_OFF_INTERLOCK_1:
    BMU_Index_No: int = 0
    BMU_ON_OFF_DECISION_BASED_ON_BMU_VOLTAGE_AND_SOC: bool = False
    BMU_Unit_Value: float = 0.0
