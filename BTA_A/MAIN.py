import time
import can
import sys
import os
import constants as consts
import platform
import random

import BTA_005_CAN_READ_DATA_ORGANIZING
import BTA_006_BMU_READ_DATA_ORGANIZING
import BTA_007_BMU_READ_DATA_SCALING

sys.path.append(os.path.abspath("DUT/BMU"))

# ============================================================
    # BMU DATA ORGANIZER (PERSISTENT)
# ============================================================

BMU_CAN_READ_DATA_LOCAL = BTA_005_CAN_READ_DATA_ORGANIZING.BMU_CAN_DATA_ORGANIZING()


# Persistent BMU LOCAL STORAGE (DO NOT ERASE)
BMU_LOCAL_CACHE = {}   # key = bmu_id, value = DUT_BMU_READ_DATA_LOCAL


# ============================================================
# HELPER: SEND TEST FRAME (SIMULATION)
# ============================================================

def send_test_frame(cob_id: int, data: bytes):
    msg = can.Message(
        arbitration_id=cob_id,
        data=data,
        is_extended_id=False
    )
    return msg


# ============================================================
# MAIN LOOP
# ============================================================

print("Starting BMU Windows test loop...\n")


while True:

    def make_test_bytes():
        return bytes([1,10, 20, 20, 30, 40, 20, 10])

    # --------------------------------------------------------
    # SIMULATE CAN FRAME ARRIVAL
    # --------------------------------------------------------
    COB_ID = random.randint(64,767)
    print("COB_ID:", COB_ID)

    CAN_MESSAGE = send_test_frame(COB_ID, make_test_bytes())

    # --------------------------------------------------------
    # RAW CAN → BMU RAW ORGANIZATION
    # --------------------------------------------------------
    bmu_id, frame_index = BMU_CAN_READ_DATA_LOCAL.process_single_frame(
        CAN_MESSAGE.arbitration_id,
        CAN_MESSAGE.data
    )

    # --------------------------------------------------------
    # PROCESS ONLY THE BMU THAT RECEIVED THIS FRAME
    # --------------------------------------------------------
    for BMU_NO in range(0, consts.MAX_NUMBER_OF_BMU):
        if BMU_NO is not None:

            BMU_CAN_DATA_LOCAL = BMU_CAN_READ_DATA_LOCAL.BMU_CAN_RAW_DATA[BMU_NO]

            # RAW → INPUT STRUCTURE
            BMU_READ_DATA_INPUT = (
                BTA_006_BMU_READ_DATA_ORGANIZING.BMU_READ_DATA_ORGANIZING(BMU_CAN_DATA_LOCAL)
            )

            # INPUT → LOCAL (SCALING)
            BMU_READ_DATA_LOCAL = (
                BTA_007_BMU_READ_DATA_SCALING.BMU_READ_DATA_SCALING(BMU_READ_DATA_INPUT)
            )

            # ----------------------------------------------------
            # PERSIST DATA (FRAME-STICKY)
            # ----------------------------------------------------
            if BMU_NO not in BMU_LOCAL_CACHE:
                BMU_LOCAL_CACHE[BMU_NO] = BMU_READ_DATA_LOCAL
            else:
                old = BMU_LOCAL_CACHE[BMU_NO]
                for k, v in BMU_READ_DATA_LOCAL.__dict__.items():
                    if v is not None:
                        setattr(old, k, v)

        # --------------------------------------------------------
        # DISPLAY (READ-ONLY)
        # --------------------------------------------------------

        for BMU_ID, BMU_DATA in BMU_LOCAL_CACHE.items():
            print(f"\nBMU {BMU_ID + 1}")
            print(f"Data_Aquisition_Location : {BMU_DATA}")
       
        time.sleep(1)
