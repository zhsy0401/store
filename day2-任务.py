'''
#第一题
x=input("")
num=[int(n) for n in x.split()]
print(sum(num))

第二题
x=input("")
num=[int(n) for n in x.split()]
print("最大值：",max(num))
print("和:",sum(num))
print("平均数：",sum(num)/10)

第三题
import random
num=random.randint(50,150)
print(num)

第四题
a,b,c=map(int ,input().split())
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('等边三角形')
    elif a==b or a==c or b==c:
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print('等腰直角三角形')
        else:
            print('等腰三角形')
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print('直角三角形')
    else:
        print('普通三角形')
else:
    print('无法构成三角形')

第五题
a=int(56)
b=int(78)
a=a+b
b=a-b
a=a-b
print("A=",a)
print("B=",b)

第六题
import sys
i=3
while i:
    x=input("用户名：")
    y=input("密码：")
    if x=="root":
        if y=="admin":
         print("登陆成功")
         break
        else:
            print("密码错误")
            i = i - 1
            print("还有",i,"次机会")
    else:
        print("账号错误")
        i=i-1
        print("还有", i, "次机会")

第七题
print("      *      ")
print("     * *     ")
print("    * * *    ")
print("   * * * *   ")
print("  * * * * *  ")
print(" * * * * * * ")
print("* * * * * * *")

第八题
x=int(1)
y=int(1)
while x:
    while y:
        print(x,"*",y,"=",x*y)
        y=y+1
        if y>9:
            y=1
            break
    x=x+1
    if x>9:
        break

第九题
print("1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81")
print("1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64")
print("1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49")
print("1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36")
print("1*5=5 2*5=10 3*5=15 4*5=20 5*5=25")
print("1*4=4 2*4=8  3*4=12 4*4=16")
print("1*3=3 2*3=6  3*3=9")
print("1*2=2 2*2=4")
print("1*1=1")

第十题
i=0
z=20-i
a=0
j=0
while z>0:
     a=a+3
     if  a ==20 :
      print("你出来了")
      break
     else :
       a=a-2
       i = a
       z = 20-i
       j=j+1
       print("第",j,"天了,已经爬了",a,"米")

第十一题
char=int(1)
Oax_li=int(2)
fLul=int(3)
BYTE=int(4)
Cy%ty=int(5)
$123=int(6)
3_3=int(7)
T_T=int(8)

标识符	是否合法	标识符	是否合法
char	合法	Cy%ty	%不合法
Oax_li	合法	$123	$123不合法
fLul	合法	3_3 	33不合法
BYTE	合法	T_T	合法

第十二题
import math
Sum=0
num = int(20)
for i in range(1,num+1):
    F=math.factorial(i)
    Sum +=F
print('阶乘之和：',Sum)
'''