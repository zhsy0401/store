from selenium import webdriver
import time
# 创建谷歌浏览器对象
driver = webdriver.Chrome()



# 任务一
#
# # 打开百度网址
# driver.get("http://www.baidu.com")
#
# # 窗口最大化
# driver.maximize_window()
#
#
# #寻找搜索输入框
# driver.find_element_by_id("kw").send_keys("python")
#
# # 点击百度一下按钮
# driver.find_element_by_id("su").click()
#
# time.sleep(3)


# #任务二-1弹窗的验证
# driver.get(r"D:\学习资料\python自动化测试\测试环境搭建\自动化\练习的html\练习的html\弹框的验证\dialogs.html")
#
# driver.maximize_window()
#
# driver.find_element_by_xpath("//*[@id='confirm']").click()
#
# time.sleep(2)
#
# driver.switch_to.alert.accept()#点击确定
# # driver.switch_to.alert.dismiss()#点击取消



# #任务二-表单提交（包括上传文件和下拉列表）
# driver.get(r"D:\学习资料\python自动化测试\测试环境搭建\自动化\练习的html\练习的html\上传文件和下拉列表\autotest.html")
#
# driver.maximize_window()
#
# driver.find_element_by_xpath("//*[@id='accountID']").send_keys("魔法书")
# time.sleep(0.5)
# driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("12838")
# time.sleep(0.5)
# driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
# time.sleep(0.5)
# driver.find_element_by_xpath("//*[@id='sexID1']").click()#男
# # driver.find_element_by_xpath("//*[@id='sexID2']").click()#女
# time.sleep(0.5)
# driver.find_element_by_xpath("//*[@value='spring']").click()#春夏！！！！！！！！！！！
# driver.find_element_by_xpath("//*[@value='summer']").click()
# # driver.find_element_by_xpath("//*[@value='Auterm']").click()#秋冬！！！！！！！！！！！
# #driver.find_element_by_xpath("//*[@value='winter']").click()
# time.sleep(0.5)
# driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\zhsy\Pictures\可爱长发女孩.jpg")
# time.sleep(0.5)
# driver.find_element_by_xpath("//*[@id='buttonID']").click()




# #任务二-页面跳转
# driver.get(r"D:\学习资料\python自动化测试\测试环境搭建\自动化\练习的html\练习的html\跳转页面\pop.html")
#
# driver.maximize_window()
#
# driver.find_element_by_xpath("//*[@id='goo']").click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[1])
#
# #寻找搜索输入框
# driver.find_element_by_id("kw").send_keys("python")
#
# # 点击百度一下按钮
# driver.find_element_by_id("su").click()






#任务三-京东购物
driver.get("https://www.jd.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("MagicBook")

driver.find_element_by_xpath("//*[@class='button']").click()
time.sleep(0.5)

driver.find_element_by_xpath("//*[@src='//img30.360buyimg.com/popshop/jfs/t1/139060/38/19638/2825/5fe0477aE64df77e0/55af9759d5e9d78a.jpg']").click()

time.sleep(0.5)

driver.find_element_by_xpath("//*[@src='//img14.360buyimg.com/n7/jfs/t1/84552/11/16868/279058/6139a966Ea6268c1b/3906b0dbe3109151.jpg']").click()

time.sleep(7)

driver.switch_to.window(driver.window_handles[1])
driver.close()



time.sleep(3)
# 退出浏览器
driver.quit()

