
import constants as consts
import BTA_005_CAN_READ_DATA_ORGANIZING
import BTA_006_BMU_READ_DATA_ORGANIZING
import BTA_007_BMU_READ_DATA_SCALING



# -----------------------------
# Helper to generate test bytes
# -----------------------------
def make_test_bytes():
    """
    Unique 8-byte pattern for validation
    """
    return bytes([
        0, # sync counter
        10, # 2nd byte
        0, # 3rd byte
        10, # 4th byte
        0, # 5th byte
        10, # 6th byte
        0, # 7th byte
        1, # 8th byte
    ])

cob_id = 80


# -----------------------------
# CAN RAW DATA ORGANIZING BMU WISE BASED ON COB-ID
# -----------------------------
BMU_CAN_READ_DATA = BTA_005_CAN_READ_DATA_ORGANIZING.BMU_CAN_DATA_ORGANIZING()
BMU_CAN_READ_DATA.process_single_frame(
    cob_id,
    make_test_bytes()
)
#---------------------------------------------

# -----------------------------
# Verification
# -----------------------------
ALL_BMU_DATA = BMU_CAN_READ_DATA.bmus

# -------------------------------------------------
# EACH BMU CAN RAW DATA ORGANIZING TO BMU INPUT DATA STRUCTURE BYTEWISE
# -------------------------------------------------
BMU_READ_DATA_INPUT = []  # Initialize variable
for bmu_raw in ALL_BMU_DATA:
    # Decode raw CAN frames into structured data
    BMU_READ_DATA_INPUT.append(BTA_006_BMU_READ_DATA_ORGANIZING.BMU_READ_DATA_ORGANIZING(
        bmu_raw
    ))
#-------------------------------------------------

# -------------------------------------------------
# BMU INPUT DATA STRUCTURE TO BMU LOCAL DATA STRUCTURE SCALINGWISE
# -------------------------------------------------
BMU_READ_DATA_LOCAL_LIST = []
for bmu_data in BMU_READ_DATA_INPUT:
    BMU_READ_DATA_LOCAL_LIST.append(
        BTA_007_BMU_READ_DATA_SCALING.BMU_READ_DATA_SCALING(bmu_data)
    )
#-------------------------------------------------








# -----------------------------
 # ONLY FOR TESTING PURPOSES
# -----------------------------
# # Example: Print the first BMU's local data
# for key, value in BMU_READ_DATA_LOCAL_LIST[0].__dict__.items():
#     print(f"{key}: {value}")

print(f"Data_Aquisition_Location : ", BMU_READ_DATA_INPUT[0].Data_Aquisition_Location)

for i in range(0,56):
    print(f"Cell_Voltage[{i}] : ", BMU_READ_DATA_LOCAL_LIST[0].Cell_Voltage[i])


