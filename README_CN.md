# DFRobot_DMX512
- [English Version](./README.md)

这是一个控制 EDGE 201-DMX512 设备库。

![](./resources/images/DFR0944.png)

## 产品链接(https://www.dfrobot.com.cn)

    SKU：DFR0944

## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性)
* [历史](#历史)
* [创作者](#创作者)

## 概述
  控制 EDGE 201-DMX512 设备库。

## 库安装

使用此库前，请首先下载库文件，将其粘贴到micropython设备的文件系统中，然后打开examples文件夹并在该文件夹中运行演示。

## 方法

```python
    def begin(self):
        '''
            @fn begin
            @brief 初始化 DMX512
        '''
    
    def led_light(self, addr, number, data):
        '''
            @fn led_light
            @brief 控制LED灯
            @param addr 灯的开始地址
            @param number 灯数量
            @param data 灯的亮度
            @return uint8_t 返回 1 正常，0 错误
        '''
    
    def rgb_light(self, addr, number, R, G, B):
        '''
            @fn rgb_light
            @brief 控制RGB灯
            @param addr 灯开始地址
            @param bumber 灯数量
            @param R 红色
            @param G 绿色
            @param B 蓝色
            @return uint8_t 返回 1 正常，0 错误
        '''
    
    def difital_in(self, pin):
        '''
            @fn difital_in
            @brief 获取数据
            @param pin 引脚
            @return value, 0 或 1
        '''
    
    def relay_out(self, value):
        '''
            @fn relayOUT
            @brief 继电器控制
            @param vale 0:关闭,1:打开
        '''
    
    def stop_clock(self):
        '''
            @fn stop_clock
            @brief 停止时钟
        '''
    
    def start_clock(self):
        '''
            @fn stop_clock
            @brief 开始时钟
        '''
     

    def set_rtc_time(self, year, month, day, week, hour, minute, seconds):
        '''
            @fn set_rtc_time
            @brief 设置RTC时间
            @param year 年
            @param month 月
            @param day 日 
            @param week 星期
            @param hour 小时
            @param minute 分钟
            @param seconds 秒
        '''

        
    def get_rtc_time(self):
        '''
            @fn get_rtc_time
            @brief 获取RTC时间
            @return 返回获取的RTC时间
        '''


    def write(self, addr, data):
        '''
            @fn write
            @brief dmx512 写数据
            @param addr 设备地址
            @param data 设备数据
        '''
 ``` 

## 兼容性

* Micropython Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| dmx512       |    √      |            |          |         |

## 历史

- 2024-10-18 - 1.0.0 版本

## 创作者

Written by TangJie(jie.tang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))





