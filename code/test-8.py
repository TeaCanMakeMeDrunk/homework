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
f=open('d:\\python\\lynn\\淘宝数据--山东.csv','a',encoding='gbk')#write
for page in range(1,37):   
    url='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E8%A3%99%E5%AD%90&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E5%B1%B1%E4%B8%9C&s='+str((page-1)*44)+'&ajax=true'
    print(url)
    try:
        data=r.urlopen(url).read().decode('utf-8','ignore')       
        f.write(data+'\n')
        print('success')
    except Exception as err:
        print('have an error')
f.close() 






