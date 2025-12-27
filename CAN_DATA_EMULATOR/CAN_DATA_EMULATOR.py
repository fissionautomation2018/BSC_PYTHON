# ==========================================================
# BMU-1 FULL 48-FRAME EMULATOR (Windows test)
# SPC-COM-E0088 Rev.5 compliant
# ==========================================================

BMU_NO = 1
BMU_OFFSET = BMU_NO * 0x20

def u16(val):
    return [val & 0xFF, (val >> 8) & 0xFF]

def frame(can_id, data):
    assert len(data) == 8
    return can_id, bytes(data)


def generate_bmu1_frames():
    frames = []

    sync = 1

    # ---------------- 0x20 ----------------
    frames.append(frame(
        0x20 + BMU_OFFSET,
        [
            sync,
            0b00010000,      # Status → BMU abnormality = FALSE
            0x00,            # Final charge/discharge
            0x00,            # Over/under/temp
            *u16(80000),     # SOC = 80 Ah
            *u16(95000),     # SOH = 95 Ah
        ]
    ))

    # ---------------- 0x21 ----------------
    frames.append(frame(
        0x21 + BMU_OFFSET,
        [
            sync,
            *u16(3700),
            *u16(3650),
            30,
            25,
            20,
        ]
    ))

    # ---------------- 0x22 ----------------
    frames.append(frame(
        0x22 + BMU_OFFSET,
        [
            sync,
            5,
            10,
            6,
            12,
            0,
            0,
            0,
        ]
    ))

    # ---------------- 0x23 ----------------
    frames.append(frame(
        0x23 + BMU_OFFSET,
        [
            sync,
            *u16(1000),      # Charge current
            *u16(800),       # Discharge current
            *u16(7500),      # Unit voltage
            0x00,
        ]
    ))

    # ---------------- 0x24 ----------------
    frames.append(frame(
        0x24 + BMU_OFFSET,
        [
            sync,
            *u16(300),
            *u16(250),
            *u16(200),
            0x00,
        ]
    ))

    # ---------------- 0x25 ----------------
    frames.append(frame(
        0x25 + BMU_OFFSET,
        [
            sync, 0, 0, 0, 0, 0, 0,
            80,  # SOC %
        ]
    ))

    # ---------------- 0x26 ----------------
    frames.append(frame(
        0x26 + BMU_OFFSET,
        [
            sync,
            0x00, 0x00, 0x00,  # CMU 1-22
            0x00,              # CMU 23-28
            *u16(0x0000),      # Module 28
            0x00,
        ]
    ))

    # ---------------- 0x27 – 0x2F ----------------
    module = 1
    for base in range(0x27, 0x30):
        data = [sync]
        for _ in range(3):
            data += u16(0x0000)
            module += 1
        data.append(0)
        frames.append(frame(base + BMU_OFFSET, data))

    # ---------------- Cell voltages 0x30–0x33 ----------------
    cell = 3700
    frames.append(frame(
        0x30 + BMU_OFFSET,
        [sync, *u16(cell), *u16(cell), *u16(cell), 1]
    ))
    frames.append(frame(
        0x31 + BMU_OFFSET,
        [sync, *u16(cell), *u16(cell), *u16(cell), 0]
    ))
    frames.append(frame(
        0x32 + BMU_OFFSET,
        [sync, *u16(cell), *u16(cell), *u16(cell), 0]
    ))
    frames.append(frame(
        0x33 + BMU_OFFSET,
        [sync, *u16(cell), *u16(cell), *u16(cell), 0]
    ))

    # ---------------- Cell temp (6) 0x36 ----------------
    frames.append(frame(
        0x36 + BMU_OFFSET * 3,
        [sync, 25, 25, 25, 25, 25, 25, 0]
    ))

    # ---------------- Cell temp (13) 0x37, 0x38 ----------------
    frames.append(frame(
        0x37 + BMU_OFFSET * 12,
        [sync, 25, 25, 25, 25, 25, 25, 25]
    ))
    frames.append(frame(
        0x38 + BMU_OFFSET * 12,
        [sync, 25, 25, 25, 25, 25, 25, 0]
    ))

    # ---------------- Abnormality detail 2 ----------------
    frames.append(frame(
        0x50B + BMU_NO * 0x40,
        [sync, 0, 0, 0, 0, 0, 0, 0]
    ))

    # ---------------- CMU Identification ----------------
    frames.append(frame(
        0x50C + BMU_NO * 0x50,
        [sync, 1, 0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC]
    ))

    return frames
