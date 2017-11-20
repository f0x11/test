#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'f0x11'

import xlrd

data = xlrd.open_workbook('test.xlsx')

table = data.sheets()[0]          #通过索引顺序获取
# # table = data.sheet_by_index(0) #通过索引顺序获取
# # table = data.sheet_by_name(u'Sheet1')#通过名称获取
#
# # 获取整行和整列的值（数组）
# i = 0
# table.row_values(i)
print table.col_values(0)
# # 获取行数和列数
# nrows = table.nrows
# ncols = table.ncols
# # 循环行列表数据
# for i in range(nrows ):
#     print table.row_values(i)
#
# # 单元格
# cell_A1 = table.cell(0, 0).value
# cell_C4 = table.cell(2, 3).value
#
# # 使用行列索引
# cell_A1 = table.row(0)[0].value
# cell_A2 = table.col(1)[0].value
#
# # 简单的写入
# row = 0
#
# col = 0
#
# # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
# # ctype = 1
# # value = '单元格的值'
#
# # xf = 0  # 扩展的格式化
#
# # table.put_cell(row, col, ctype, value, xf)
