__author__ = 'haistill'

import store_ult,store_info
#Hell's Kitchen

if "__main__" == __name__:
    yelp = open('D:/js/googleM/yelp.txt').readlines()
    for l in yelp:
        l = l.strip('\n')
        if ' 'in l:
            l = l.replace(' ','_')
        print l
        store_ult.store_ult(l)
        store_info.store_info(l)





