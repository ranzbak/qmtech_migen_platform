"""
Open Aars V3.0 daughter board platform file
"""

import qmtech100tcoreboard as coreboard
from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_aars_io = [
    ("board_leds",  0, Pins("T24 Y25 W21 AB24"), IOStandard("LVCMOS33")),

    # Video output pins to the ADV7511 HDMI transmitter
    ("adv_video_out", 0,
        Subsignal("de", Pins("D25"), IOStandard("LVCMOS33")),
        Subsignal("clk", Pins("G21"), IOStandard("LVCMOS33"), Misc("DRIVE 8")),

        Subsignal("r", Pins("C2 B2 A2 A3 A4 B4 A5 B5"), IOStandard("LVCMOS33")),
        Subsignal("g", Pins("J25 G20 F2 E1 C1 E5 D5 C4"), IOStandard("LVCMOS33")),
        Subsignal("b", Pins("E25 G26 E23 F23 F22 G22 J26"), IOStandard("LVCMOS33")),

        Subsignal("hsync", Pins("E26"), IOStandard("LVCMOS33")),
        Subsignal("vsync", Pins("D26"), IOStandard("LVCMOS33")),
     ),

    # Joystick interface via I2C MCP23S17 IO extender
    ("joystick_spi", 0,
        Subsignal("mosi", Pins("V21"), IOStandard("LVCMOS33")),
        Subsignal("miso", Pins("U21"), IOStandard("LVCMOS33")),
        Subsignal("cs", Pins("W23"), IOStandard("LVCMOS33")),
        Subsignal("sck", Pins("Y22"), IOStandard("LVCMOS33")),
        Subsignal("inta", Pins("V23"), IOStandard("LVCMOS33")),
    ),

    # PS2 keyboard
    ("ps2_keyboard", 0,
        Subsignal("clk", Pins("W25"), IOStandard("LVCMOS33")),
        Subsignal("dat", Pins("AC24"), IOStandard("LVCMOS33")),
    ),

    # PS Mouse
    ("ps_mouse", 0,
        Subsignal("clk", Pins("Y21"), IOStandard("LVCMOS33")),
        Subsignal("dat", Pins("AC24"), IOStandard("LVCMOS33")),
    ),

    # ESP32 SPI bus
    ("esp32", 0,
        Subsignal("mosi", Pins("D1"), IOStandard("LVCMOS33")),
        Subsignal("miso", Pins("B1"), IOStandard("LVCMOS33")),
        Subsignal("sck", Pins("D4"), IOStandard("LVCMOS33")),
        Subsignal("ss1", Pins("E2"), IOStandard("LVCMOS33")),
        Subsignal("ss2", Pins("G1"), IOStandard("LVCMOS33")),
    ),

    # Audio out I2S interface to MAX9850
    ("max_i2s", 0,
        Subsignal("clk", Pins("Y26"), IOStandard("LVCMOS33")),
        Subsignal("lrclk", Pins("AC26"), IOStandard("LVCMOS33")),
        Subsignal("data", Pins("AA25"), IOStandard("LVCMOS33")),
    ),

    # Open AARS on board SD ram
    ("sdram", 0,
        Subsignal("a", Pins(
            "K1  J1  M6 M5  T25 P25 P23 P24",
            "N21 N22 P3 M24 Y23")),
        Subsignal("dq", Pins(
            "J4  H4  H2  H1  H9  G5  M2  L2",
            "L22 L23 N26 M26 K22 K23 K25 K26")),
        Subsignal("we_n",  Pins("N3")),
        Subsignal("ras_n", Pins("K5")),
        Subsignal("cas_n", Pins("L5")),
        Subsignal("cs_n",  Pins("m4")),
        Subsignal("cke",   Pins("M25")),
        Subsignal("ba",    Pins("L4 R3")),
        Subsignal("dm",    Pins("N2 P26")),
        Misc("SLEW=FAST"),
        IOStandard("LVCMOS33"),
    ),

    # Floppy interface
    ("floppy", 0,
        Subsignal("mtron", Pins("R25")),
        Subsignal("sel0", Pins("T3")),
        Subsignal("dir", Pins("P5")),
        Subsignal("step", Pins("P6")),
        Subsignal("chng", Pins("M1")),
        Subsignal("index", Pins("N1")),
        Subsignal("rdy", Pins("P1")),
        Subsignal("dkrd", Pins("R1")),
        Subsignal("trk0", Pins("R2")),
        Subsignal("dkwdb", Pins("T2")),
        Subsignal("dkweb", Pins("U1")),
        Subsignal("side", Pins("U2")),
        IOStandard("LVCMOS33"),
    )
]

_io = coreboard._io + _aars_io

# Platform -----------------------------------------------------------------------------------------

class Platform(coreboard.Platform):
    def __init__(self):
        super().__init__()
