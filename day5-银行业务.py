
import random
# print("==============================================")
# print("|------------中国工商银行账户管理系统------------|")
# print("|------------1、开户              ------------|")
# print("|------------2、取钱              ------------|")
# print("|------------3、存钱              ------------|")
# print("|------------4、转账              ------------|")
# print("|------------5、查询              ------------|")
# print("|------------6、退出              ------------|")
# print("==============================================")
bank={}#创建一个空的字典
#开户逻辑
bank_name="狼腾测试猿银行"
#                第一个对应第一个 不是名称对应名称



def bank_adduser(account,username,password,country,province,street,door):
                #账号     用户名     密码      国家      省份    街道  门牌
    if  len(bank) >100:
        return 3
    if username in bank:#  如变量在容器内执行下面的代码
        return 2
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
    account=random.randint(10000000,99999999)

    while 1:#判断随机数生成的账号是否重复,循环到不重复为止
        if account in bank:
            account=random.randint(10000000,99999999)
        else:
            break

    stast=bank_adduser(account,username,password,country,province,street,door)
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
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
#{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}



def moneyin():#存钱
    bankname = input("请输入用户名：")
    if bankname in bank:
        num = input("存入金额：")
        num = int(num)
        if num < 0:
            num = 0
        bank[bankname]["money"] = bank[bankname]["money"]+num
        info = '''
                        *-----------存款凭证-----------*
                        | 用户名:%s                    
                        | 账号：%s                     
                        | 余额：%s                     
                        | 银行名称: %s                 
                        *-----------------------------*
                        '''
        # 每个元素都可传入%
        print(info % (bankname, bank[bankname]["account"], bank[bankname]["money"], bank_name))
    else:
        return False



def moneyout():#取钱
    bankname = input("请输入用户名：")
    bankpassword = input("请输入密码：")
    if bankname in bank:
        if bankpassword in bank[bankname]["password"]:
            out = input("请输入要取出的金额：")
            out = int(out)
            if out < 0:
                out = 0
            if out <= bank[bankname]["money"]:
                bank[bankname]["money"] = bank[bankname]["money"] - out
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
                print(info % (bankname, bank[bankname]["account"], out,bank[bankname]["money"], bank_name))
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
    bankname = input("请输入用户名：")
    bankpassword = input("请输入密码：")
    if bankname in bank:
        if bankpassword in bank[bankname]["password"]:
            pushname = input("请输入收款用户名：")
            if pushname in bank:
                money = input("请输入转账金额：")
                money = int(money)
                if money < 0:
                    money = 0
                if money <= bank[bankname]["money"]:
                    print("是否转账（谨防诈骗！）")
                    tf = input("请输入是(yes)或否(no)：")
                    if tf == '是' or tf == 'yes' or tf == 'YES':
                        bank[pushname]["money"] = bank[pushname]["money"]+money
                        bank[bankname]["money"] = bank[bankname]["money"]-money
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
                        print(info % (bankname, bank[bankname]["account"],pushname,bank[pushname]["account"], money, bank[bankname]["money"], bank_name))
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
    bankname = input("请输入用户名：")
    bankpassword = input("请输入密码：")
    if bankname in bank:
        if bankpassword in bank[bankname]["password"]:
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
            print(info % (bankname, bank[bankname]["account"], bankpassword, bank[bankname]["country"], bank[bankname]["province"], bank[bankname]["street"],bank[bankname]["door"] , bank[bankname]["money"], bank_name))
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
        break