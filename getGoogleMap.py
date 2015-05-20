import urllib2,time

count =0
startLatitude = 40.70100
endLatitude = 40.87784
startLongitude1 = -74.01789
startLongitude2 = -73.980
endLongitude1 = -73.9275
endLongitude2 = -73.885

i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
                 "Referer": 'http://www.baidu.com'}

day=0

basex = startLatitude + (endLatitude - startLatitude)/4*day
basey1 = startLongitude1 + (endLongitude1 - startLongitude1)/4*day
basey2 = startLongitude2 + (endLongitude2 - startLongitude2)/4*day

for  i in range(25):
    x = basex + (endLatitude - startLatitude)/4/25*i
    j1 = basey1 + (endLongitude1 - startLongitude1)/4/25*i
    j2 = basey2 + (endLongitude2 - startLongitude2)/4/25*i
    for j in range(25):
        y = j1 + (j2 - j1)/25*j
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(x)+','+str(y)+'&radius=200&sensor=false&key=AIzaSyBPBrypsYwNvOJ2QHa8GWMw1ehDS-rye1Y'
        print count,url
        try:
            text = urllib2.urlopen(urllib2.Request(url,headers=i_headers)).read()
        except:
            continue
        f = open('D:/js/googleM/result'+str(day)+'/'+str(count)+'.txt','w')
        count+=1
        f.write(text)
        f.close()
        while 'next_page_token' in text:
            print count,'i have next page'
            lines = text.split('\n')
            l = lines[2].split(':')
            nextPage = l[1][2:len(l[1])-2]
            url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'+ nextPage + '&sensor=false&key=AIzaSyBPBrypsYwNvOJ2QHa8GWMw1ehDS-rye1Y'
            print count,url
            try:
                text = urllib2.urlopen(urllib2.Request(url,headers=i_headers)).read()
            except:
                continue
            f = open('D:/js/googleM/result'+str(day)+'/'+str(count)+'.txt','w')
            count+=1
            f.write(text)
            f.close()
        time.sleep(5)
