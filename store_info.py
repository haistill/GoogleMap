from selenium  import webdriver
import csv

def store_info(data_name):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)

    writer=csv.writer(open(data_name+'_info.csv','wb'))
    reader=csv.reader(open(data_name+'.csv','rb'))
    for row in reader:
        url=row
        print url
        driver.get(url)
        name=driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div[1]/div/div[2]/div[1]/h1').text
        street=driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div[1]/div/div[3]/div[1]/div/div[2]/ul/li[1]/strong/address/span[1]').text
        post=driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div[1]/div/div[3]/div[1]/div/div[2]/ul/li[1]/strong/address/span[4]').text
        coordinate=driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div[1]/div/div[3]/div[1]/div/div[1]/div').get_attribute("data-map-state")

        latitude=str(coordinate).split('{"latitude":')
        latitude=latitude[1].split(',"longitude":')
        latitude=latitude[0]
        latitude=latitude.split(',')
        latitudes=latitude[0]

        longitude=latitude[1].split(':')
        longitude=longitude[1].split('}')
        longitude=longitude[0]
        try:
            open_day=driver.find_element_by_xpath('//*[@id="super-container"]/div/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/th').text
            print open_day,'open day'
            open_start=driver.find_element_by_xpath('//*[@id="super-container"]/div/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]').text
            print open_start,'open start'
        except:
            open_day='null'
            open_start='null'
        try:
            busi_info1=driver.find_element_by_xpath('//*[@id="super-container"]/div/div/div[2]/div[2]/div[3]/ul/li/div/dl[1]/dt').text
            busi_info1_result=driver.find_element_by_xpath('//*[@id="super-container"]/div/div/div[2]/div[2]/div[3]/ul/li/div/dl[1]/dd').text
            print busi_info1
        except:
            busi_info1=driver.find_element_by_xpath('//*[@id="super-container"]/div/div/div[2]/div[2]/div[2]/ul/li/div/dl[1]/dt').text
            busi_info1_result=driver.find_element_by_xpath('//*[@id="super-container"]/div/div/div[2]/div[2]/div[2]/ul/li/div/dl[1]/dd').text
            print busi_info1
        rating=driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div/i').get_attribute("title")
        num_review=driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/span/span').text
        writer.writerow([street,post,latitudes,longitude,open_day,open_start,busi_info1,busi_info1_result,rating,num_review])
        driver.get('http:\\www.google.com')
