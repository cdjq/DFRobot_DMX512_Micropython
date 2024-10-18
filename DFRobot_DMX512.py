# -*- coding:utf-8 -*-
'''
@file DFRobot_DMX512.py
@brief Contor EDGE 201-DMX512 device library

@copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
@licence     The MIT License (MIT)
@author [tangjie](jie.tang@dfrobot.com)
@version  V1.0
@date  2024-10-12
@https://github.com/DFRobot/DFRobot_DMX512

'''

from machine import I2C, Pin
import time

dmx512_device_addr = 0x2E
rtc_device_addr = 0x51


PIN_DI1 = 7
PIN_DI2 = 10
PIN_DI3 = 18
PIN_DI4 = 35
PIN_DI5 = 36
PIN_DI6 = 37
PIN_DI7 = 38
PIN_DI8 = 39
CONTROLSTATUS1  =  0X00
VLSECONDS         =  0X02
MINUTES           =  0X03
HOURS             =  0X04
DAYS              =  0X05
WEEK              =  0X06
CENTURYMONTHS     =  0X07
YEARS             =  0X08

eJan = 1
eFeb = 2
eMar = 3
eApr = 4
eMay = 5
eJun = 6
eJul = 7
eAug = 8
eSep = 9
eOct = 10
eNov = 11
eDec = 12

class DFRobot_DMX512(object):

    def __init__(self):
        '''
            @brief init I2C
        '''
        self.i2c = I2C(0, scl = Pin(2), sda = Pin(1), freq = 100000)
        
        
    def begin(self):
        '''
            @fn begin
            @brief init DMX512
        '''
        self.send_buf = bytearray(515)
        self.send_buf[0] = 0x55
        for i in range(514):
            self.send_buf[i+1] = 0
        self.i2c.writeto(dmx512_device_addr, self.send_buf)
        time.sleep(1)
        self.read_buf = self.i2c.readfrom_mem(rtc_device_addr, 0, 1)
    
    def led_light(self, addr, number, data):
        '''
            @fn led_light
            @brief contor led lights
            @param addr Starting address of the lights
            @param number Number of lights
            @param data Brightness of the lights
            @return uint8_t Returns 0 if out of range, 1 if normal
        '''
        self._addr = addr
        if(self._addr + number > 512):
            return 0
        for i in range(number):
            self.write(self._addr,data)
            self._addr += 1
        return 1
    
    def rgb_light(self, addr, number, R, G, B):
        '''
            @fn rgb_light
            @brief control RGB lights
            @param addr Statring address of the lights
            @param bumber Number of light strips
            @param R Red color
            @param G Green color
            @param B Blue color
            @return uint8_t Returns 0 if out of range, 1 if normal
        '''
        self._addr = addr
        self.i = 0
        if(self._addr + number > 512):
            return 0
        while(self.i < number):
            self.write(self._addr,R)
            self.write(self._addr + 1,G)
            self.write(self._addr + 2,B)
            self.i +=3
            self._addr += 3
        return 1
    
    def difital_in(self, pin):
        '''
            @fn difital_in
            @brief get value
            @param pin pin
            @return value, 0 or 1
        '''
        pin = Pin(pin, Pin.IN)
        return pin.value()
    
    def relay_out(self, value):
        '''
            @fn relayOUT
            @brief pilot relay
            @param vale 0:close,1:open
        '''
        relay = Pin(46, Pin.OUT)
        relay.value(value)
    
    def stop_clock(self):
        '''
            @fn stop_clock
            @brief Stop the clock
        '''
        self.send_buf = bytearray(2)
        self.send_buf[0] = CONTROLSTATUS1
        self.send_buf[1] = (1 << 5)
        self.i2c.writeto(rtc_device_addr, self.send_buf)

    def start_clock(self):
        '''
            @fn stop_clock
            @brief Start the clock
        '''
        self.send_buf = bytearray(2)
        self.send_buf[0] = CONTROLSTATUS1
        self.send_buf[1] = 0
        self.i2c.writeto(rtc_device_addr, self.send_buf)

    def set_rtc_time(self, year, month, day, week, hour, minute, seconds):
        '''
            @fn set_rtc_time
            @brief set rtc time
            @param year year
            @param month month
            @param day day 
            @param week
            @param hour hour
            @param minute minute
            @param seconds seconds
        '''
        self._day = day
        self.send_buf = bytearray(8)
        if(month == 2):
            if(year % 4):
                if(self._day > 28):
                    self._day = 28
            else:
                if(self._day > 29):
                    self._day = 29
        self.send_buf[0] = VLSECONDS
        self.send_buf[1] = (self._get_secon_number(seconds) << 4) | self._get_first_number(seconds)
        self.send_buf[2] = (self._get_secon_number(minute) << 4) | self._get_first_number(minute)
        self.send_buf[3] = (self._get_secon_number(hour) << 4) | self._get_first_number(hour)
        self.send_buf[4] = (self._get_secon_number(self._day) << 4) | self._get_first_number(self._day)
        self.send_buf[5] = (self._get_secon_number(week) << 4) | self._get_first_number(week)
        self.send_buf[6] = (self._get_secon_number(month) << 4) | self._get_first_number(month)
        self.send_buf[7] = (self._get_secon_number(year) << 4) | self._get_first_number(year)

        self.i2c.writeto(rtc_device_addr, self.send_buf)
        time.sleep(0.1)

        
    def get_rtc_time(self):
        '''
            @fn get_rtc_time
            @brief get rtc time
            @return return get time
        '''
        my_list = [0, 0, 0, 0, 0, 0, 0]
        self.read_buf = self.i2c.readfrom_mem(rtc_device_addr, VLSECONDS, 7)
        my_list[0] = self._bcd_to_number((self.read_buf[0] & 0b01110000) >> 4, (self.read_buf[0] & 0b00001111)) #seconds
        my_list[1] = self._bcd_to_number((self.read_buf[1] & 0b01110000) >> 4, (self.read_buf[1] & 0b00001111)) #minute
        my_list[2] = self._bcd_to_number((self.read_buf[2] & 0b00110000) >> 4, (self.read_buf[2] & 0b00001111)) #hour
        my_list[3] = self._bcd_to_number(0, (self.read_buf[4] & 0b00000111)) #week
        my_list[4] = self._bcd_to_number((self.read_buf[3] & 0b00110000) >> 4, (self.read_buf[3] & 0b00001111)) #day
        my_list[5] = self._bcd_to_number((self.read_buf[5] & 0b00010000) >> 4, (self.read_buf[5] & 0b00001111)) #month
        my_list[6] = self._bcd_to_number((self.read_buf[6] & 0b11110000) >> 4, (self.read_buf[6] & 0b00001111)) #year

        return my_list


    def write(self, addr, data):
        '''
            @fn write
            @brief dmx512 write data
            @param addr device addr
            @param data device data
        '''
        self.send_buf = bytearray(4)
        self.send_buf[0] = 0x55
        self.send_buf[1] = addr & 0xff
        self.send_buf[2] = addr >> 8 & 0xff
        self.send_buf[3] = data
        self.i2c.writeto(dmx512_device_addr, self.send_buf)

    def _get_secon_number(self, number):
        output = number / 10
        return int(output)

    def _get_first_number(self, number):
        output = number % 10
        return int(output)
    
    def _bcd_to_number(self, first, second):
        output = first * 10  + second
        return int(output)
        

    