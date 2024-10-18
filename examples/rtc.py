# -*- coding:utf-8 -*-
'''
    @file send_data.py
    @brief This is a routine for setting the RTC time and reading the RTC time.

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
    dmx512.begin() 
    dmx512.stop_clock() # stop RTC
    dmx512.set_rtc_time(24,10,14,4,10,30,30) # confing time
    dmx512.start_clock() # start RTC
    
def loop():
    time_data = dmx512.get_rtc_time() #get rtc time
    print("year:",time_data[6],
          "month:",time_data[5],
          "day:",time_data[4],
          "week:",time_data[3],
          "hour:",time_data[2],
          "minute:",time_data[1],
          "seconds:",time_data[0])
    time.sleep(1)

def main():
    setup()
    while(True):
        loop()
    
if __name__ == "__main__":
    main()