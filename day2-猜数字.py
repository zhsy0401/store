'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：你的初始资金为100 每猜一次减10  资金为0时或者猜成功游戏结束
    猜大 如果你输入的数字和随机数对比 大于随机数  打印一句话为  猜大了
    猜小 如果你输入的数字和随机数对比 小于随机数  打印一句话为  猜小了

import random
#                 范围
num=random.randint(0, 2)#   随机一个数字赋值给num
#        这是一个随机数函数   起始值为0     终止值为20000
print(num)#打印一个随机数
while 1:
    a=input("请输入一个数字")# 从键盘上输入一个   字符    赋值给a
    a= int(a)
    if  a == num :
        print("你成功了")
        break
    else:
        print("你失败了，请再次输入")
'''
import random
num=random.randint(0,9999)
print(num)
i=int(100)
print("---------------猜数字----------------")
print("输入您所猜测的数字（数字范围为0~9999），每次猜测需扣除10点金额")
print("您的资金余额为：",i)
while 1:
    a=input("请输入您所猜测的数字:")
    i = i - 10
    print("您的金额剩余：",i)
    a=int(a)
    if a>num:
        print("您猜大了")
    elif a<num:
        print("您猜小了")
    elif a==num:
        print("恭喜您，猜对了！")
        break
    if i==0:
        print("游戏结束，您的金额为0")
        break

