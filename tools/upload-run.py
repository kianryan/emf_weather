#!/usr/bin/env python3

# Upload weather to tidal for testing.

import pyboard
pyb = pyboard.Pyboard('/dev/ttyS10', baudrate=115200)

pyb.fs_ls('/')
# pyb.fs_mkdir('/apps/weather')

