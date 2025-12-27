from constants import *

class BMU_CAN_Data:
    def __init__(self):
        self.can_frames = [None] * MAX_FRAMES_PER_BMU


class BMU_CAN_DATA_ORGANIZING:
    def __init__(self):
        self.BMU_CAN_RAW_DATA = [
            BMU_CAN_Data() for _ in range(MAX_NUMBER_OF_BMU)
        ]

    def process_single_frame(self, cob_id, data_bytes):
        """
        Stores one CAN frame persistently.
        Returns:
            (bmu_index, frame_index) or (None, None)
        """

        # -------- LOW RANGE (32 frames) --------
        for bmu_index in range(MAX_NUMBER_OF_BMU):
            base = 32 + (bmu_index + 1) * 32
            if base <= cob_id < base + 32:
                frame_index = cob_id - base
                self.BMU_CAN_RAW_DATA[bmu_index].can_frames[frame_index] = list(data_bytes)
                return bmu_index, frame_index

        # -------- HIGH RANGE (16 frames) --------
        for bmu_index in range(MAX_NUMBER_OF_BMU):
            base = 1280 + (bmu_index + 1) * 16
            if base <= cob_id < base + 16:
                frame_index = 32 + (cob_id - base)
                self.BMU_CAN_RAW_DATA[bmu_index].can_frames[frame_index] = list(data_bytes)
                return bmu_index, frame_index

        return None, None