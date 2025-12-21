from dataclasses import dataclass


@dataclass
class DUT_BMU_WRITE_DATA_OUTPUT:
    """
    PLC TYPE: DUT_BMU_WRITE_DATA_OUTPUT
    Direct Python equivalent
    """

    Sync_Counter: int = 0              # USINT  (0..255)
    Status: int = 0                    # USINT  (0..255)
    Main_Circuit_Voltage: int = 0      # UINT   (0..65535)

    Reserved_Byte_3: int = 0           # USINT
    Reserved_Byte_4: int = 0           # USINT
    Reserved_Byte_5: int = 0           # USINT
    Reserved_Byte_6: int = 0           # USINT

    Time_Lower_32_bits: int = 0        # UDINT  (0..4294967295)
    Time_Higher_32_bits: int = 0       # UDINT  (0..4294967295)

    Data_Aquisition_Location: int = 0  # USINT
