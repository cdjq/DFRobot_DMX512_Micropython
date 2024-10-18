# -*- coding:utf-8 -*-
'''
    @file send_data.py
    @brief This is a library of routines for controlling DMX512 devices.

    @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
    @licence     The MIT License (MIT)
    @author [tangjie](jie.tnag@dfrobot.com)
    @version  V1.0
    @date  2024-10-18
    @https://github.com/DFRobot/DFRobot_DMX512
'''
import sys
import os
sys.path.append('../')
import time
from DFRobot_DMX512 import * 

dmx512 = DFRobot_DMX512()

def setup():
    dmx512.begin() # init DMX512
    dmx512.write(1, 255)
    dmx512.write(2, 255)
    dmx512.write(3, 100)
    dmx512.write(4, 100)
    dmx512.write(5, 0)
    dmx512.write(6, 0)
    dmx512.write(7, 0)
    dmx512.write(8, 0)
    dmx512.write(9, 0)

def loop():
    dmx512.relay_out(0) # close relay
    time.sleep(1)
    dmx512.relay_out(1) # open relay
    time.sleep(1)

def main():
    setup()
    while(True):
        loop()
    
if __name__ == "__main__":
    main()