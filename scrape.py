import scraper
import requests
import time
import re
import string
import urllib2
from lxml import html

# Dependencies:
# sudo apt-get install python-qt4

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()
"""
#### Granada Info ####

granadaWebsite = requests.get('https://thegranada.com').content

print("\n\n#########################   The Granada   #########################\n\n")

for i in range(0,15) :
    artist = "//div[4]/div[2]/div[1]/div[1]/div[{}]/div[2]/div[1]/div[1]/h2/a".format(str(i+2))
    date = "//div[4]/div[2]/div[1]/div[1]/div[{}]/div[2]/div[1]/div[2]".format(str(i+2))
    artist = { 'Artist' : { 'xpath' : artist } }
    date = {'Date' : { 'xpath' : date } }
    artist = scraper.scrapes(granadaWebsite,artist)
    date = scraper.scrapes(granadaWebsite,date)
    artist = str(artist['Artist']).strip("[']")
    date = str(date['Date']).strip("[']")
    if(artist):
        print("{}\n{}".format(artist, date))
        print

print('\n\n')

"""
for i in range(1,5):
    time.sleep(1)

print

"""


#### The Bottleneck Info ####

print("\n\n#########################   The Bottleneck   #########################\n\n")

bottleneckWebsite = requests.get('http://thebottlenecklive.com').content

for i in range(0,10):
    artist = '//*[@id="content"]/div[{}]/div[3]/a/h4'.format(str(i))
    dayName = '//*[@id="content"]/div[{}]/div[1]/h6[3]'.format(str(i))
    month = '//*[@id="content"]/div[{}]/div[1]/h6[1]'.format(str(i))
    dayNum = '//*[@id="content"]/div[{}]/div[1]/h6[2]'.format(str(i))
    artist = { 'Artist' : { 'xpath' : artist } }
    dayName = { 'Day Name' : { 'xpath' : dayName } }
    dayNum = { 'Day Num' : { 'xpath' : dayNum } }
    month = { 'Month' : { 'xpath' : month } }
    artist = scraper.scrapes(bottleneckWebsite, artist)
    dayName = scraper.scrapes(bottleneckWebsite, dayName)
    month = scraper.scrapes(bottleneckWebsite, month)
    dayNum = scraper.scrapes(bottleneckWebsite, dayNum)
    artist = str(artist['Artist']).strip("[']")
    dayName = str(dayName['Day Name']).strip("[']")
    month = str(month['Month']).strip("[']")
    dayNum = str(dayNum['Day Num']).strip("[']")
    if(artist):
        print("{}\n{}, {} {}".format(artist, dayName, month, dayNum))
        print
print("\n\n")


#### Liberty Hall Info ####

libertyHall = requests.get('http://libertyhall.net/events').content

print("\n\n#########################    Liberty Hall   #########################\n\n")

for i in range(1, 10):
    artist = '/html/body/div[2]/div/div/div[{}]/div[3]/div/h5/a'.format(str(i))
    artist = { 'Artist' : { 'xpath' : artist } }
    artist = scraper.scrapes(libertyHall, artist)
    artist = str(artist['Artist']).strip("[']")
    artist = artist.lower().title()
    date = '/html/body/div[2]/div/div/div[{}]/div[3]/div/p[1]'.format(str(i))
    date = { 'Date' : { 'xpath' : date } }
    date = scraper.scrapes(libertyHall, date)
    date = str(date['Date']).strip("[']")

    if(artist):
        print("{}\n{}".format(artist, date))
        print


print("\n\n")



#### Liberty Hall Info ####

jackpot = requests.get('http://www.jackpotlawrence.com/events/list').content

print("\n\n#########################    The Jackpot   #########################\n\n")

for i in range(1, 10):
    artist = '//*[@id="tribe-events-content"]/div[3]/div[{}]/div[1]/div[1]/div[1]/h3/a'.format(str(i))
    artist = { 'Artist' : { 'xpath' : artist } }
    artist = scraper.scrapes(jackpot, artist)
    artist = str(artist['Artist']).strip("[']")
    artist = artist.replace('\\n', '')
    artist = artist.replace('\u2019', "'")
    artist = artist.strip("u'")
    artist = artist.replace('\\t','')
    artist = artist.replace('at The Jackpot', '')
    artist = artist.replace('at Jackpot', '')
    artist = artist.replace('Bar/Jackpot/Ingredient', '')
    date = '//*[@id="tribe-events-content"]/div[3]/div[{}]/div[1]/div[2]/div[1]/div[1]/div[1]/span'.format(str(i))
    date = { 'Date' : { 'xpath' : date } }
    date = scraper.scrapes(jackpot, date)
    date = str(date['Date']).strip("[']")
    date = date.split('@')
    date = date[0]
    if(artist):
        print("{}\n{}".format(artist, date))#, date))
        print









#### Liberty Hall Info ####

crossroads = requests.get('http://www.crossroadskc.com/').content

print("\n\n#########################    Crossroads KC   #########################\n\n")

for i in range(2, 12):
    artist = '//*[@id="midcontent"]/div[{}]/div[3]/p[1]/a[1]'.format(str(i))
    artist = { 'Artist' : { 'xpath' : artist } }
    artist = scraper.scrapes(crossroads, artist)
    artist = str(artist['Artist']).strip("[']")
    dayName = '//*[@id="midcontent"]/div[{}]/div[1]/h6[3]'.format(str(i))
    dayName = { 'Day Name' : { 'xpath' : dayName } }
    dayName = scraper.scrapes(crossroads, dayName)
    dayName = str(dayName['Day Name']).strip("[']")
    month = '//*[@id="midcontent"]/div[{}]/div[1]/h6[1]'.format(str(i))
    month = { 'Month' : { 'xpath' : month } }
    month = scraper.scrapes(crossroads, month)
    month = str(month['Month']).strip("[']")
    dayNum = '//*[@id="midcontent"]/div[{}]/div[1]/h6[2]'.format(str(i))
    dayNum = { 'Day Num' : { 'xpath' : dayNum } }
    dayNum = scraper.scrapes(crossroads, dayNum)
    dayNum = str(dayNum['Day Num']).strip("[']")
    date = "{}, {} {}".format(dayName, month, dayNum)
    if(artist):
        print("{}\n{}".format(artist, date))
        print


"""

















