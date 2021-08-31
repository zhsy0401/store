# list=[1,2,3,4,5,6,7,8,9]#通过角标来获取值
#     0 1 2 3 4 5 6 7 8
#        raenge数数（len长度，list的长度）
# for i in range(len(list)):#   i  in  结果赋值给i ，i=range(len(list))
#     print(list[i])#1,2,3,4,5,6,7,8,9
import sys


dict={"北京":{"昌平":{"沙河":{"七马路":{"育荣教育园区":"狼腾测试员"}}}},
      "天津":{"滨海新区":{"塘沽":{"第五大道":{"滨海国际会议中心":"会展中心"}}}},
      "秦皇岛":{"北戴河区":{"戴河镇":{"金港大道":"河北环境工程学院"}}},
       "邢台市":{"信都区":{"郭守敬大道":"七里河市民体育公园"}},
      "承德市":{"围场县":{"御道口":"木兰围场游客服务中心"}},0:0
      }


i = input("请输入地名")


if i == "北京":
    changping = input("请输入地名")
    if changping == "昌平":
        shahe = input("请输入地名")
    else:
        print("404")
        sys.exit(0)
    if shahe == "沙河":
        qml = input("请输入地名")
    else:
        print("404")
        sys.exit(0)
    if qml == "七马路":
        qyjyyq = input("请输入地名")
    else:
        print("404")
        sys.exit(0)
    if qyjyyq == "育荣教育园区":
        print(dict[i][changping][shahe][qml][qyjyyq])
    else:
        print("404")
        sys.exit(0)


if i == "天津":
    bhxq = input("请输入地名")
    if bhxq == "滨海新区":
        tg = input("请输入地名")
    else:
        print("404")
        sys.exit(0)
    if tg == "塘沽":
         dwdd = input("请输入地址")
    else:
        print("404")
        sys.exit(0)
    if dwdd == "第五大道":
        hyzx = input("请输入地名")
    else:
        print("404")
        sys.exit(0)
    if hyzx == "滨海国际会议中心":
        print(dict[i][bhxq][tg][dwdd][hyzx])
    else:
        print("404")
        sys.exit(0)


if i == "秦皇岛":
    bdh = input("请输入地名")
    if bdh == "北戴河区":
        dhz = input("请输入地址")
    else:
        print("404")
        sys.exit(0)
    if dhz == "戴河镇":
        jg = input("请输入地名")
    else:
        print("404")
        sys.exit(0)
    if jg == "金港大道":
        print(dict[i][bdh][dhz][jg])
    else:
        print("404")
        sys.exit(0)


if i == "邢台市":
    xd = input("请输入地名")
    if xd == "信都区":
        gsj = input("请输入地址")
    else:
        print("404")
        sys.exit(0)
    if gsj == "郭守敬大道":
        print(dict[i][xd][gsj])
    else:
        print("404")
        sys.exit(0)


if i == "承德市":
    wc = input("请输入地名")
    if wc == "围场县":
        ydk = input("请输入地址")
    else:
        print("404")
        sys.exit(0)
    if ydk == "御道口":
        print(dict[i][wc][ydk])
    else:
        print("404")
        sys.exit(0)