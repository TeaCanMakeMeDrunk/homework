# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:02:28 2018

练习题5：
1.优化代码 用函数的方式修改练习4 输出每一天的天气
2.打印温度折线图，是用函数来优化（必须要有返回值）

函数的参数 ctrl+i
@author: admin558
"""
inputCity=input('please input your city:')
url='http://api.openweathermap.org/data/2.5/forecast?q='+inputCity+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

a=[2,10,18,26,34]
def printWeather(day,i):
    print('weather in the time 18:00 of the day',day,'is:')
    print('temp is:',data['list'][i]['main']['temp'])
    print('weathe is:',data['list'][i]['weather'][0]['main'])
    print('pressure is:',data['list'][i]['main']['pressure'])
    print('temp_max is:',data['list'][i]['main']['temp_max'])
    print('temp_min is:',data['list'][i]['main']['temp_min'])
    print('----------------------------------------------------')

printWeather(1,2)#day one
printWeather(2,10)#day two
printWeather(3,18)#day three
printWeather(4,26)#day four
printWeather(5,34)#day five

print('the temp chart：')
def printChart(i):
    return '-'*int(data['list'][i]['main']['temp'])
print('day one:',printChart(2))
print('day two:',printChart(10))
print('day three:',printChart(18))
print('day four:',printChart(26))
print('day five:',printChart(34))

# encoding=utf-8
import matplotlib.pyplot as plt

names = ['1', '2', '3', '4', '5']
x = range(len(names))
y = []
a=[2,10,18,26,34]
for i in a:
    y.append(data['list'][i]['main']['temp'])
print(y)
plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'temp change')
plt.legend()  # 让图例生效

plt.xlabel("未来五天") #X轴标签
plt.ylabel("温度变化") #Y轴标签
plt.title("temp chart") #标题

plt.show()