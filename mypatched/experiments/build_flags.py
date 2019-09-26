#!/usr/bin/env python
from __future__ import print_function
import sys

#dynamic build flags for generic compile options
if __name__ == "__main__":
  args = " ".join([ "-std=gnu11",
                    "-Os",
                    "-mcpu=cortex-m3",
                    "-mthumb",

                    "-fsigned-char",
                    "-fno-move-loop-invariants",
                    "-fno-strict-aliasing",

                    "--specs=nano.specs",
                    "--specs=nosys.specs",

                    "-IMarlin/src/HAL/HAL_STM32F1",

                    "-MMD",
                    "-MP",
                    "-DTARGET_STM32F1"
                  ])

  for i in range(1, len(sys.argv)):
    args += " " + sys.argv[i]

  print(args)

# extra script for linker options
else:
  from SCons.Script import DefaultEnvironment
  env = DefaultEnvironment()
  env.Append(
      ARFLAGS=["rcs"],

      ASFLAGS=["-x", "assembler-with-cpp"],

      CXXFLAGS=[
          "-ffast-math",
          "-fabi-version=0",
          "-fno-use-cxa-atexit",
          "-fno-threadsave-statics"
      ],
      LINKFLAGS=[
        "-ffast-math",
          "-Os",
          "-mcpu=cortex-m3",
          "-ffreestanding",
          "-mthAmb",
          "--specs=nano.specs",
          "--specs=nosys.specs",
          "-u_printf_float",
      ],
  )
