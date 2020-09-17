#!/usr/bin/env python3
"""
Blink the LED of the QMTECH DDR3 CORE BOARD
"""

import os
import argparse

from migen import *

from litex import *
from litex.soc.integration.builder import *

# Custom platform file
import qmtech100tcoreboard as platform_mod
from openaars_30 import board_leds

from litescope import LiteScopeAnalyzer

class MyLedBlink(Module):
    def __init__(self, platform):

        self.led = led = platform.request("user_led")
        counter = Signal(26)

        # Get the board leds
        board_leds = Cat(*[platform.request("board_led", i) for i in range(4)])
        self.board_leds = board_leds

        # Add 1 to the counter
        self.sync += counter.eq(counter + 1)

        # Output the results via an LED
        self.comb += led.eq(counter[25])
        self.comb += board_leds.eq(Cat(*[counter[i] for i in range(24, 20, -1)]))

        # Analyser
        # analyzer_signals = [
        #     counter
        # ]
        # self.submodules.analyzer = LiteScopeAnalyzer(analyzer_signals,
        #                                              depth=1024,
        #                                              clock_domain="sys_clk",
        #                                              csr_csv="analyzer.csv")
        # self.submodules += ["analyzer"]


def main():
    # Handle command line imput
    parser = argparse.ArgumentParser(description="Qmtech xc7a100t DDR3 Open Aars logical analyzer")
    #builder_args(parser)
    parser.add_argument("-b", "--build", action="store_true", help="Build bitstream")
    parser.add_argument("-l", "--load", action="store_true", help="Load bitstream")
    args = parser.parse_args()
    # if not args.build and not args.load:
    #     print("No build or load argument given assume build and load")
    #     args.build = True
    #     args.load = True

    # Setup the platform
    # platform = platform_mod.Platform("xc7a100t_ddr3")  # Instantiate QmTech core board
    platform = platform_mod.Platform("xc7a35t_ddr3")  # Instantiate QmTech core board
    platform.add_extension(board_leds)
    #platform.add_extension(openaars_30._aars_io)    # Add Open AARS peripherals

    dut = MyLedBlink(platform)

    if args.build:
        platform.build(dut)
        #builder = Builder(dut, **builder_argdict(args))
        #builder.build(run=args.build)

    if args.load:
        platform.create_programmer().load_bitstream("build/top.bit")


if __name__ == "__main__":
    main()
