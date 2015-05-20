from selenium import webdriver
import csv,time

def store_ult(data_name):
    driver = webdriver.Firefox()
    #driver.implicitly_wait(10)
    writer=csv.writer(open(data_name+'.csv','wb'))
    arr="http://www.yelp.com/search?cflt=restaurants&find_loc=New+York%2C+NY%2C+USA#find_desc&start=0&cflt=food&l=p:NY:New_York:Manhattan:"+data_name
    driver.get(arr)
    max_page=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div[3]/div[1]/div/div[2]/div/div/div').text
    max_page=int(max_page.split(' ')[3])
    print max_page
    for page in range(0,max_page):
        strr="http://www.yelp.com/search?cflt=restaurants&find_loc=New+York%2C+NY%2C+USA#find_desc&start="+str(page*10)+"&cflt=food&l=p:NY:New_York:Manhattan:"+data_name
        driver.get(strr)
        for i in range(1,11):
            store="//*[@id='super-container']/div[3]/div[3]/div[1]/div/div[2]/ul/li["+str(i)+"]/div/div[1]/div[1]/div/div[2]/h3/span/a"
            end_time = time.time()+30
            while end_time > time.time():
                try:
                    store_url=driver.find_element_by_xpath(store).get_attribute("href")
                    if store_url:
                        writer.writerow([store_url])
                        print store_url
                        break
                except:
                    pass
        #driver.get("http://www.google.com")
    driver.close()

if "__main__" == __name__:
    store_ult('Chinatown')

