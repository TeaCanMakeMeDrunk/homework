# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:49:54 2018

1.打印每天18点的天气信息，温度，城市，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气描述，用户输入英文（数据里面有中英文）
3.打印温度折线图 a*wendu 
4.获取所有温度，并且排序 sorted([1,23])
5.友情提示，根据温度穿衣，打伞，出门
@author: admin558
"""
inputCity=input('please input your city:')
url='http://api.openweathermap.org/data/2.5/forecast?q='+inputCity+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

#####每天18点的天气信息，温度，城市，情况，气压，最高温度，最低温度
print('day one weather:')
print('temp is:',data['list'][2]['main']['temp'])
print('city is:',data['city']['name'])
print('weathe isr:',data['list'][2]['weather'][0]['main'])
print('pressure is:',data['list'][2]['main']['pressure'])
print('temp_max is:',data['list'][2]['main']['temp_max'])
print('temp_min is:',data['list'][2]['main']['temp_min'])
print('day two weather:')
print('temp is:',data['list'][10]['main']['temp'])
print('city is:',data['city']['name'])
print('weathe isr:',data['list'][10]['weather'][0]['main'])

print('pressure is:',data['list'][10]['main']['pressure'])
print('temp_max is:',data['list'][10]['main']['temp_max'])
print('temp_min is:',data['list'][10]['main']['temp_min'])
print('day three weather:')
print('temp is:',data['list'][18]['main']['temp'])
print('city is:',data['city']['name'])
print('weathe isr:',data['list'][18]['weather'][0]['main'])

print('pressure is:',data['list'][18]['main']['pressure'])
print('temp_max is:',data['list'][18]['main']['temp_max'])
print('temp_min is:',data['list'][18]['main']['temp_min'])
print('day four weather:')
print('temp is:',data['list'][26]['main']['temp'])
print('city is:',data['city']['name'])
print('weathe isr:',data['list'][26]['weather'][0]['main'])

print('pressure is:',data['list'][26]['main']['pressure'])
print('temp_max is:',data['list'][26]['main']['temp_max'])
print('temp_min is:',data['list'][26]['main']['temp_min'])
print('day five weather:')
print('temp is:',data['list'][34]['main']['temp'])
print('city is:',data['city']['name'])
print('weathe isr:',data['list'][34]['weather'][0]['main'])

print('pressure is:',data['list'][34]['main']['pressure'])
print('temp_max is:',data['list'][34]['main']['temp_max'])
print('temp_min is:',data['list'][34]['main']['temp_min'])

print('the temp chart：')
print('day one:','-'*int(data['list'][2]['main']['temp']))
print('day two:','-'*int(data['list'][10]['main']['temp']))
print('day three:','-'*int(data['list'][18]['main']['temp']))
print('day four:','-'*int(data['list'][26]['main']['temp']))
print('day five:','-'*int(data['list'][34]['main']['temp']))

print('the temp sort is：')
allTemp=[
        data['list'][2]['main']['temp'],
        data['list'][10]['main']['temp'],
        data['list'][18]['main']['temp'],
        data['list'][26]['main']['temp'],
        data['list'][34]['main']['temp']]
print(sorted(allTemp))

print("tips:")
a=[2,10,18,26,34]
for i in a:
    temp1=data['list'][i]['main']['temp']
    if temp1>30:
        print('温度：'+str(temp1)+'℃ 天气炎热,注意防晒')
    elif temp1<30 and temp1>20:
         print('温度：',str(temp1),'℃ 温度适宜,适合运动')
    else:
         print('温度：',str(temp1),'℃ 温度较低,适当加衣')


    



