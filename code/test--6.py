# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:36:39 2018
练习6：
1.显示4个商品然后打印分割线，只要第一个36个商品信息
2.列出36个商品
3.获取所有的商品价格并且给商品排序，从高到底
4.按照销量排序
5.商品过滤，只要15天退款或者包邮的商品信息，显示
@author: admin558
"""

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&s=0&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

length=len(data['mods']['itemlist']['data']['auctions'])

#打印36个商品信息，每四个打印一个分割线
def printMods():
    b=0
    for i in range(length):
        print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
        print(data['mods']['itemlist']['data']['auctions'][i]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i]['nick'])
        print(data['mods']['itemlist']['data']['auctions'][i]['item_loc'])
        b+=1
        if b%4==0:
            print('----------------------------------------------------------')

#调用方法
printMods()

#获取所有的商品并且给商品排序，从高到底
def sortAll(value,name):
    priceList=[]
    for i in range(length):
        if(name == '商品销量'):   
            priceList.append(int(data['mods']['itemlist']['data']['auctions'][i][value][0:-3]))
        else:
            priceList.append(float(data['mods']['itemlist']['data']['auctions'][i][value]))
    print(name+'排序,从高到底：')
    sortList=sorted(priceList)
    print(list(reversed(sortList)))

#调用方法
sortAll('view_price','商品价格')
sortAll('view_sales','商品销量')
print('-----------------------------------------------------------------------------------')
#商品过滤，只要15天退款或者包邮的商品信息，显示
print('商品信息:')
for i in range(15):
    price=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    if price>80 and price<498:
        print('商品价格大于100')
    elif price<60 and price>40:
         continue
         print('商品价格在40到60之间')
    else:
        while price==499.0:
            print('最大商品价格是499.0')
            break






