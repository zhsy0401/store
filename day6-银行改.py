
import random
import pymysql
con = pymysql.connect(host="localhost",user="root",password="",database="banksql")
cursor =con.cursor()

bank={}#创建一个空的字典
#开户逻辑
bank_name="狼腾测试猿银行"
#                第一个对应第一个 不是名称对应名称



def bank_adduser(account,username,password,country,province,street,door,money):
                #账号     用户名     密码      国家      省份    街道  门牌
    sql = "select count(*) from bank"
    cursor.execute(sql)
    date = cursor.fetchall()
    if  date[0][0] >=100:
        return 3
    sql = "select * from bank where username = %s"
    param = username
    cursor.execute(sql,param)
    date = cursor.fetchall ()
    if len(date) != 0:#  如变量在容器内执行下面的代码
        return 2
    else :
        sql = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account,username,password,country,province,street,door,money]
        cursor.execute(sql, param)
        con.commit()
        bank[username]={
            "account":account,#
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1



def adduser():#定义了一个方法，新增用户
    username=input("请输入您的用户名:")
    password = input("请输入您的密码:")
    print("请输入您的居住地址:")
    country=input("\t\t请输入国家:")
    province=input("\t\t请输入省份:")
    street=input("\t\t请输入城市:")
    door=input("\t\t请输入详细地址:")
    money=0
    account=random.randint(10000000,99999999)

    while 1:#判断随机数生成的账号是否重复,循环到不重复为止
        sql = "select * from bank where account = %s"
        param = account
        cursor.execute(sql, param)
        date = cursor.fetchall()
        if len(date) != 0:
            account=random.randint(10000000,99999999)
        else:
            break

    stast=bank_adduser(account,username,password,country,province,street,door,money)
    #        调用方法   （元素，，，，，，，，，）
    if stast ==3 :
        print("你去别的银行吧")
    elif stast== 2:
        print("开户失败，你别重复")
    elif stast== 1:
        info = '''
                    *-----------个人信息------------
                    | 用户名:%s                    
                    | 账号：%s                     
                    | 密码：*****                  
                    | 国籍：%s                     
                    | 省份：%s                     
                    | 街道：%s                     
                    | 门牌号：%s                   
                    | 余额：%s                     
                    | 开户行名称：%s                
                    *-----------------------------*
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, money, bank_name))
#{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}



def moneyin():#存钱
    account = input("请输入账号：")
    sql = "select * from bank where account = %s"
    param = account
    cursor.execute(sql, param)
    date = cursor.fetchall()
    if len(date) != 0:
        num = input("存入金额：")
        num = int(num)
        if num < 0:
            num = 0
        sql = "update bank set money=money+%s where account = %s"
        param = [num, account]
        cursor.execute(sql, param)
        con.commit()
        sql = "select * from bank where account = %s"
        param = account
        cursor.execute(sql, param)
        date = cursor.fetchall()  # ((password,),)
        info = '''
                        *-----------存款凭证-----------*
                        | 用户名:%s                    
                        | 账号：%s                     
                        | 余额：%s                     
                        | 银行名称: %s                 
                        *-----------------------------*
                        '''
        # 每个元素都可传入%
        print(info % (date[0][1],date[0][0],date[0][7],bank_name))
    else:
        return False



def moneyout():#取钱
    account = input("请输入账号：")
    bankpassword = input("请输入密码：")
    bankpassword = int(bankpassword)
    sql = "select * from bank where account = %s"
    param = account
    cursor.execute(sql, param)
    date = cursor.fetchall()
    if len(date) != 0:
        sql = "select password from bank where account = %s"
        param = account
        cursor.execute(sql, param)
        date = cursor.fetchall()#((password,),)
        if bankpassword == date[0][0]:
            out = input("请输入要取出的金额：")
            out = int(out)
            if out < 0:
                out = 0
            sql = "select money from bank where account = %s"
            param = account
            cursor.execute(sql, param)
            date = cursor.fetchall()  # ((password,),)
            if out <= date[0][0]:
                sql = "update bank set money=money-%s where account = %s"
                param = [out,account]
                cursor.execute(sql, param)
                con.commit()
                sql = "select * from bank where account = %s"
                param = account
                cursor.execute(sql, param)
                date = cursor.fetchall()  # ((password,),)
                info = '''
                        *-----------存款凭证-----------*
                        | 用户名:%s                    
                        | 账号：%s 
                        | 取出金额：%s                   
                        | 余额：%s                     
                        | 银行名称: %s                 
                        *-----------------------------*
                                        '''
                # 每个元素都可传入%
                print(info % (date[0][1], date[0][0],out,date[0][7],bank_name))
                return 0
            else:
                print("去赚钱吧！你还没有那么多钱")
                return 3
        else:
            print("取钱密码都能忘？？？")
            return 2
    else:
        print("用户名错误，再想想！")
        return 1



def moneygo():#转账
    account = input("请输入账号：")
    bankpassword = input("请输入密码：")
    bankpassword = int(bankpassword)
    sql = "select * from bank where account = %s"
    param = account
    cursor.execute(sql, param)
    date = cursor.fetchall()
    if len(date) != 0:
        sql = "select password from bank where account = %s"
        param = account
        cursor.execute(sql, param)
        dateout = cursor.fetchall()  # ((password,),)
        if bankpassword == dateout[0][0]:
            accountin = input("请输入转入账号：")
            sql = "select * from bank where account = %s"
            param = accountin
            cursor.execute(sql, param)
            datein = cursor.fetchall()

            if len(datein) != 0:
                money = input("请输入转账金额：")
                money = int(money)
                if money < 0:
                    money = 0
                sql = "select money from bank where account = %s"
                param = account
                cursor.execute(sql, param)
                date = cursor.fetchall()  # ((password,),)
                if money <= date[0][0]:
                    print("是否转账（谨防诈骗！）")
                    tf = input("请输入是(yes)或否(no)：")
                    if tf == '是' or tf == 'yes' or tf == 'YES':
                        sql = "update bank set money=money-%s where account = %s"
                        param = [money, account]
                        cursor.execute(sql, param)
                        con.commit()
                        sql = "update bank set money=money+%s where account = %s"
                        param = [money, accountin]
                        cursor.execute(sql, param)
                        con.commit()
                        sql = "select * from bank where account = %s"
                        param = account
                        cursor.execute(sql, param)
                        date = cursor.fetchall()  # ((password,),)

                        sql = "select * from bank where account = %s"
                        param = accountin
                        cursor.execute(sql, param)
                        datein = cursor.fetchall()  # ((password,),)
                        info = '''
                             *-----------存款凭证-----------*
                             | 用户名：%s                    
                             | 账号：%s 
                             | 收款用户：%s
                             | 收款账号：%s 
                             | 转账金额：%s                   
                             | 余额：%s                     
                             | 银行名称: %s                 
                             *-----------------------------*
                                                                '''
                        # 每个元素都可传入%
                        print(info % (date[0][1],date[0][0],accountin,datein[0][1],money,date[0][7],bank_name))
                        return 0
                    else:
                        print("取消转账")
                else:
                    print("去赚钱吧！你还没有那么多钱")
                    return 3
            else:
                print("再问一问收款账户嗷，谨防诈骗！")
                return 1
        else:
            print("转账密码都能忘？？？")
            return 2
    else:
        print("用户名错误，再想想！")
        return 1



def howmoney():
    account = input("请输入账号：")
    bankpassword = input("请输入密码：")
    bankpassword=int(bankpassword)
    sql = "select * from bank where account = %s"
    param = account
    cursor.execute(sql, param)
    date = cursor.fetchall()
    if len(date) != 0:
        sql = "select password from bank where account = %s"
        param = account
        cursor.execute(sql, param)
        dateout = cursor.fetchall()  # ((password,),)
        if bankpassword == dateout[0][0]:
            sql = "select * from bank where account = %s"
            param = account
            cursor.execute(sql, param)
            date = cursor.fetchall()  # ((password,),)
            info = '''
                                *-----------个人信息------------
                                | 用户名:%s                    
                                | 账号：%s                     
                                | 密码：%s                  
                                | 国籍：%s                     
                                | 省份：%s                     
                                | 城市：%s                     
                                | 详细地址：%s                   
                                | 余额：%s                     
                                | 开户行名称：%s                
                                *-----------------------------*
                            '''
            # 每个元素都可传入%
            print(info % (date[0][1],date[0][0],date[0][2],date[0][3],date[0][4],date[0][5],date[0][6],date[0][7],bank_name))
        else:
            print("密码错误！！！")
    else:
        print("用户名错误")



#begin = input("请选择业务")
while True:
    print("==============================================")
    print("|------------中国工商银行账户管理系统------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、取钱              ------------|")
    print("|------------3、存钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")
    begin = input("请选择业务:")
    if begin =="1":#您输入的业务等于1执行开户操作
        adduser()
        continue
    elif begin == "2":
        moneyout()
        continue
    elif begin == "3":
        moneyin()
        continue
    elif begin == "4" :
        moneygo()
        continue
    elif begin == "5":
        howmoney()
        continue
    else:
        print(6,"、退出")
        cursor.close()
        con.close()
        break