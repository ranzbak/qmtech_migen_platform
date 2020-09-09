#!/usr/bin/env python3
"""
Blink the LED of the QMTECH DDR3 CORE BOARD
"""

from migen import *
from litex import *
#import qmtech100tcoreboard as platform_mod
import openaars_30 as platform_mod

class MyLedBlink(Module):
    def __init__(self, platform):
        self.led = led = platform.request("user_led")
        counter = Signal(26)

        self.con_u4 = con_u4 = platform.request("con_u4")
        self.con_u2 = con_u2 = platform.request("con_u2")
        self.boardLed = [0] * 4
        boardLed = Cat(con_u2.U244, con_u2.U252, con_u2.U254, con_u2.U256)
        # self.boardLed[0] = boardLed[0] = con_u4.U445
        # self.boardLed[1] = boardLed[1] = con_u4.U452
        # self.boardLed[2] = boardLed[2] = con_u4.U454
        # self.boardLed[3] = boardLed[3] = con_u4.U456

        self.sync += counter.eq(counter + 1)
        # self.sync += boardLed[1].eq(0)

        self.comb += led.eq(counter[25])
        self.comb += con_u2.U256.eq(counter[21])
        self.comb += con_u2.U254.eq(counter[22])
        self.comb += con_u2.U252.eq(counter[23])
        self.comb += con_u2.U244.eq(counter[24])

if __name__ == "__main__":
    platform = platform_mod.Platform()
    dut = MyLedBlink(platform)
    platform.build(dut)
    platform.create_programmer().load_bitstream("build/top.bit")
