"""
Open Aars V3.0 daughter board platform file
"""

#import qmtech100tcoreboard as coreboard
from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# Use add_extension() to add the connectors to the platform
# The platform this connector file is attended for is: qmtech100tcoreboard.py

# IOs ----------------------------------------------------------------------------------------------

# LEDS on the daughter board
board_leds = [
    ("board_led", 0, Pins("CON_U4:44"), IOStandard("LVCMOS33")),
    ("board_led", 1, Pins("CON_U4:52"), IOStandard("LVCMOS33")),
    ("board_led", 2, Pins("CON_U4:54"), IOStandard("LVCMOS33")),
    ("board_led", 3, Pins("CON_U4:56"), IOStandard("LVCMOS33")),
]

spi = [
]

# PS2 keyboard & mouse
ps2 = [
    ("keyboard", 0,
        Subsignal("keyboard_clk", Pins("CON_U4:58")),
        Subsignal("keyboard_dat", Pins("CON_U4:55")),
        IOStandard("LVCMOS33"),
    ),
    ("mouse", 0,
        Subsignal("mouse_clk", Pins("CON_U4:53")),
        Subsignal("mouse_dat", Pins("CON_U4:55")),
        IOStandard("LVCMOS33"),
    )
]

# SPI Interfaces
spi = [
    # ESP32 SPI bus
    ("esp32", 0,
         Subsignal("esp32_mosi", Pins("CON_U2:21")),
         Subsignal("esp32_miso", Pins("CON_U2:19")),
         Subsignal("esp32_sck",  Pins("CON_U2:15")),
         Subsignal("esp32_ss1",  Pins("CON_U2:23")),
         Subsignal("esp32_ss2",  Pins("CON_U2:27")),
         IOStandard("LVCMOS33"),
    ),
    # Joystick interface via I2C MCP23S17 IO extender
    ("controllers", 0,
         Subsignal("ctrl_mosi", Pins("CON_U4:45")),
         Subsignal("ctrl_miso", Pins("CON_U4:46")),
         Subsignal("ctrl_cs",   Pins("CON_U4:47")),
         Subsignal("ctrl_sck",  Pins("CON_U4:50")),
         Subsignal("ctrl_inta", Pins("CON_U4:48")),
         IOStandard("LVCMOS33"),
    )
]

# Audio out I2S interface to MAX9850
aars_i2s = [
    ("max9850", 0,
        Subsignal("i2s_clk",   Pins("CON_U4:57")),
        Subsignal("i2s_lrclk", Pins("CON_U4:59")),
        Subsignal("i2s_data",  Pins("CON_U4:51")),
        IOStandard("LVCMOS33"),
    )
]

# Video output pins to the ADV7511 HDMI transmitter
aars_video = [
    ("adv7511", 0,
         Subsignal("de",    Pins("CON_U4:09")),
         Subsignal("clk",   Pins("CON_U4:19"), Misc("DRIVE 8")), # Lower drive prevents display stripes

         Subsignal("r",     Pins("CON_U2:13 CON_U2:14 CON_U2:11 CON_U2:12 CON_U2:9  CON_U2:10 CON_U2:5  CON_U2:8")),
         Subsignal("g",     Pins("CON_U4:18 CON_U4:20 CON_U2:24 CON_U2:22 CON_U2:20 CON_U2:18 CON_U2:17 CON_U2:16")),
         Subsignal("b",     Pins("CON_U4:10 CON_U4:11 CON_U4:12 CON_U4:13 CON_U4:14 CON_U4:15 CON_U4:16 CON_U4:17")),

         Subsignal("hsync", Pins("CON_U4:8")),
         Subsignal("vsync", Pins("CON_U4:7")),
         IOStandard("LVCMOS33"),
    )
]

aars_sdram = [
    # Open AARS on board SD ram
    ("sdram", 0,
         Subsignal("a", Pins(
             "CON_U2:46 CON_U2:45 CON_U2:48 CON_U2:47 CON_U4:43 CON_U4:41 CON_U4:40 ",
             "CON_U4:39 CON_U4:38 CON_U4:37 CON_U2:43 CON_U4:36 CON_U4:49")),
         Subsignal("dq", Pins(
             "CON_U2:30 CON_U2:29 CON_U2:32 CON_U2:31 CON_U2:34 CON_U2:33 CON_U2:36 CON_U2:35",
             "CON_U4:32 CON_U4:31 CON_U4:30 CON_U4:29 CON_U4:28 CON_U4:27 CON_U4:26 CON_U4:25")),
         Subsignal("we_n",  Pins("CON_U2:37")),
         Subsignal("ras_n", Pins("CON_U2:39")),
         Subsignal("cas_n", Pins("CON_U2:40")),
         Subsignal("cs_n",  Pins("CON_U2:42")),
         Subsignal("cke",   Pins("CON_U4:35")),
         Subsignal("ba",    Pins("CON_U2:41 CON_U2:44")),
         Subsignal("dm",    Pins("CON_U2:38 CON_U4:33")),
         Misc("SLEW=FAST"),
         IOStandard("LVCMOS33"),
    ),
]

aars_floppy = [
    # Floppy interface
    ("floppy", 0,
         Subsignal("mtron", Pins("CON_U4:42")),
         Subsignal("sel0",  Pins("CON_U2:49")),
         Subsignal("dir",   Pins("CON_U2:51")),
         Subsignal("step",  Pins("CON_U2:52")),
         Subsignal("chng",  Pins("CON_U2:53")),
         Subsignal("index", Pins("CON_U2:54")),
         Subsignal("rdy",   Pins("CON_U2:55")),
         Subsignal("dkrd",  Pins("CON_U2:56")),
         Subsignal("trk0",  Pins("CON_U2:57")),
         Subsignal("dkwdb", Pins("CON_U2:58")),
         Subsignal("dkweb", Pins("CON_U2:59")),
         Subsignal("side",  Pins("CON_U2:60")),
         IOStandard("LVCMOS33"),
    ),
]
