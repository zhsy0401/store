import xlrd

wb = xlrd.open_workbook(filename=r"C:\Users\zhsy\OneDrive\桌面\day07【mysql工具类与excel读取】\2020年每个月的销售情况.xlsx")

sum = int(0)
num = int(0)
book = {}



def all(i):#计算全年总销售额
    sheet = wb.sheet_by_name('%s'%i)
    num = int (0)
    rows = sheet.nrows
    for i in range(1,rows):
        date = sheet.row_values(i)
        num = num + date[2] * date[4]
    return num


def zb(book,i):#销售占比
    sheet = wb.sheet_by_name('%s' % i)
    rows = sheet.nrows
    for i in range(1, rows):
        date = sheet.row_values(i)
        name = date[1]
        num = date[4]
        if name in book:
            book[name] = book[name] + num
            continue
        else:
            book[name]=num
            continue
    a=int(0)
    for i in book.values():
        a += i
    return a



def yf(book,i):#计算月总销售额
    sheet = wb.sheet_by_name('%s' % i)
    rows = sheet.nrows
    for i in range(1, rows):
        date = sheet.row_values(i)
        name = date[1]
        num = date[4]
        if name in book:
            book[name] = book[name] + num
            continue
        else:
            book[name] = num
            continue
    c = int (0)
    for i in book.values():
        c += i
    return c



def xse(book,i):#计算并输出销售额占比
    sheet = wb.sheet_by_name('%s' % i)
    rows = sheet.nrows
    for i in range(1, rows):
        date = sheet.row_values(i)
        name = date[1]
        if name in book:
            book[name] = book[name] + num * date[2]
            continue
        else:
            book[name]=num * date[2]
            continue
    e=int(0)
    for i in book.values():
        e += i
    return e



def zd(book,i):#最畅销的衣服是那种
    sheet = wb.sheet_by_name('%s' % i)
    rows = sheet.nrows
    for i in range(1, rows):
        date = sheet.row_values(i)
        name = date[1]
        num = date[4]
        if name in book:
            book[name] = book[name] + num
            continue
        else:
            book[name]=num
            continue
    f = max(book.values())
    f = int(f)
    return f



def zs(book,i):#最畅销的衣服是那种
    sheet = wb.sheet_by_name('%s' % i)
    rows = sheet.nrows
    for i in range(1, rows):
        date = sheet.row_values(i)
        name = date[1]
        num = date[4]
        if name in book:
            book[name] = book[name] + num
            continue
        else:
            book[name]=num
            continue
    f = min(book.values())
    f = int(f)
    return f









time = ("1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月")

for i in time:#计算并输出全年总销售额
    sum = sum + all(i)
    num = zb(book,i)

# print("全年总销售额：",round(sum,2),"元")
# print("")



# for i in book.keys():#计算并输出销售占比
#     book[i] = book[i]/num*100
#     book[i] = float("%.2f"%book[i])
#     print(i,"的全年销售（件数）占比：",book[i],"%")
# print("")
# print("")




# book = {}
# for i in time:#计算并输出月总销售额
#     book = {}
#     c = yf(book,i)
#     print("")
#     print(i,"销售（件数）占比")
#     for l in book.keys():
#         book[l] = book[l] / c * 100
#         book[l] = float("%.2f" % book[l])
#         print(l, "的销售（件数）占比：", book[l], "%")
# print("")
# print("")




# book = {}
#
# for i in time:#计算并输出销售额占比
#     d = xse(book,i)
#
# for i in book.keys():
#     book[i] = book[i] / d * 100
#     book[i] = float("%.2f" % book[i])
#     print(i, "的全年销售额占比：", book[i], "%")
# print("")





# book = {}
# for i in time:#最畅销的衣服是那种
#     g = zd(book,i)
# for i in book.keys():
#     if book[i] == g:
#         print("最畅销的衣服是：",i)
# print("")



