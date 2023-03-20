from requests_html import HTMLSession
from random import *
import webbrowser
#########################################################
k = randint(1,250)
#########################################################
session = HTMLSession()
r = session.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
selc = r.html.find('.lister-list > tr:nth-child('+str(k)+') > td:nth-child(2) > a:nth-child(1)',first=True)
name = selc.text
link = list(selc.absolute_links)[0]
r1 = session.get(link)
duration = r1.html.find('ul.ipc-inline-list:nth-child(2) > li:nth-child(3)',first=True).text
#rate = r1.html.find('.sc-80d4314-3 > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)',first=True).text
s_name = name.replace(' ' ,'-')
date  = r1.html.find('ul.ipc-inline-list:nth-child(2) > li:nth-child(1) > a:nth-child(1)',first=True).text
sujet = r1.html.find(".sc-35061649-0",first=True).text
director = r1.html.find('.sc-eda143c4-3 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)',first=True).text
##########################################################
print('Name :',name)
print('Duration :' , duration)
#print('Rate :',rate+'/10')
print('Year :' , date)
print('Spoiling XD :' , sujet)
print('Director :' , director)
##########################################################
url = 'https://1movieshd.com/search/'
url+=s_name
##########################################################
ok = False
while not(ok) :
    prompt = input('You wanna watch the movie Y/N : ')
    ok = prompt =='Y' or prompt =='N' or prompt =='n' or prompt =='y'

if prompt == 'Y' or prompt == 'y'  :
    webbrowser.open(url)
    
else :
    print('enjoy your time  ')
# still under maintance we'll finish it  ASAP #