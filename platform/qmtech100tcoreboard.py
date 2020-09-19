#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2018-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause
# Altered 2020 Paul Honig

from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform
from migen.build.xilinx.programmer import VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

# QMTECH XC7A100T DDR3
_io_100t_ddr3 = [
    ("user_led", 0,      Pins("J19"), IOStandard("LVCMOS33")),
    ("user_btn", 0,      Pins("H19"), IOStandard("LVCMOS33")),

    ("clk50", 0,         Pins("U22"), IOStandard("LVCMOS33")),


    # MT25QL128 SPI Flash,16M bytes
    ("spiflash4x", 0,  # clock needs to be accessed through STARTUPE2
     Subsignal("cs_n",   Pins("P18")),
     Subsignal("clk",    Pins("H13")),
     Subsignal("dq",     Pins("R14", "R15", "P14", "N14")),
     IOStandard("LVCMOS33")
    ),
    ("spiflash", 0,  # clock needs to be accessed through STARTUPE2
     Subsignal("cs_n",   Pins("P18")),
     Subsignal("clk",    Pins("H13")),
     Subsignal("mosi",   Pins("R14")),
     Subsignal("miso",   Pins("R15")),
     Subsignal("wp",     Pins("P14")),
     Subsignal("hold",   Pins("N14")),
     IOStandard("LVCMOS33")
    ),

    # MT41K128M16JT-125:K DDR3,256MB Micron
    ("ddram", 0,
     Subsignal("a",      Pins(
         "E17 G17 F16 F17 C17 G16 D16 H16 E16",
         "H14 F15 F20 H15 C18 G15"),
               IOStandard("SSTL135")),
     Subsignal("ba",     Pins("B17 D18 A17"), IOStandard("SSTL135")),
     Subsignal("ras_n",  Pins("A19"),         IOStandard("SSTL135")),
     Subsignal("cas_n",  Pins("B19"),         IOStandard("SSTL135")),
     Subsignal("we_n",   Pins("A18"),         IOStandard("SSTL135")),
     Subsignal("dm",     Pins("A22 C22"),     IOStandard("SSTL135")),
     Subsignal("dq",     Pins(
         "D21 C21 B22 B21 D19 E20 C19 D20",
         "C23 D23 B24 B25 C24 C26 A25 B26"),
               IOStandard("SSTL135")),
     Subsignal("dqs_p",  Pins("B20 A23"),     IOStandard("DIFF_SSTL135")),
     Subsignal("dqs_n",  Pins("A20 A24"),     IOStandard("DIFF_SSTL135")),
     Subsignal("clk_p",  Pins("F18"),         IOStandard("DIFF_SSTL135")),
     Subsignal("clk_n",  Pins("F19"),         IOStandard("DIFF_SSTL135")),
     Subsignal("cke",    Pins("E18"),         IOStandard("SSTL135")),
     Subsignal("odt",    Pins("G19"),         IOStandard("SSTL135")),
     # Subsignal("cs_n",   Pins(""),            IOStandard("SSTL135")),
     Subsignal("reset_n", Pins("H17"),        IOStandard("SSTL135"))
    ),
]

# QMTECH XC7A35T DDR3
_io_35t_ddr3 = [
    ("user_led", 0,      Pins("E6"), IOStandard("LVCMOS33")),
    ("user_btn", 0,      Pins("K5"), IOStandard("LVCMOS33")),

    ("clk50", 0,         Pins("N11"), IOStandard("LVCMOS33")),


    # MT25QL128 SPI Flash,16M bytes
    ("spiflash4x", 0,  # clock needs to be accessed through STARTUPE2
     Subsignal("cs_n",   Pins("L12")),
     Subsignal("clk",    Pins("E8")),
     Subsignal("dq",     Pins("J13", "J14", "K15", "K16")),
     IOStandard("LVCMOS33")
    ),
    ("spiflash", 0,  # clock needs to be accessed through STARTUPE2
     Subsignal("cs_n",   Pins("L12")),
     Subsignal("clk",    Pins("E8")),
     Subsignal("mosi",   Pins("J13")),
     Subsignal("miso",   Pins("J14")),
     Subsignal("wp",     Pins("K15")),
     Subsignal("hold",   Pins("K16")),
     IOStandard("LVCMOS33")
    ),

    # MT41K128M16JT-125:K DDR3,256MB Micron
    ("ddram", 0,
     Subsignal("a",      Pins(
         "B14 C8 A14 C14  C9 B10 D9 A12  D8 A13 B12 A9 A8 B11"),
               IOStandard("SSTL135")),
     Subsignal("ba",     Pins("C16 A15 B15"), IOStandard("SSTL135")),
     Subsignal("ras_n",  Pins("B16"),         IOStandard("SSTL135")),
     Subsignal("cas_n",  Pins("C11"),         IOStandard("SSTL135")),
     Subsignal("we_n",   Pins("C12"),         IOStandard("SSTL135")),
     Subsignal("dm",     Pins("F12 H11"),     IOStandard("SSTL135")),
     Subsignal("dq",     Pins(
         "F15 F13 E16 D11 E12 E13 D16 E11",
         "G12 J16 G16 J15 H14 H12 H16 H13",
         ""),
               IOStandard("SSTL135")),
     Subsignal("dqs_p",  Pins("D14 G14"),     IOStandard("DIFF_SSTL135")),
     Subsignal("dqs_n",  Pins("D15 F14"),     IOStandard("DIFF_SSTL135")),
     Subsignal("clk_p",  Pins("B9"),         IOStandard("DIFF_SSTL135")),
     Subsignal("clk_n",  Pins("A10"),         IOStandard("DIFF_SSTL135")),
     Subsignal("cke",    Pins("D13"),         IOStandard("SSTL135")),
     Subsignal("odt",    Pins("C13"),         IOStandard("SSTL135")),
     # Subsignal("cs_n",   Pins(""),            IOStandard("SSTL135")),
     Subsignal("reset_n", Pins("E15"),        IOStandard("SSTL135"))
    ),
]


