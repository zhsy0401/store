# '''
# 开发一个商城。
# 需求：
# 买XXXX东西
# 资金结算
# XXXXX水果商城
# 金钱加在一起。
# 水果：
# 编号、名称、单价、数量、质量、产地
# '''
# print("-----------Frank水果商城--------") #  打印水果商城
# print("编号   名称    单价   数量    产地    质量  ")
# print(" 1    榴莲      75    20     北极   AAA")
# print(" 2    黄桃      7.5   300    南极   AAAA")
# print(" 3    鳄梨🥑     15   120    墨西哥  AAAAA")
# print(" 4    西番莲     5    90000   新疆   A++")
# money=(75*20+7.5*300+15*120+5*90000)
# # 变量名 赋值  值
# print("总价格为：",money)
# #                变量引用
# #        str     分隔符    计算公式or变量
print("-----------衣服销售数据的统计与分析------------")
print("总销售额：")

yrf=253.6
yrf1=10+69+140+10+10

nzk=86.3
nzk1=60+72+35+90+60+60+140

fy=96.8
fy1=43+25+43+60+43+78

pc=135.9
pc1=63+24+63+57

tx=65.8
tx1=63+45+129+63+58+48+63

cs=49.3
cs1=120

sum=yrf*yrf1+nzk*nzk1+fy*fy1+pc*pc1+tx*tx1+cs*cs1

print('%.3f'%sum)

print("平均每日销售数量：")

mr=yrf1+nzk1+fy1+pc1+tx1+cs1
mrpj=mr/30

print('%.3f'%mrpj)

print("月销售量占比：")

yrf1=yrf1/mr*100
nzk1=nzk1/mr*100
fy1=fy1/mr*100
pc1=pc1/mr*100
tx1=tx1/mr*100
cs1=cs1/mr*100

print("羽绒服：",'%.2f'%yrf1,"%")
print("牛仔裤：",'%.2f'%nzk1,"%")
print("风衣：",'%.2f'%fy1,"%")
print("皮草：",'%.2f'%pc1,"%")
print("T恤：",'%.2f'%tx1,"%")
print("衬衫：",'%.2f'%cs1,"%")
