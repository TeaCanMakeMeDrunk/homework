# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:05:34 2018
获得2300所学校编号
获取31所城市编号
@author: Administrator
"""

#1.获得2300所学校编号
ls=open('d:\\python\\lynn\\all_school.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
print("学校编号：",schoolls)

#2.获取31所城市
ls2=open("d:\\python\\lynn\\XML高考派城市.txt",encoding="gbk").readlines()
cityls=[]
for line in ls2:
    text=line.split(", ")
    if len(text)==2:
         print(text[1].split(")")[1][2:4],text[1].split(")")[0])
    
import urllib.request as r
f=open('d:\\python\\lynn\\全国招生计划表--四川.txt','a',encoding='gbk')#write
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36 QQBrowser',
        'X-Requested-With':'XMLHttpRequest'}
for schoolId in schoolls:
#    for city in range(50,53):
        for type in (1,2):
            req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(schoolId,type,51).encode(),headers=headers)
            try:
                data=r.urlopen(req).read().decode('utf-8','ignore')
                if '<!DOCTYPE html>' in data:
                    print('reject enter!')
                else:
                    data=r.urlopen(req).read().decode('utf-8','ignore')
                    f.write(data+'\n')
                    print('success')
            except Exception as err:
                print('have an error')
f.close()#关闭保存程序  




        
