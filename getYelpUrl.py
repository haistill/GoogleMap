__author__ = 'haistill'

from selenium  import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(1)
userList = []
userSet = set()

def singleUserProfileInfo(url):
    userId = url.split('=')[1]    #userid
    print userId
    driver.get(url)
    profile = []
    for i in range(1,10):
        try:
            profile.append(driver.find_element_by_xpath("//*[@id='user_stats']/li["+str(i)+"]").text)
        except:
            pass
        #print profile
    return profile,userId

def getReviewList(profile,userId):
    reviewNum = int(profile[1].split(' ')[0])
    reviews = []
    for pageNum in range(0,reviewNum/10+1):
        reviewUrl = 'http://www.yelp.com/user_details_reviews_self?userid='+ userId + '&rec_pagestart='+ str(pageNum*10)
        print reviewUrl
        driver.get(reviewUrl)
        for j in range(1,11):
            t = []
            try:
                storeName = driver.find_element_by_xpath("//*[@id='user_main_content']/ul/li["+str(j)+"]/div/div[1]/div/div[2]/div[1]/a").text
                storeCategory = driver.find_element_by_xpath("//*[@id='user_main_content']/ul/li["+str(j)+"]/div/div[1]/div/div[2]/div[2]/span[2]/a[2]").text
                storeAddress = driver.find_element_by_xpath("//*[@id='user_main_content']/ul/li["+str(j)+"]/div/div[1]/div/div[2]/address").text
                reviewTime = driver.find_element_by_xpath("//*[@id='user_main_content']/ul/li["+str(j)+"]/div/div[2]/div[1]/div/span").text
                reviewContent = driver.find_element_by_xpath("//*[@id='user_main_content']/ul/li["+str(j)+"]/div/div[2]/div[1]/p").text
                t.append(storeName)
                t.append(storeCategory)
                t.append(storeAddress)
                t.append(reviewTime)
                t.append(reviewContent)
                print storeName,storeCategory,storeAddress,reviewTime,reviewContent
                reviews.append(t)
            except:
                pass
    return reviews

def getFriendList(profile,userId):
    friendNum = int(profile[0].split(' ')[0])
    friendList = []
    for friendNum in range(0,friendNum/100+1):
        friendUrl = 'http://www.yelp.com/user_details_friends?sort=time_last_reviewed&userid='+userId+'&start='+ str (friendNum*100)
        driver.get(friendUrl)
        for j in range(1,101):
            try:
                address = driver.find_element_by_xpath("//*[@id='friends_box_list']/div["+str(j)+"]/div/ul[2]/li[2]").text
                if address == 'New York, NY':
                    friendLink = driver.find_element_by_xpath("//*[@id='friends_box_list']/div["+str(j)+"]/div/div/a").get_attribute("href")
                    friendId = friendLink.split('=')[1]
                    friendList.append(friendId)
                    if friendId not in userSet:
                        userList.append(friendId)
                        userSet.add(friendId)
            except:
                pass
    return friendList

def write(userId, profile, reviews,friendList):
    f = open('D:/js/yelp/'+userId+'.txt','w')
    f.write(userId)
    f.write('\n')
    for i in profile:
        f.write(i)
        f.write('\n')
    f.write('==========================')
    for i in reviews:
        for j in i:
            f.write(j)
            f.write('|')
        f.write('\n')
    f.write('--------------------------')
    for i in friendList:
        f.write(i)
        f.write('\n')
    f.close()

def iterator():
    while len(userList) != 0:
        userId = userList.pop()
        #userSet.remove(userId)
        url = 'http://www.yelp.com/user_details?userid='+ userId
        profile, userId = singleUserProfileInfo(url)
        reviewsList = getReviewList(profile, userId)
        friendList = getFriendList(profile,userId)
        write(userId, profile, reviewsList,friendList)

if "__main__" == __name__:
    startUrl = 'http://www.yelp.com/user_details?userid=VLfsjhGO9vxw7lO5KGrJtw'  #http://www.yelp.com/user_details?userid=6s-g2vFu12OemhiK3FJuOQ
    profile, userId = singleUserProfileInfo(startUrl)
    reviewsList = getReviewList(profile, userId)
    friendList = getFriendList(profile,userId)
    write(userId, profile, reviewsList,friendList)
    iterator()