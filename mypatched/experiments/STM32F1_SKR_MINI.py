from __future__ import print_function
import sys
Import("env")

# Relocate firmware from 0x08000000 to 0x08007000
for define in env['CPPDEFINES']:
    if define[0] == "VECT_TAB_ADDR":
        env['CPPDEFINES'].remove(define)
env['CPPDEFINES'].append(("VECT_TAB_ADDR", "0x08007000"))
env.Replace(LDSCRIPT_PATH="buildroot/share/PlatformIO/ldscripts/STM32F1_SKR_MINI.ld")

env.Append(
    ARFLAGS=["rcs"],

    ASFLAGS=["-x", "assembler-with-cpp"],

    CCFLAGS=[
        "-Wno-register",
        "-fabi-version=0",
        "-fno-use-cxa-atexit",
        "-fno-threadsafe-statics"
    ],
    LINKFLAGS=[
        "-Os",
        "-mcpu=cortex-m3",
        "-ffreestanding",
        "-mthumb",
        "--specs=nano.specs",
        "--specs=nosys.specs",
        "-u_printf_float",
    ],
)