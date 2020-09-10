#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2018-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause
# Altered 2020 Paul Honig

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer
#from litex.build.openocd import OpenOCD

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("user_led",  0, Pins("J19"), IOStandard("LVCMOS33")),

    ("user_btn", 0, Pins("H19"), IOStandard("LVCMOS33")),

    ("clk50", 0, Pins("U22"), IOStandard("LVCMOS33")),

    ("cpu_reset", 0, Pins("H19"), IOStandard("LVCMOS33")),

    ("ddram", 0,
        Subsignal("a", Pins(
            "E17 G17 F16 F17 C17 G16 D16 H16 E16",
            "H14 F15 F20 H15 C18 G15"),
            IOStandard("SSTL135")),
        Subsignal("ba",    Pins("B17 D18 A17"), IOStandard("SSTL135")),
        Subsignal("ras_n", Pins("A19"), IOStandard("SSTL135")),
        Subsignal("cas_n", Pins("B19"), IOStandard("SSTL135")),
        Subsignal("we_n", Pins("A18"),  IOStandard("SSTL135")),
        Subsignal("dm", Pins("A22 C22"), IOStandard("SSTL135")),
        Subsignal("dq", Pins(
            "D21 C21 B22 B21 D19 E20 C19 D20",
            "C23 D23 B24 B25 C24 C26 A25 B26"),
            IOStandard("SSTL135")),
        Subsignal("dqs_p", Pins("B20 A23"), IOStandard("DIFF_SSTL135")),
        Subsignal("dqs_n", Pins("A20 A24"), IOStandard("DIFF_SSTL135")),
        Subsignal("clk_p", Pins("F18"), IOStandard("DIFF_SSTL135")),
        Subsignal("clk_n", Pins("F19"), IOStandard("DIFF_SSTL135")),
        Subsignal("cke",   Pins("E18"), IOStandard("SSTL135")),
        Subsignal("odt",   Pins("G19"), IOStandard("SSTL135")),
        # Subsignal("cs_n", Pins(""), IOStandard("SSTL135")),
        Subsignal("reset_n", Pins("H17"), IOStandard("SSTL135"))
    ),

    # Breakout Connector U2
    ("con_u2", 0,
        Subsignal("U207", Pins("D26"), IOStandard("LVCMOS33")),
        Subsignal("U208", Pins("E26"), IOStandard("LVCMOS33")),
        Subsignal("U209", Pins("D25"), IOStandard("LVCMOS33")),
        Subsignal("U210", Pins("E25"), IOStandard("LVCMOS33")),
        Subsignal("U211", Pins("G26"), IOStandard("LVCMOS33")),
        Subsignal("U212", Pins("H26"), IOStandard("LVCMOS33")),
        Subsignal("U213", Pins("E23"), IOStandard("LVCMOS33")),
        Subsignal("U214", Pins("F23"), IOStandard("LVCMOS33")),
        Subsignal("U215", Pins("F22"), IOStandard("LVCMOS33")),
        Subsignal("U216", Pins("G22"), IOStandard("LVCMOS33")),
        Subsignal("U217", Pins("J26"), IOStandard("LVCMOS33")),
        Subsignal("U218", Pins("J25"), IOStandard("LVCMOS33")),
        Subsignal("U219", Pins("G21"), IOStandard("LVCMOS33")),
        Subsignal("U220", Pins("G20"), IOStandard("LVCMOS33")),
        Subsignal("U221", Pins("H22"), IOStandard("LVCMOS33")),
        Subsignal("U222", Pins("H21"), IOStandard("LVCMOS33")),
        Subsignal("U223", Pins("J21"), IOStandard("LVCMOS33")),
        Subsignal("U224", Pins("K21"), IOStandard("LVCMOS33")),
        Subsignal("U225", Pins("K26"), IOStandard("LVCMOS33")),
        Subsignal("U226", Pins("K25"), IOStandard("LVCMOS33")),
        Subsignal("U227", Pins("K23"), IOStandard("LVCMOS33")),
        Subsignal("U228", Pins("K22"), IOStandard("LVCMOS33")),
        Subsignal("U229", Pins("M26"), IOStandard("LVCMOS33")),
        Subsignal("U230", Pins("N26"), IOStandard("LVCMOS33")),
        Subsignal("U231", Pins("L23"), IOStandard("LVCMOS33")),
        Subsignal("U232", Pins("L22"), IOStandard("LVCMOS33")),
        Subsignal("U233", Pins("P26"), IOStandard("LVCMOS33")),
        Subsignal("U234", Pins("R26"), IOStandard("LVCMOS33")),
        Subsignal("U235", Pins("M25"), IOStandard("LVCMOS33")),
        Subsignal("U236", Pins("M24"), IOStandard("LVCMOS33")),
        Subsignal("U237", Pins("N22"), IOStandard("LVCMOS33")),
        Subsignal("U238", Pins("N21"), IOStandard("LVCMOS33")),
        Subsignal("U239", Pins("P24"), IOStandard("LVCMOS33")),
        Subsignal("U240", Pins("P23"), IOStandard("LVCMOS33")),
        Subsignal("U241", Pins("P25"), IOStandard("LVCMOS33")),
        Subsignal("U242", Pins("R25"), IOStandard("LVCMOS33")),
        Subsignal("U243", Pins("T25"), IOStandard("LVCMOS33")),
        Subsignal("U244", Pins("T24"), IOStandard("LVCMOS33")),
        Subsignal("U245", Pins("V21"), IOStandard("LVCMOS33")),
        Subsignal("U246", Pins("U21"), IOStandard("LVCMOS33")),
        Subsignal("U247", Pins("W23"), IOStandard("LVCMOS33")),
        Subsignal("U248", Pins("V23"), IOStandard("LVCMOS33")),
        Subsignal("U249", Pins("Y23"), IOStandard("LVCMOS33")),
        Subsignal("U250", Pins("Y22"), IOStandard("LVCMOS33")),
        Subsignal("U251", Pins("AA25"), IOStandard("LVCMOS33")),
        Subsignal("U252", Pins("Y25"), IOStandard("LVCMOS33")),
        Subsignal("U253", Pins("Y21"), IOStandard("LVCMOS33")),
        Subsignal("U254", Pins("W21"), IOStandard("LVCMOS33")),
        Subsignal("U255", Pins("AC24"), IOStandard("LVCMOS33")),
        Subsignal("U256", Pins("AB24"), IOStandard("LVCMOS33")),
        Subsignal("U257", Pins("Y26"), IOStandard("LVCMOS33")),
        Subsignal("U258", Pins("W25"), IOStandard("LVCMOS33")),
        Subsignal("U259", Pins("AC26"), IOStandard("LVCMOS33")),
        Subsignal("U260", Pins("AB26"), IOStandard("LVCMOS33")),
    ),

    # Breakout Connector U4
    ("con_u4", 0,
        Subsignal("U407", Pins("A5"), IOStandard("LVCMOS33")),
        Subsignal("U408", Pins("B5"), IOStandard("LVCMOS33")),
        Subsignal("U409", Pins("A4"), IOStandard("LVCMOS33")),
        Subsignal("U410", Pins("B4"), IOStandard("LVCMOS33")),
        Subsignal("U411", Pins("A2"), IOStandard("LVCMOS33")),
        Subsignal("U412", Pins("A3"), IOStandard("LVCMOS33")),
        Subsignal("U413", Pins("C2"), IOStandard("LVCMOS33")),
        Subsignal("U414", Pins("B2"), IOStandard("LVCMOS33")),
        Subsignal("U415", Pins("D4"), IOStandard("LVCMOS33")),
        Subsignal("U416", Pins("C4"), IOStandard("LVCMOS33")),
        Subsignal("U417", Pins("D5"), IOStandard("LVCMOS33")),
        Subsignal("U418", Pins("E5"), IOStandard("LVCMOS33")),
        Subsignal("U419", Pins("B1"), IOStandard("LVCMOS33")),
        Subsignal("U420", Pins("C1"), IOStandard("LVCMOS33")),
        Subsignal("U421", Pins("D1"), IOStandard("LVCMOS33")),
        Subsignal("U422", Pins("E1"), IOStandard("LVCMOS33")),
        Subsignal("U423", Pins("E2"), IOStandard("LVCMOS33")),
        Subsignal("U424", Pins("F2"), IOStandard("LVCMOS33")),
        Subsignal("U425", Pins("F4"), IOStandard("LVCMOS33")),
        Subsignal("U426", Pins("G4"), IOStandard("LVCMOS33")),
        Subsignal("U427", Pins("G1"), IOStandard("LVCMOS33")),
        Subsignal("U428", Pins("G2"), IOStandard("LVCMOS33")),
        Subsignal("U429", Pins("H4"), IOStandard("LVCMOS33")),
        Subsignal("U430", Pins("J4"), IOStandard("LVCMOS33")),
        Subsignal("U431", Pins("H1"), IOStandard("LVCMOS33")),
        Subsignal("U432", Pins("H2"), IOStandard("LVCMOS33")),
        Subsignal("U433", Pins("G5"), IOStandard("LVCMOS33")),
        Subsignal("U434", Pins("H9"), IOStandard("LVCMOS33")),
        Subsignal("U435", Pins("L2"), IOStandard("LVCMOS33")),
        Subsignal("U436", Pins("M2"), IOStandard("LVCMOS33")),
        Subsignal("U437", Pins("N3"), IOStandard("LVCMOS33")),
        Subsignal("U438", Pins("N2"), IOStandard("LVCMOS33")),
        Subsignal("U439", Pins("K5"), IOStandard("LVCMOS33")),
        Subsignal("U440", Pins("L5"), IOStandard("LVCMOS33")),
        Subsignal("U441", Pins("L4"), IOStandard("LVCMOS33")),
        Subsignal("U442", Pins("M4"), IOStandard("LVCMOS33")),
        Subsignal("U443", Pins("P3"), IOStandard("LVCMOS33")),
        Subsignal("U444", Pins("R3"), IOStandard("LVCMOS33")),
        Subsignal("U445", Pins("J1"), IOStandard("LVCMOS33")),
        Subsignal("U446", Pins("K1"), IOStandard("LVCMOS33")),
        Subsignal("U447", Pins("M5"), IOStandard("LVCMOS33")),
        Subsignal("U448", Pins("M6"), IOStandard("LVCMOS33")),
        Subsignal("U449", Pins("T3"), IOStandard("LVCMOS33")),
        Subsignal("U450", Pins("T4"), IOStandard("LVCMOS33")),
        Subsignal("U451", Pins("P5"), IOStandard("LVCMOS33")),
        Subsignal("U452", Pins("P6"), IOStandard("LVCMOS33")),
        Subsignal("U453", Pins("M1"), IOStandard("LVCMOS33")),
        Subsignal("U454", Pins("N1"), IOStandard("LVCMOS33")),
        Subsignal("U455", Pins("P1"), IOStandard("LVCMOS33")),
        Subsignal("U456", Pins("R1"), IOStandard("LVCMOS33")),
        Subsignal("U457", Pins("R2"), IOStandard("LVCMOS33")),
        Subsignal("U458", Pins("T2"), IOStandard("LVCMOS33")),
        Subsignal("U459", Pins("U1"), IOStandard("LVCMOS33")),
        Subsignal("U460", Pins("U2"), IOStandard("LVCMOS33")),
     ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk50"
    default_clk_period = 1e9/50e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100tfgg676-2", _io, toolchain="vivado")
        #self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")

    def create_programmer(self):
        #return OpenOCD("openocd_xc7_ft2232.cfg", "bscan_spi_xc7a100t.bit")
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk50", loose=True), 1e9/50e6)