#### The Uptown  Info ####

# Original website:
# http://www.ticketofficesales.com/venue/uptown-theater-kansas-city-tickets-
# for-sale.aspx?&mkwid=s8dsPJ9Lp|pcrid|141649744496|pkw|uptown%20theatre%20
# events|pmt|b|pdv|c|&st-t=google&vt-k=uptown%20theatre%20events&gclid=CjwKEAj
# wzKPGBRCS55Oe46q9hCkSJAAMvVuMyNTA6e5YCHRv6NVSQC14lFeqSDE256OB2jUfe9kI_BoCiVX
# w_wcB

print("\n\n#########################    The Uptown   #########################\n\n")


uptown = 'https://tinyurl.com/juwa9gr'
uptown = 'http://www.uptowntheater.com/calendar.html'

r = Render(uptown)
#result is a QString.
result = r.frame.toHtml()

formatted_result = str(result.toAscii())

tree = html.fromstring(formatted_result)
archive_links = tree.xpath('//*[@id="avn0"]/a/text()')
print archive_links

#archive_links = tree.xpath('//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[2]/@class')
for i in range(1, 10):
    artist = '//*[@id="avn{}"]/a'.format(str(i))
    artist = { 'Artist' : { 'xpath' : artist } }
    print artist
    artist = scraper.scrapes(tree, artist)
    print artist
    artist = str(artist['Artist']).strip("[']")
    print artist
    """
    date = '//*[@id="tribe-events-content"]/div[3]/div[{}]/div[1]/div[2]/div[1]/div[1]/div[1]/span'.format(str(i))
    date = { 'Date' : { 'xpath' : date } }
    date = scraper.scrapes(jackpot, date)
    date = str(date['Date']).strip("[']")
    date = date.split('@')
    date = date[0]
"""
    if(artist):
        print("{}\n".format(artist))#, date))
        print
