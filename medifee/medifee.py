from bs4 import BeautifulSoup
import urllib
from ordered_set import OrderedSet
import cPickle as pickle
import pandas as pd

id = 1
name = []
phone = []
url = "http://www.medifee.com/dc-in-new-delhi"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html5lib")
#atags = soup.find_all("h2", {"class": 'forumtitle'})
body = soup.find_all("td")

err = None
address = []
for td in body:
    try:
        if td.find("a"):
            err = True
            name.append(td.a.text.decode('utf-8'))
            address.append(td.br.nextSibling.decode('utf-8'))
            links ='http://www.medifee.com'+str(td.a['href'].decode('utf-8'))
            print 'name --',td.a.string,'>>>links --','http://www.medifee.com'+str(td.a['href']),'>>>ad--',td.br.nextSibling

            with open('links.txt', 'a') as f:
                f.write(links)
                f.write('\n')

        else:
            if err:
                print td.string
                phone.append(td.string)


    except Exception as e:
        print e
        err = False
        pass

print len(name),len(phone),len(address)
centers = {'Name':name, 'Phone':phone,'Address':address}
df = pd.DataFrame(centers)
df.to_csv('Diagnostic Centers in Delhi.txt',sep='|')


#==============

c =-1
f = open('links.txt','rb')

for url in f:
    print url
    c += 1
    name = []
    price = []
    offer = []
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html5lib")
    body = soup.find_all("td")
    if len(body)>0:
        for i in range(0,len(body),3):
            name.append(body[i].string.encode('utf-8'))
            price.append(body[i+1].string.encode('utf-8'))
            offer.append(body[i+2].string)
            #print body[i].string , '--name'
            #print body[i+1].string,'--price'
            #print body[i+2].string,'--offer'
            #print '==='*30
        d = {'Name': name, 'Price': price, 'Offer': offer}
        df = pd.DataFrame(d)
        df.to_csv(str(c) + '.txt', sep='|')

        print c












