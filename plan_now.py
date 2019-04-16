#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
第二种扣税方法：累计预扣法
"""
rate = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
base = [0, 36000, 144000, 300000, 420000, 660000, 960000]
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

#print("%.2f" % income)
pre_tax = 0
for k in range(1,13,1):
	income = (18000 - wuxian - yijin - zhuanxiang - 5000) * k
#	print("第 %d 月应纳税额：%.2f" % (k, income))

	for i in range(len(base)):
		if income > base[i]:
			continue
		else:
			if i < 2:
				tax = income * 0.03 - pre_tax
				pre_tax = income * 0.03
				print("tax: %.2f" % tax)
			else:
				tax = income * rate[i-1] - susuan[i-2] - pre_tax
				pre_tax = pre_tax + tax 
				print("tax: %.2f" % tax)
#			print("%d, %d, %d" % (i, base[i], susuan[i-2]))
			break

print("total tax : %.2f" % pre_tax)
	

