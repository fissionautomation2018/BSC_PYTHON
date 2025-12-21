
from constants import *


# ==========================
# BMU DATA CLASS
# ==========================
class BMU_CAN_Data:
    def __init__(self, bmu_id):
        self.bmu_id = bmu_id
        # 48 frames × 8 bytes
        self.can_frames = [None] * MAX_FRAMES_PER_BMU

    def store_frame(self, frame_index, data_bytes):
        """
        data_bytes: bytes or bytearray (length 8)
        """
        self.can_frames[frame_index] = list(data_bytes)

    def is_complete(self):
        return all(frame is not None for frame in self.can_frames)


# ==========================
# BMU MANAGER
# ==========================
class BMU_CAN_DATA_ORGANIZING:
    def __init__(self):
        self.bmus = [BMU_CAN_Data(i + 1) for i in range(MAX_NUMBER_OF_BMU)]

    def process_single_frame(self, cob_id, data_bytes):
        """
        ONE call = ONE CAN frame
        Stores frame in correct BMU & frame index
        Returns ALL BMUs data
        """

        # -------------------------
        # LOW COB-ID RANGE
        # -------------------------
        if LOW_BASE_ID <= cob_id < LOW_BASE_ID + MAX_NUMBER_OF_BMU * LOW_RANGE_SIZE:
            offset = cob_id - LOW_BASE_ID
            bmu_index = offset // LOW_RANGE_SIZE
            frame_index = offset % LOW_RANGE_SIZE

        # -------------------------
        # HIGH COB-ID RANGE
        # -------------------------
        elif HIGH_BASE_ID <= cob_id < HIGH_BASE_ID + MAX_NUMBER_OF_BMU * HIGH_RANGE_SIZE:
            offset = cob_id - HIGH_BASE_ID
            bmu_index = offset // HIGH_RANGE_SIZE
            frame_index = 32 + (offset % HIGH_RANGE_SIZE)

        else:
            # Not a BMU frame
            return self.bmus

        # Safety check
        if bmu_index >= MAX_NUMBER_OF_BMU:
            return self.bmus

        # -------------------------
        # Store BYTE-wise data
        # -------------------------
        self.bmus[bmu_index].store_frame(frame_index, data_bytes)

        return self.bmus
