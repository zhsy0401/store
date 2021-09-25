from threading import Thread
import threading
import time

lock = threading.RLock()

bread = 500
bmoney = 2

class buy(Thread):
    by = ""

    def run(self) -> None:
        self.num = int(0)
        self.money = int(3000)
        global bread,bmoney,book#全局变量

        while 1:

            if bread >= 1:
                if self.money >= 2:
                    if bread == 0:
                        lock.acquire()
                        print("蛋挞卖空了，请稍等")
                        time.sleep(2)#（1/5）如想快速查看结果，请把本行前加 #
                        lock.release()
                        continue
                    bread = bread - 1
                    self.money = self.money - bmoney
                    self.num = self.num + 1
                    lock.acquire()
                    print(self.by, "买了一个蛋挞，ta一共买了", self.num, "个蛋挞")#（2/5）如想快速查看结果，请把本行前加 #
                    lock.release()
                else:
                    lock.acquire()
                    print(self.by,"钱包空了，就剩韭菜根了 ta拥有了",self.num,"个蛋挞*****************************************************************************","\n")
                    lock.release()
                    break
            else:
                lock.acquire()
                print("蛋挞卖空了，请稍等")#（3/5）如想快速查看结果，请把本行前加 #
                time.sleep(2)#（4/5）如想快速查看结果，请把本行前加 #
                lock.release()
                continue


class sell(Thread):
    sl = ""

    def run(self) -> None:

        global bread

        while 1:

            if bread == 500:
                time.sleep(3)
                continue
            else:

                bread = bread + 1
                lock.acquire()
                print(self.sl,"师傅制作了一个蛋挞，现在一共有",bread,"个蛋挞在销售")#（5/5）如想快速查看结果，请把本行前加 #
                lock.release()
                if bread >= 500:
                    continue

                continue


by1 = buy()
by1.by = "韭菜1"
by2 = buy()
by2.by = "韭菜2"
by3 = buy()
by3.by = "韭菜3"
by4 = buy()
by4.by = "韭菜4"
by5 = buy()
by5.by = "韭菜5"
by6 = buy()
by6.by = "韭菜6"

sl1 = sell()
sl1.sl = "镰刀1"
sl2 = sell()
sl2.sl = "镰刀2"
sl3 = sell()
sl3.sl = "镰刀3"

by1.start()
by2.start()
by3.start()
by4.start()
by5.start()
by6.start()

sl1.start()
sl2.start()
sl3.start()