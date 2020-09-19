#!/usr/bin/env python3
"""
Blink the LED of the QMTECH DDR3 CORE BOARD

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

import os
import argparse

from migen import *

# Custom platform file
import qmtech100tcoreboard as platform_mod
from openaars_30 import board_leds

class MyLedBlink(Module):
    def __init__(self, platform):

        self.led = led = platform.request("user_led")
        counter = Signal(26)

        # Get the board leds
        board_leds = Cat(*[platform.request("board_led", i) for i in range(4)])
        self.board_leds = board_leds

        # Counter logic
        self.sync += counter.eq(counter + 1)

        # Output the results via an LED
        self.comb += led.eq(counter[25])
        self.comb += board_leds.eq(Cat(*[counter[i] for i in range(24, 20, -1)]))


def main():
    # Handle command line imput
    parser = argparse.ArgumentParser(description="Qmtech xc7a100t DDR3 Open Aars logical analyzer")
    parser.add_argument("-b", "--build", action="store_true", help="Build bitstream")
    parser.add_argument("-l", "--load", action="store_true", help="Load bitstream")
    parser.add_argument("-p", "--platform",
                        type=str,
                        default="xc7a100t_ddr3",
                        choices=['xc7a35t_ddr3', 'xc7a100t_ddr3'],
                        help="Platform/Board type"
                       )
    args = parser.parse_args()

    # Setup the platform
    platform = platform_mod.Platform(args.platform)  # Instantiate QmTech core board
    platform.add_extension(board_leds)

    dut = MyLedBlink(platform)

    if args.build:
        platform.build(dut)

    if args.load:
        platform.create_programmer().load_bitstream("build/top.bit")


if __name__ == "__main__":
    main()
