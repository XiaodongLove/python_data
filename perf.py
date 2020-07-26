import csv
import numpy
import matplotlib
import xlwt
import xlrd
from xlutils.copy import copy


def get_dso_name(path):
    dso_name = []
    dso = open(path)
    for line in dso:
        if line[0] != '#':
            dso_name.append(line.split( ))
    return dso_name

#获取了需要统计的列表

#初始化列表



#统计函数占比
#按照最上一级libc统计
#path: 写入数据路径
#sheet_name 表格的名字
#value 写入的值

def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    index = 1
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

def write_excel_xls_new(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    index = 1
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    sheet = new_workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheet_name)  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(worksheet.name)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")

def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()


'''
firefox  8256 124136.622540:     250000 cpu-clock:
	    7fff810b2a28 finish_task_switch ([kernel.kallsyms])
	    7fff81865ad1 __schedule ([kernel.kallsyms])
	    7fff81865fd5 schedule ([kernel.kallsyms])
	    7fff81869a35 schedule_hrtimeout_range_clock ([kernel.kallsyms])
	    7fff81869a63 schedule_hrtimeout_range ([kernel.kallsyms])
	    7fff812355e4 poll_schedule_timeout ([kernel.kallsyms])
	    7fff81236c73 do_sys_poll ([kernel.kallsyms])
	    7fff81236e95 sys_poll ([kernel.kallsyms])
	    7fff8186a95b entry_SYSCALL_64_fastpath ([kernel.kallsyms])
	           fb80d [unknown] (/lib/x86_64-linux-gnu/libc-2.23.so)
	             285 [unknown] ([unknown])
	ff24448d491374e4 [unknown] ([unknown])
'''

def
#声明一个二维数组

book_name_xls = 'xls格式测试工作簿.xls'
sheet_name_xls = 'xls格式测试表'
sheet_name_xls1 = 'xls格式测试表1'
value_title = [["姓名", "性别", "年龄", "城市", "职业"],]

dso_name = get_dso_name("dso.csv")
sheet_name_dso = 'geekbench_dso统计'
write_excel_xls(book_name_xls, sheet_name_xls, value_title)



write_excel_xls_new(book_name_xls, sheet_name_dso, value_title)
write_excel_xls_append(book_name_xls, sheet_name_dso, dso_name)

for i in dso_name:
    write_excel_xls_new(book_name_xls, i[2].strip(']').strip('['), value_title)

#write_excel_xls(book_name_xls, sheet_name_xls1, value_title)
write_excel_xls_new(book_name_xls, sheet_name_xls1, value_title)
value = [[],]
f = open("./report.txt")
count = 0
for line in f:
    #print(line)
    if line[0] != '#':
        a = line.split( )
        value[0] = a
        for i in dso_name:
            if i[2] in a:
                write_excel_xls_append(book_name_xls, i[2].strip(']').strip('['), value)
            #else:
                #write_excel_xls_append(book_name_xls, sheet_name_xls1, value)
f.close()


