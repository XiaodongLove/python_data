import xlwt
import datetime

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('Sheet1')

# 字体样式设置
style = xlwt.XFStyle()  # 初始化样式
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.height = 20 * 11  # 字体大小，11为字号，20为衡量单位
font.bold = True  # 黑体
font.underline = True  # 下划线
font.italic = True  # 斜体字
style.font = font  # 设定样式
# 数据写入excel,参数对应 行, 列, 值
worksheet.write(0, 0, 'test_data')  # 不带样式的写入
worksheet.write(1, 0, 'test_data', style)  # 带字体样式的写入

# 设置单元格宽度
worksheet.col(0).width = 3333

# 设置单元格背景颜色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 13
style = xlwt.XFStyle()  # Create the Pattern
style.pattern = pattern  # Add Pattern to Style
worksheet.write(2, 0, 'colour', style)

# 给单元格添加边框方法一
borders = xlwt.Borders()  # Create Borders
borders.left = xlwt.Borders.DASHED  # DASHED虚线，NO_LINE没有，THIN实线
borders.right = xlwt.Borders.DASHED  # borders.right=1 表示实线
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40
style = xlwt.XFStyle()  # Create Style
style.borders = borders  # Add Borders to Style
worksheet.write(3, 0, 'border1', style)

# 给单元格添加边框方法二
# 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7，大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
borders = xlwt.Borders()
borders.left = 1  # 设置为细实线
borders.right = 1
borders.top = 1
borders.bottom = 1
borders.left_colour = 2  # 颜色设置为红色
borders.right_colour = 2
borders.top_colour = 2
borders.bottom_colour = 2
style = xlwt.XFStyle()  # Create Style
style.borders = borders  # Add Borders to Style
worksheet.write(4, 0, 'border2', style)

# 输入一个日期到单元格
style = xlwt.XFStyle()
style.num_format_str = 'M/D/YY'  # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
worksheet.write(5, 0, datetime.datetime.now(), style)

# 单元格添加计算公式
worksheet.write(0, 1, 2)  # Outputs 2
worksheet.write(0, 2, 3)  # Outputs 3
worksheet.write(1, 1, xlwt.Formula('B1*C1'))  # Should output "6" (B1[2] * B2[6])
worksheet.write(1, 2, xlwt.Formula('SUM(B1,C1)'))  # Should output "5" (B1[2] + C1[3])

# 向单元格添加一个超链接
worksheet.write(0, 3, xlwt.Formula(
    'HYPERLINK("http://www.baidu.com";"baidu")'))  # Outputs the text "baidu" linking to http://www.baidu.com

# 单元格合并
worksheet.write_merge(0, 0, 4, 5, 'First Merge')  # 合并0行的4到5列
worksheet.write_merge(1, 2, 4, 5, 'Second Merge')  # 合并1和2行的4到5列

# 设置单元格内容的对其方式
alignment = xlwt.Alignment()  ## Create Alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style = xlwt.XFStyle()
style.alignment = alignment  # Add Alignment to Style
worksheet.write(0, 6, 'alignment', style)

# 保存文件
workbook.save('data_test.xls')
