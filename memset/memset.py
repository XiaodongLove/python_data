import pandas as pd
import numpy as np
from pandas import Series,DataFrame
# matplotlib不引入，在调用的时候plot（）时候，不会报错，但是图片加载不出来
import matplotlib.pyplot as plt

#打开txt文件，然后解析memset
pid_memset = open("./pid.txt")
for line in pid_memset:
    line.strip()



f = open("./do_page_fault.txt")
for line in f:

#横坐标是分区，[1,2,4,8,16,32,64,128]
index = []
for i in range(16):
    index.append(2**i)
print(index)



columns = ['address', 'set', 'size']
df = DataFrame(np.random.randint(0, 150, size=(15, 3)),
               columns=columns,
               index=index)
