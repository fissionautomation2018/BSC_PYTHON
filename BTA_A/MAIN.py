
import constants as consts
import BTA_005_CAN_READ_DATA_ORGANIZING
import BTA_006_BMU_READ_DATA_ORGANIZING
import BTA_007_BMU_READ_DATA_SCALING

BMU_CAN_READ_DATA = BTA_005_CAN_READ_DATA_ORGANIZING.BMU_CAN_DATA_ORGANIZING()

# -----------------------------
# Helper to generate test bytes
# -----------------------------
def make_test_bytes(bmu_id, frame_no):
    """
    Unique 8-byte pattern for validation
    """
    return bytes([
        0x03, # sync counter
        0XFF,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00

    ])

# -----------------------------
# Send LOW RANGE frames (1–32)
# -----------------------------
for bmu in range(1, 23):            # BMU 1..22
    for frame in range(1, 33):      # Frame 1..32
        cob_id = consts.LOW_BASE_ID + (bmu - 1) * consts.LOW_RANGE_SIZE + (frame - 1) # Original line
        BMU_CAN_READ_DATA.process_single_frame(
            cob_id,
            make_test_bytes(bmu, frame)
        )

# -----------------------------
# Send HIGH RANGE frames (33–48)
# -----------------------------
for bmu in range(1, 23):             # BMU 1..22
    for frame in range(33, 49):      # Frame 33..48
        cob_id = consts.HIGH_BASE_ID + (bmu - 1) * consts.HIGH_RANGE_SIZE + (frame - 33)
        BMU_CAN_READ_DATA.process_single_frame(
            cob_id,
            make_test_bytes(bmu, frame)
        )

# -----------------------------
# Verification
# -----------------------------
ALL_BMU_DATA = BMU_CAN_READ_DATA.bmus

#################################

# -------------------------------------------------
# Decode organized data
# -------------------------------------------------

BMU_READ_DATA_INPUT = []  # Initialize variable

for bmu_raw in ALL_BMU_DATA:

    # Check completeness
    if not bmu_raw.is_complete():
        print("❌ BMU data incomplete – skipping decoding")
        continue

    # Decode raw CAN frames into structured data
    BMU_READ_DATA_INPUT.append(BTA_006_BMU_READ_DATA_ORGANIZING.BMU_READ_DATA_ORGANIZING(
        bmu_raw
    ))
####################################################

BMU_READ_DATA_LOCAL_LIST = []

for bmu_data in BMU_READ_DATA_INPUT:
    BMU_READ_DATA_LOCAL_LIST.append(
        BTA_007_BMU_READ_DATA_SCALING.BMU_READ_DATA_SCALING(bmu_data)
    )


# Example: Print the first BMU's local data
for key, value in BMU_READ_DATA_LOCAL_LIST[0].__dict__.items():
    print(f"{key}: {value}")

