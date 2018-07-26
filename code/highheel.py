# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:12:54 2018
文件的保存：
    创建文件，文件名:喜欢的TV,保存的路径：当前目录，内容
    1.创建文件，文件名:喜欢的TV
    2.内容
    3.保存的路径
    4.设置文本格式
    5.保存到硬盘中
文件的打开：
    1.寻找路径
    2.打开文件
    3.读取内容
    4.关闭文件流
练习8：保存淘宝数据(小组项目)
1.每个组员爬取某个URL的100页数据 每个组员爬取的不同的城市，上海 北京 成都 郑州 组间城市不重复
2.保存淘宝商品信息(同练习题6)，并且保存为csv格式
3.每组组长合并各组员的数据  -后续班级合并数据

@author: Administrator
"""
######阅读文件会发生的问题，文字编码的问题，乱码？
f=open('d:\\python\\lynn\\淘宝数据--山东.csv','w',encoding='utf-8')#write
ls=f.readlines()   #将文本读取成列表
#s=f.read()     读取文本当中所有的字符
f.close()
###########################
'''
文件的保存：
    创建文件，文件名:喜欢的TV,保存的路径：当前目录，内容
    1.创建文件，文件名:喜欢的TV
    2.内容
    3.保存的路径
    4.设置文本格式
    5.保存到硬盘中
'''
import urllib.request as r#导入联网工具包，名为为r   a----append
#use 'gbk' can chinese
f=open('d:\\python\\lynn\\淘宝数据--高跟鞋.txt','a',encoding='utf-8')#write
cityList=['%E5%AE%89%E5%BE%BD','%E7%A6%8F%E5%BB%BA','%E7%94%98%E8%82%83','%E5%B9%BF%E4%B8%9C','%E5%B9%BF%E8%A5%BF','%E8%B4%B5%E5%B7%9E','%E6%B5%B7%E5%8D%97','%E6%B2%B3%E5%8C%97']
j=1
for page in range(1,101):   
    for city in cityList:
        url='https://s.taobao.com/search?q=%E9%AB%98%E8%B7%9F%E9%9E%8B&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc={}&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'.format(city,(page-1)*44)
#       print(url)
        try:
            data=r.urlopen(url).read().decode('utf-8','ignore')
            if '<!DOCTYPE html>' in data:
                print('reject enter!')
            else:
                f.write(data+'\n')
                print('第{}条数据success'.format(j))
                j+=1
        except Exception as err:
            print(err,'have an error')
f.close()


