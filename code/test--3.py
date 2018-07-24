# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:33:42 2018

@author: admin558
"""
a=b'1' #byte类型
print(a)
import urllib.request as r  #导入联网工具包，   打开网址，读取内容转换为str
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')

import json#字符串转字典的工具包
data=json.loads(data)

print('temp',data['main']['temp'])
print('descprition:',data['weather'][0]['description'])
print('pressure:',data['main']['pressure'])