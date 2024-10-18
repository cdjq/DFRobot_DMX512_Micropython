# -*- coding:utf-8 -*-
'''
    @file rtu.py
    @brief This is a simple example of using RTU.

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
from DFRobot_RTU import * 

rtu = DFRobot_RTU(9600,11)

def setup():
    pass
    
def loop():
    read_buf = rtu.read_input_register(0x72,0x05) #get RTU device data
    print(read_buf) 
    time.sleep(1)

def main():
    setup()
    while(True):
        loop()
    
if __name__ == "__main__":
    main()