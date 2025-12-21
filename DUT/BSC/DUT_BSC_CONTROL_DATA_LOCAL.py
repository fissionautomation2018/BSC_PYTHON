from dataclasses import dataclass, field
from typing import List
from BTA_A.constants import MAX_NUMBER_OF_BMU

@dataclass
class DUT_BSC_CONTROL_DATA_LOCAL:
    # Control source
    BSC_CONTROL_MODE: bool = False        # FALSE: TOP CONTROLLER, TRUE: DASHBOARD
    BSC_AUTO_CONTROL_MODE: bool = False   # TRUE: AUTO, FALSE: MANUAL

    # Auto mode controls
    BSC_CONTACTORS_ON_OFF: bool = False
    BSC_Battery_Idle: bool = False
    BSC_Battery_Charge: bool = False
    BSC_Battery_Discharge: bool = False

    # Setpoints
    BSC_Charge_or_Discharge_Current: int = 0  # UINT

    # Commands
    BSC_Fault_Reset: bool = False
    CELL_Data_LOG_Enable: bool = False

    # Manual mode per-BMU ON/OFF
    BMU_MANUAL_ON_OFF: List[bool] = field(
        default_factory=lambda: [False] * MAX_NUMBER_OF_BMU
    )
