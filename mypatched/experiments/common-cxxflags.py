#
# common-cxxflags.py
# Convenience script to apply customizations to CPP flags
#
from __future__ import print_function
import sys
Import("env")

#   env.Append(
#       ARFLAGS=["rcs"],

#       ASFLAGS=["-x", "assembler-with-cpp"],

#       CXXFLAGS=[
#           "-Wno-register",
#           "-fabi-version=0",
#           "-fno-use-cxa-atexit",
#           "-fno-threadsave-statics"
#       ],
#       LINKFLAGS=[
#           "-Os",
#           "-mcpu=cortex-m3",
#           "-ffreestanding",
#           "-mthumb",
#           "--specs=nano.specs",
#           "--specs=nosys.specs",
#           "-u_printf_float",
#       ],
#   )

env.Append(CCFLAGS=[
  "-Wno-register",
  "-ffast-mathy"
  #"-Wno-incompatible-pointer-types",
  #"-Wno-unused-const-variable",
  #"-Wno-maybe-uninitialized",
  #"-Wno-sign-compare"
])
