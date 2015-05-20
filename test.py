__author__ = 'haistill'

from selenium  import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(1)
driver.get('https://www.meteor.com/blog/2015/04/24/how-to-give-a-conference-talk-on-meteor')
content = driver.find_element_by_xpath('//*[@id="content"]/p[1]/text()')
print content