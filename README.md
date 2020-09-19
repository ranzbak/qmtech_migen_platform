# QMTech Migen Platform files

[Migen](https://github.com/m-labs/migen) is a Python based high level language
to make writing and integrating HDL projects easier and quicker.
Migen supports a lot of
[Platforms](https://github.com/m-labs/migen/tree/master/migen/build/platforms) already,
but the budget QMTech booards are missing (2020-09).
So for me to start playing with Migen I had to write my own Platform files,
and since this is work that might save others from having to do the same,
I'm sharing the platform files.
Information about the QMtech boards can be found at the [company website](http://http://www.chinaqmtech.com/).

### Boards supported

|Board|type|test_script|description|
|---|---|---|---|
|QM_XC7A35T_DDR3|core board|XC7A35T-1FTG256C, 256Mb DDR3|
|QM_XC7A100T_DDR3|core board|XC7A100T-2FGG676I, 256Mb DDR3|
|QM_ARTIX7_XC7A35T DB|daughter board|qm_db_test.py|RTL8211EG ethernet, 16-VGA, 5 user leds, 5 user keys, 7-SEG LEDS, 2xPMOD, SDCARD|
|[Open AARS](https://github.com/ranzbak/qmtech_minimig)|daughter board|aars_test.py|ADV7511 HDMI, ESP32 + SDCARD, 2x Joystick, PS/2 2x, Max9850 I2S audio output, 32Mb SDRAM|

### Migen

In order to use the platform files, Migen needs to be installed.
Information on how to setup Migen can be found [here](https://m-labs.hk/migen/manual/introduction.html#installing-migen)

### Improvements

I created this file mostly to develop my Minimig project,
so I'm not going to test all the hardware peripherals.
When you find a bugs/mistakes in the platform files,
please create a bug in Github bug report.
