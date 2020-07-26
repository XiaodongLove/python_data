import pandas as pd
import numpy as np
from pandas import Series,DataFrame
# matplotlib不引入，在调用的时候plot（）时候，不会报错，但是图片加载不出来
import matplotlib.pyplot as plt

#构造一个模拟序列
'''
size  0x  -  0x

    size   set   data 
0   0x      0     255
1   0x      1     355 
2   0x      2     999
3   
'''
memset_set =

#打开txt文件，然后解析memset
pid_memset = open("./pid.txt")
for line in pid_memset:
    line.strip()


pid_all = []
for line in pid_memset:
    #获取所有线程tid
    pid_all.append(line.split()[1])

#横坐标是分区，[1,2,4,8,16,32,64,128]
index = []
for i in range(16):
    index.append(2**i)
print(index)

#获取文件数据
data = []
f = open("./do_page_fault.txt")
for line in f:
    if line.split()[0].split('-')[3] in pid_all:
        data.append(line.split()[3:5])


#根据size统计address，和set的值


columns = ['address', 'set', 'size']
df = DataFrame(data, columns=columns)
#根据size列排序
df = df.sort_values(by=['size'], ascending=True)
#统计排序后的数据

#df['size'].value_counts()

groups=pd.cut(df['size'],bins=index)

#对df的size进行切割，然后赋值给生产
df['Categories'] = pd.cut(df['size'], bins=index)
#通过value_counts统计获得的数据
pd.value_counts()
#对统计到的数据，


df.plot()   #绘制折线图
df.plot(kind='bar')  #绘制直方图