# Connectors ---------------------------------------------------------------------------------------

# QMTECH XC7A100T DDR3
_connectors_100t_ddr3 = [

    # Breakout Connector U2
    # NC pins at the start are there to allign the pin numbers with the positions
    ("CON_U2", """NC NC NC NC NC NC NC
                A5 B5 A4 B4 A2 A3 C2 B2 D4 C4 D5 E5 B1 C1 D1 E1
                E2 F2 F4 G4 G1 G2 H4 J4 H1 H2 G5 H9 L2 M2 N3 N2
                K5 L5 L4 M4 P3 R3 J1 K1 M5 M6 T3 T4 P5 P6 M1 N1
                P1 R1 R2 T2 U1 U2
               """),
    # Breakout Connector U4
    # NC pins at the start are there to allign the pin numbers with the positions
    ("CON_U4", """NC NC NC NC NC NC NC
                D26 E26 D25 E25 G26 H26 E23 F23 F22 G22 J26 J25 G21 G20 H22 H21
                J21 K21 K26 K25 K23 K22 M26 N26 L23 L22 P26 R26 M25 M24 N22 N21
                P24 P23 P25 R25 T25 T24 V21 U21 W23 V23 Y23 Y22 AA25 Y25 Y21 W21
                AC24 AB24 Y26 W25 AC26 AB26
               """),

]

# QMTECH XC7A35T DDR3
_connectors_35t_ddr3 = [
    # Keeping to the 100T connector naming
    # U2 => U8, U4 => U7

    # U8 on the PCB
    ("CON_U2", """NC NC NC NC NC NC NC
                B7 A7 B6 B5 E6 K5 J5 J4 G5 G4 C7 C6 D6 D5 A5 A4
                B4 A3 D4 C4 C3 C2 B2 A2 C1 B1 E2 D1 E3 D3 F5 E5
                F2 E1 F4 F3 G2 G1 H2 H1 K1 J1 L3 L2 H5 H4 J3 H3
                K3 K2 L4 M4 N3 N2
               """),

    # U7 on the PCB
    ("CON_U4", """NC NC NC NC NC NC NC
                M12 N13 N14 N16 P15 P16 R15 R16 T14 T15 P13 P14 T13 R13 T12 R12
                L13 N12 K12 K13 P10 P11 N9 P9 T10 R11 T9 R10 T8 R8 T7 R7
                T5 R6 P6 R5 N6 M6 L5 P5 T4 T3 R3 T2 R2 R1 M5 N4
                P4 P3 N1 P1 M2 M1
               """),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    """
    Platform file for the "Xilinx FPGA Artix7 Artix-7 XC7A100T DDR3 Core Board"

    Hardware:

    On-Board FPGA: XC7A100T-2FGG676I;
    On-Board FPGA external crystal frequency: 50MHz;
    XC7A100T-2FGG676I has rich block RAM resource up to 4,860Kb;
    XC7A100T-2FGG676I has 101,440 logic cells;

    On-Board MT25QL128 SPI Flash,16M bytes for user configuration code;
    On-Board 256MB Micron DDR3，MT41K128M16JT-125:K;
    On-Board 3.3V power supply for FPGA by using MP2315 wide input range DC/DC;
    XC7A100T core board has two 64p, 2.54mm pitch headers for extending user IOs.
    XC7A100T core board has 1 user switch;
    XC7A100T core board has 1 reset switch;
    XC7A100T core board has 1 user LEDs;
    XC7A100T core board has JTAG interface, by using 6p, 2.54mm pitch header;
    XC7A100T core board PCB size is: 6.7cm x 8.4cm;
    Default power source for board is: 1A@5V DC, the DC header type: DC-050, 5.5mmx2.1mm;
    """
    default_clk_name   = "clk50"
    default_clk_period = 1e9/50e6

    def __init__(self, board_type: str):
        _connectors = []
        fpga_part = ""

        # Board types
        if board_type == "xc7a100t_ddr3":
            _io = _io_100t_ddr3
            _connectors = _connectors_100t_ddr3
            fpga_part = "xc7a100tfgg676"
        elif board_type == "xc7a35t_ddr3":
            _io = _io_35t_ddr3
            _connectors = _connectors_35t_ddr3
            fpga_part = "xc7a35tftg256-1"
        else:
            raise ValueError('Please select a valid board')


        XilinxPlatform.__init__(self, fpga_part, _io, _connectors, toolchain="vivado")
        self.toolchain.bitstream_commands = \
            ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
