__author__ = 'haistill'
# -*- coding: utf-8 -*-
import simplejson as json
import os,unicodedata,string

def remove_accents(data):
    nkfd_form = unicodedata.normalize('NFKD', unicode(data))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

filePath='D:/js/googleM/result3/'

desfile='D:/js/googleM/result.txt'
fw = open(desfile,'a')
l = []
for filename in os.listdir(filePath):
    jsonobject = json.load(file(filePath+filename))
    result = jsonobject['results']
    for i in result:
        geometry = i['geometry']
        location = geometry['location']
        lat = location['lat']
        lng = location['lng']
        name = i['name']
        types = i['types']
        t = ''
        for j in types:
            t+=j+' '
        print str(lat),str(lng),name,t
        l.append(str(lat)+'|'+str(lng)+'|'+name+'|'+t)
for i in l:
    print i
    try:
        fw.write(remove_accents(i))
    except:
        continue
    fw.write('\n')
fw.close()
