# interlock_globals.py
from BTA_A.constants import MAX_NUMBER_OF_BMU
from DUT_BMU_ON_OFF_INTERLOCK_1 import DUT_BMU_ON_OFF_INTERLOCK_1
from DUT_BMU_ON_OFF_INTERLOCK_2 import DUT_BMU_ON_OFF_INTERLOCK_2


# PLC: ARRAY[1..MAX_NUMBER_OF_BMU]
# Python: list with fixed length

BMU_ON_OFF_INTERLOCK_1 = [
    DUT_BMU_ON_OFF_INTERLOCK_1(BMU_Index_No=i + 1)
    for i in range(MAX_NUMBER_OF_BMU)
]

BMU_ON_OFF_INTERLOCK_2 = [
    DUT_BMU_ON_OFF_INTERLOCK_2()
    for _ in range(MAX_NUMBER_OF_BMU)
]
