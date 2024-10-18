# DFRobot_DMX512
- [中文版](./README_CN.md)

This is a control EDGE 201-DMX512 device library.

![](./resources/images/DFR0944.png)

## Product link(https://www.dfrobot.com)

    SKU：DFR0944

## Catalogue

* [Overview](#Overview)
* [Installation](#Installation)
* [Methods](#Methods)
* [Compatibility](#Compatibility)
* [History](#History)
* [Credits](#Credits)

## Overview
  This is a control EDGE 201-DMX512 device library.

## Installation

Before using this library, first download the library file, paste it into the file system of your micropython device, then open the examples folder and run the demo in it.

## Methods

```python
    def begin(self):
        '''
            @fn begin
            @brief init DMX512
        '''
    
    def led_light(self, addr, number, data):
        '''
            @fn led_light
            @brief contor led lights
            @param addr Starting address of the lights
            @param number Number of lights
            @param data Brightness of the lights
            @return uint8_t Returns 0 if out of range, 1 if normal
        '''
    
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
    
    def difital_in(self, pin):
        '''
            @fn difital_in
            @brief get value
            @param pin pin
            @return value, 0 or 1
        '''
    
    def relay_out(self, value):
        '''
            @fn relayOUT
            @brief pilot relay
            @param vale 0:close,1:open
        '''
    
    def stop_clock(self):
        '''
            @fn stop_clock
            @brief Stop the clock
        '''
    
    def start_clock(self):
        '''
            @fn stop_clock
            @brief Start the clock
        '''
     

    def set_rtc_time(self, year, month, day, week, hour, minute, seconds):
        '''
            @fn set_rtc_time
            @brief set rtc time
            @param year year
            @param month month
            @param day day 
            @param week week
            @param hour hour
            @param minute minute
            @param seconds seconds
        '''

        
    def get_rtc_time(self):
        '''
            @fn get_rtc_time
            @brief get rtc time
            @return return get time
        '''


    def write(self, addr, data):
        '''
            @fn write
            @brief dmx512 write data
            @param addr device addr
            @param data device data
        '''
  
```

## Compatibility

* Micropython Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| dmx512       |    √      |            |          |         |

## History

- 2024-10-18 - Version 1.0.0 released.

## Credits

Written by TangJie(jie.tang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))





