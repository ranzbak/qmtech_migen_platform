"""
Open Aars V3.0 daughter board platform file
QM_ARTIX7_XC7A35T DB

Copyright (C) 2020 by Paul Honig paul<at>etv.cx

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform

# Use add_extension() to add the connectors to the platform
# The platform this connector file is attended for is: qmtech100tcoreboard.py

# Extensions ---------------------------------------------------------------------------------------

# Input buttons
buttons = [
    ("user_btn", 1, Pins("CON_U2:7"), IOStandard("LVCMOS33")),
    ("user_btn", 2, Pins("CON_U4:44"), IOStandard("LVCMOS33")),
    ("user_btn", 3, Pins("CON_U4:43"), IOStandard("LVCMOS33")),
    ("user_btn", 4, Pins("CON_U4:42"), IOStandard("LVCMOS33")),
    ("user_btn", 5, Pins("CON_U4:41"), IOStandard("LVCMOS33")),
]

# Line of Red LEDs
user_leds = [
    ("user_led", 1, Pins("CON_U4:40"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("CON_U4:39"), IOStandard("LVCMOS33")),
    ("user_led", 3, Pins("CON_U4:38"), IOStandard("LVCMOS33")),
    ("user_led", 4, Pins("CON_U4:37"), IOStandard("LVCMOS33")),
    ("user_led", 5, Pins("CON_U4:36"), IOStandard("LVCMOS33")),
]

# 7 Segment display
# Segments in the "gfedcba" order
d7seg = [
    ("dig", 0,
        # 3 digits
        Subsignal("dig", Pins("CON_U4:33 CON_U4:27 CON_U4:35")),
        # 7 Segments + Dot
        Subsignal("seg", Pins("CON_U4:31 CON_U4:26 CON_U4:28 CON_U4:32 CON_U4:34 CON_U4:29 CON_U4:25 CON_U4:30")),
        IOStandard("LVCMOS33"),
     )
]

# PMOD headers
pmod = [
    ("J10", 0,
        Pins("CON_U4:17 CON_U4:19 CON_U4:21 CON_U4:23 CON_U4:18 CON_U4:20 CON_U4:22 CON_U4:24"),
        IOStandard("LVCMOS33"),
    ),
    ("j11", 0,
        Pins("CON_U4:07 CON_U4:09 CON_U4:11 CON_U4:13 CON_U4:08 CON_U4:10 CON_U4:12 CON_U4:14"),
        IOStandard("LVCMOS33"),
    )
]

# CMOS/CCD camera interface
HDR_9x2 = [
    ("JP1", 0,
        Pins("CON_U4:60 CON_U4:59 CON_U4:58 CON_U4:57 CON_U4:56 CON_U4:55 CON_U4:54 CON_U4:53 CON_U4:52 CON_U4:51 CON_U4:50 CON_U4:49 CON_U4:48 CON_U4:47 CON_U4:46 CON_U4:45"),
        IOStandard("LVCMOS33")
    )
]

# SDCARD interface, no SPI atm
sdcard = [
    ("sdcard", 0,
        Subsignal("clk",  Pins("CON_U2:11")),
        Subsignal("cmd",  Pins("CON_U2:12"), Misc("PULLMODE=UP")),
        Subsignal("data", Pins("CON_U2:10 CON_U2:9 CON_U2:14 CON_U2:13"), Misc("PULLMODE=UP")),
        Misc("SLEWRATE=FAST"),
        IOStandard("LVCMOS33"),
    ),
]

# Ethernet interface to RTL8211EG-VB chip
# Supports 10/100/1000Mb 
# MII interface
eth = [
    #("eth_ref_clk", 0, Pins("G18"), IOStandard("LVCMOS33")),
    ("eth_clocks", 0,
        Subsignal("tx", Pins("CON_U2:22")),
        Subsignal("rx", Pins("CON_U2:37")),
        IOStandard("LVCMOS33"),
    ),
    ("eth", 0,
        Subsignal("rst_n",   Pins("CON_U2:26")),
        Subsignal("mdio",    Pins("CON_U2:15")),
        Subsignal("mdc",     Pins("CON_U2:16")),
        Subsignal("rx_dv",   Pins("CON_U2:42")),
        Subsignal("rx_er",   Pins("CON_U2:32")),
        Subsignal("rx_data", Pins("CON_U2:41 CON_U2:40 CON_U2:39 CON_U2:38 CON_U2:25 CON_U2:35 CON_U2:34 CON_U2:33")),
        Subsignal("tx_en",   Pins("CON_U2:28")),
        Subsignal("tx_data", Pins("CON_U2:27 CON_U2:25 CON_U2:24 CON_U2:23 CON_U2:21 CON_U2:20 CON_U2:19 CON_U2:18")),
        Subsignal("col",     Pins("CON_U2:31")),
        Subsignal("crs",     Pins("CON_U2:30")),
        IOStandard("LVCMOS33"),
    ),
]

# 16-bit VGA Output
vga = [
    ("vga", 0,
        Subsignal("hsync_n", Pins("CON_U2:44")),
        Subsignal("vsync_n", Pins("CON_U2:43")),
        Subsignal("r", Pins("CON_U2:60 CON_U2:58 CON_U2:59 CON_U2:56 CON_U2:57")),
        Subsignal("g", Pins("CON_U2:55 CON_U2:54 CON_U2:52 CON_U2:53 CON_U2:50 CON_U2:51")),
        Subsignal("b", Pins("CON_U2:49 CON_U2:47 CON_U2:48 CON_U2:45 CON_U2:46")),
        IOStandard("3.3-V LVTTL")
    ),
]
