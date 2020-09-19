#!/usr/bin/env python3
"""
Blink the LED of the QMTECH DDR3 CORE BOARD

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

import os
import sys
import argparse

from migen import *

import qmtech100tcoreboard as platform_mod
from qmtech_db_fpga_xc7a35T_ddr3 import user_leds, d7seg


class Decode7Seg(Module):
    def __init__(self):
        self.numin = numin = Signal(4)
        self.output = output = Signal(8)

        #decode number to figures
        self.sync += [
            Case(numin, {
                0x0: output.eq(~0x3F),
                0x1: output.eq(~0x06),
                0x2: output.eq(~0x5B),
                0x3: output.eq(~0x4F),
                0x4: output.eq(~0x66),
                0x5: output.eq(~0x6D),
                0x6: output.eq(~0x7D),
                0x7: output.eq(~0x07),
                0x8: output.eq(~0x7F),
                0x9: output.eq(~0x6F),
                0xA: output.eq(~0x77),
                0xB: output.eq(~0x7C),
                0xC: output.eq(~0x39),
                0xD: output.eq(~0x5E),
                0xE: output.eq(~0x79),
                0xF: output.eq(~0x71),
            })
        ]


class MyLedBlink(Module):

    def __init__(self, platform):
        decode7seg = Decode7Seg()
        self.submodules += decode7seg

        self.led = led = platform.request("user_led")
        counter = Signal(35)

        # Get the board leds
        user_leds = Cat(*[platform.request("user_led", i) for i in range(1, 6)])
        self.user_leds = user_leds

        # Counter logic
        self.sync += counter.eq(counter + 1)

        # Output the results via an LED
        self.comb += led.eq(counter[26])
        self.comb += user_leds.eq(Cat(*[counter[i] for i in range(25, 20, -1)]))

        self.dig = dig = platform.request("dig")

        number_out = Signal()

        # Assign numbers to 7-segment display
        self.sync += [
            Case(counter[18:20], {
                0x0: (decode7seg.numin.eq(counter[23:27]),
                      dig.dig.eq(0x4)),
                0x1: (decode7seg.numin.eq(counter[27:31]),
                      dig.dig.eq(0x2)),
                0x2: (decode7seg.numin.eq(counter[31:35]),
                      dig.dig.eq(0x1)),
            }),
            self.dig.seg.eq(decode7seg.output),
        ]

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
    platform.add_extension(user_leds)
    platform.add_extension(d7seg)

    dut = MyLedBlink(platform)

    if args.build:
        platform.build(dut)

    if args.load:
        platform.create_programmer().load_bitstream("build/top.bit")


if __name__ == "__main__":
    main()
