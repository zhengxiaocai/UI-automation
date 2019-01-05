#coding:utf-8

"""
昨天有个小伙伴让我帮忙给写个爬虫，爬的数据很简单，就是查询结果之后的列表数据。
因为，没有学习过爬虫框架，就想用支持UI自动化的selenium来做，这是源码；
敏感信息屏蔽掉了。
"""

from selenium import webdriver
import time
import sys
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('http://****/index.php')
time.sleep(5)

driver.find_element_by_id('user').send_keys(u'******')
time.sleep(3)
driver.find_element_by_id('pass').send_keys(u'123123')
# 至于这里为什么要等30s
# 是因为登录之后要点几个菜单，然后搜索，觉得麻烦就手动操作了。
time.sleep(30)

print u'start',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for i in range(1,1001):
    with open('data.txt', 'a') as f:
        driver.switch_to.frame(driver.find_element_by_id('iframeId'))
        for j in range(1,21):
            print i,j
            driver.execute_script("window.scrollBy ({},{});".format(0, 100))
            f.write(driver.find_element_by_xpath("//tbody/tr["+ str(j) +"]/td[4]").text)
            f.write(u'%')
            f.write(driver.find_element_by_xpath("//tbody/tr[" + str(j) +"]/td[6]").text)
            f.write(u'%')
            f.write(driver.find_element_by_xpath("//tbody/tr[" + str(j) +"]/td[9]").text)
            f.write(u'%')
            f.write(driver.find_element_by_xpath("//tbody/tr[" + str(j) +"]/td[10]").text)
            f.write('\n')
            time.sleep(0.1)
        driver.find_element_by_link_text(u'>>').click()
        time.sleep(3)
        driver.switch_to_default_content()
        time.sleep(1)

time.sleep(3)
print 'end',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

driver.quit()
