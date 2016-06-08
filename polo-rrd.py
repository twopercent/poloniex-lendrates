#!/bin/env python3

import os
import rrdtool

if not os.path.isfile('polo-lend.rrd'):
    ret = rrdtool.create("polo-lend.rrd", "--step", "3600", "--start", '0',
     "DS:BTC:GAUGE:72000:0:U",
     "DS:MAID:GAUGE:7200:0:U",
     
     
