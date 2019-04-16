#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
第一种扣税方法
"""
rate = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
base = [0, 3000, 12000, 25000, 35000, 55000, 80000]
temp_total = []
susuan = []

for i in range(0, 6, 1):
	temp_total.append((base[i+1]-base[i])*rate[i])

for i in range(1,7,1):
	sub_total = 0
	for j in range(i, 0, -1):
		sub_total = sub_total + temp_total[j-1]
	susuan.append(base[i] * rate[i] - sub_total)

#print(susuan)

income = float(input("每月工资： "))
wuxian = float(input("五险: "))
yijin = float(input("公积金: "))
zhuanxiang = float(input("专项扣除: "))

income = income - wuxian - yijin - zhuanxiang - 5000

# print("%.2f" % income)
for i in range(len(base)):
	if income > base[i]:
		continue
	else:
		print("tax: %.2f" % (income * rate[i-1] - susuan[i-2]))
#		print("%d, %d, %d" % (i, base[i], susuan[i-2]))
		break