# book = {}
# j1 = ("2月","3月","4月")
# for i in j1:#第一季度最畅销的衣服是那种
#     g = zd(book,i)
# for i in book.keys():
#     if book[i] == g:
#         print("第一季度最畅销的衣服是：",i)
#         print("")
#
# book = {}
# j2 = ("5月","6月","7月")
# for i in j2:#第二季度最畅销的衣服是那种
#     g = zd(book,i)
# for i in book.keys():
#     if book[i] == g:
#         print("第二季度最畅销的衣服是：",i)
#         print("")
#
# book = {}
# j3 = ("8月","9月","10月")
# for i in j3:#第三季度最畅销的衣服是那种
#     g = zd(book,i)
# for i in book.keys():
#     if book[i] == g:
#         print("第三季度最畅销的衣服是：",i)
#         print("")
#
# book = {}
# j4 = ("11月","12月","1月")
# for i in j4:#第四季度最畅销的衣服是那种
#     g = zd(book,i)
# for i in book.keys():
#     if book[i] == g:
#         print("第四季度最畅销的衣服是：",i)
#         print("")

# book = {}
# for i in time:#最畅销的衣服是那种
#     g = zs(book,i)
# for i in book.keys():
#     if book[i] == g:
#         print("全年销量最低的衣服：",i)
#         print("")







while True:
    print("")
    info = '''
                    *-----------------------------*
                    请选择您需要查询的问题：
                    1、全年的销售总额
                    2、每件衣服的销售（件数）占比
                    3、每件衣服的月销售占比
                    4、每件衣服的销售额占比
                    5、最畅销的衣服是那种
                    6、每个季度最畅销的衣服
                    7、全年销量最低的衣服
                    
                    输入任意字母退出查询              
                    *-----------------------------*
                    例：请选择问题:1
            '''
    print(info)
    begin = input("请选择问题:")
    print("")
    if begin =="1":#

        print("全年总销售额：", round(sum, 2), "元")
        print("")
        continue

    elif begin == "2":

        for i in book.keys():  # 计算并输出销售占比
            book[i] = book[i] / num * 100
            book[i] = float("%.2f" % book[i])
            print(i, "的全年销售（件数）占比：", book[i], "%")
        continue

    elif begin == "3":

        book = {}
        for i in time:  # 计算并输出月总销售额
            book = {}
            c = yf(book, i)
            print("")
            print(i, "销售（件数）占比")
            for l in book.keys():
                book[l] = book[l] / c * 100
                book[l] = float("%.2f" % book[l])
                print(l, "的销售（件数）占比：", book[l], "%")
        continue

    elif begin == "4" :

        book = {}

        for i in time:  # 计算并输出销售额占比
            d = xse(book, i)

        for i in book.keys():
            book[i] = book[i] / d * 100
            book[i] = float("%.2f" % book[i])
            print(i, "的全年销售额占比：", book[i], "%")
        continue

    elif begin == "5":

        book = {}
        for i in time:  # 最畅销的衣服是那种
            g = zd(book, i)
        for i in book.keys():
            if book[i] == g:
                print("最畅销的衣服是：", i)
        continue

    elif begin == "6":

        book = {}
        j1 = ("2月", "3月", "4月")
        for i in j1:  # 第一季度最畅销的衣服是那种
            g = zd(book, i)
        for i in book.keys():
            if book[i] == g:
                print("第一季度最畅销的衣服是：", i)

        book = {}
        j2 = ("5月", "6月", "7月")
        for i in j2:  # 第二季度最畅销的衣服是那种
            g = zd(book, i)
        for i in book.keys():
            if book[i] == g:
                print("第二季度最畅销的衣服是：", i)

        book = {}
        j3 = ("8月", "9月", "10月")
        for i in j3:  # 第三季度最畅销的衣服是那种
            g = zd(book, i)
        for i in book.keys():
            if book[i] == g:
                print("第三季度最畅销的衣服是：", i)

        book = {}
        j4 = ("11月", "12月", "1月")
        for i in j4:  # 第四季度最畅销的衣服是那种
            g = zd(book, i)
        for i in book.keys():
            if book[i] == g:
                print("第四季度最畅销的衣服是：", i)
        continue

    elif begin == "7":

        book = {}
        for i in time:  # 最畅销的衣服是那种
            g = zs(book, i)
        for i in book.keys():
            if book[i] == g:
                print("全年销量最低的衣服：", i)
        continue

    else:
        break