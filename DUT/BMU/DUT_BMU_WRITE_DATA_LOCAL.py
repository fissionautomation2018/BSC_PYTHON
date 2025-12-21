from dataclasses import dataclass

@dataclass
class DUT_BMU_WRITE_DATA_LOCAL:
    # Header / raw fields
    Sync_Counter: int = 0                  # UINT
    Status: int = 0                        # USINT (packed from bits below)
    Main_Circuit_Voltage: float = 0.0      # REAL

    Reserved_Byte_3: int = 0
    Reserved_Byte_4: int = 0
    Reserved_Byte_5: int = 0
    Reserved_Byte_6: int = 0

    Time_Value_ms: int = 0                 # TIME mapped to milliseconds
    Data_Aquisition_Location: int = 0      # USINT

    # ---- Status bit breakdown ----
    Operation_Instruction: bool = False                    # bit 0
    Power_Failure_Trip_Instruction: bool = False           # bit 1
    Cell_Balance_Permit_Signal: bool = False               # bit 2
    Current_Leak_Detection_Instruction_Signal: bool = False# bit 3
    Host_System_Life_Signal: bool = False                  # bit 7

    # ---- Command flags ----
    Contactors_ON: bool = False
    Contactors_OFF: bool = False
    Battery_Idle: bool = False
    Battery_Charge: bool = False
    Battery_Discharge: bool = False
    Fault_Reset: bool = False

    # ============================
    # PACK STATUS BYTE (PLC EXACT)
    # ============================
    def pack_status(self) -> int:
        status = 0
        status |= int(self.Operation_Instruction) << 0
        status |= int(self.Power_Failure_Trip_Instruction) << 1
        status |= int(self.Cell_Balance_Permit_Signal) << 2
        status |= int(self.Current_Leak_Detection_Instruction_Signal) << 3
        status |= int(self.Host_System_Life_Signal) << 7
        self.Status = status & 0xFF
        return self.Status
