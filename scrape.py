from libs import scraper
import requests
import time
import string
from lxml import html
from requests.exceptions import HTTPError
import subprocess
import sys

'''
Dependencies:
> sudo apt-get install python-qt4
> pip install lxml
'''


print("\n\n#########################"),
print ("   Processing   "),
print ("#########################\n\n")

toolbar_width = 65

# setup toolbar
sys.stdout.write("[0-%s-100]" % ("-" * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+4)) # return to start of line, after '['
'''
for i in xrange(toolbar_width - 2):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write('*')
    sys.stdout.flush()

sys.stdout.write("\n")
'''
'''
#### Get HTML from venue websites ####

## Save JS generated HTML to htmlList ##
#   Opens urljsrender.py and runs.
#   Had to do it this way because Render() would only render one request
#   per program execute.
#
#   TODO : Figure out a way to render multiple websites w/o use of secondary
#          process.
'''

htmlList = ['']*2
numWebsites = 7;
numColumns = 65;
percentDone = numColumns / numWebsites
exception = ''


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) ' \
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


try :
    rMidland = requests.get('http://midlandkc.com/events', headers = headers, timeout=20)
    rMidland.raise_for_status()
    cmd = 'python urljsrender.py http://www.midlandkc.com/events'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    htmlList[0] = out
except Exception as e :
    exception = exception + '\nError processing Midland.\n{}\n'.format(e)
for i in xrange(percentDone):
    time.sleep(0.1)
    sys.stdout.write('*')
    sys.stdout.flush()


try :
    rUptown = requests.get('http://www.uptowntheater.com/calendar.html', headers = headers, timeout = 20)
        #headers=headers, timeout=20)}
    rUptown.raise_for_status()
    cmd = 'python urljsrender.py http://www.uptowntheater.com/calendar.html'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    htmlList[1] = out
    #print('{}'.format('.' * (numColumns / numWebsites))),
    #print('Uptown successful\n')
except Exception as e :
    exception = exception + '\nError processing Uptown Theater' \
                                '/calendar.html.\n{}\n'.format(e)
for i in xrange(percentDone):
    time.sleep(0.1)
    sys.stdout.write('*')
    sys.stdout.flush()





'''
Save static html to approptriate variable
'''
try :
    rCrossroads = requests.get('http://www.crossroadskc.com/', headers = headers, timeout = 20)
        #headers=headers, timeout=20)}
    crossroads = rCrossroads.content
    rCrossroads.raise_for_status()
except Exception as e:
    exception = exception + '\nError processing Crossroads.\n{}\n'.format(e)
for i in xrange(percentDone):
    time.sleep(0.1)
    sys.stdout.write('*')
    sys.stdout.flush()


try :
    rGranada = requests.get('https://thegranada.com', headers = headers, timeout = 20)
    granadaWebsite = rGranada.content
    rGranada.raise_for_status()
except Exception as e:
    exception = exception + '\nError processing Granada.\n{}\n'.format(e)
for i in xrange(percentDone):
    time.sleep(0.1)
    sys.stdout.write('*')
    sys.stdout.flush()


try :
    rBottleneck = requests.get('http://thebottlenecklive.com', headers = headers, timeout = 20)
    bottleneckWebsite = rBottleneck.content
    rBottleneck.raise_for_status()
except Exception as e:
    exception = exception + '\nError processing Bottleneck.\n{}\n'.format(e)
for i in xrange(percentDone):
    time.sleep(0.1)
    sys.stdout.write('*')
    sys.stdout.flush()


try :
    rLibertyHall = requests.get('http://libertyhall.net/events', headers = headers, timeout = 20)
    libertyHall = rLibertyHall.content
    rLibertyHall.raise_for_status()
except Exception as e:
    exception = exception + '\nError processing Liberty Hall.\n{}\n'.format(e)
for i in xrange(percentDone):
    time.sleep(0.1)
    sys.stdout.write('*')
    sys.stdout.flush()


try :
    rJackpot = requests.get('http://www.jackpotlawrence.com/events/list', headers = headers, timeout = 20)
    jackpot = rJackpot.content
    rJackpot.raise_for_status()
except Exception as e :
    exception = exception + '\nError processing Jackpot.\n{}\n'.format(e)
for i in xrange(percentDone):
    time.sleep(0.1)
    sys.stdout.write('*')
    sys.stdout.flush()

sys.stdout.write("\n")

if(exception) :
    print exception
else :
    print '\nSuccess:\nNo errors on loading.\n'



###################
''' The Granada '''
###################

# url: https://thegranada.com

print("\n\n#########################"),
print ("   The Granada   "),
print ("#########################\n\n")

try :
    rGranada.raise_for_status()
    count = 1
    for i in range(0,15) :
        artist = "//div[4]/div[2]/div[1]/div[1]/div[{}]" \
                    "/div[2]/div[1]/div[1]/h2/a".format(str(i+2))
        date = ("//div[4]/div[2]/div[1]/div[1]/div[{}]" \
                    "/div[2]/div[1]/div[2]".format(str(i+2)))
        artist = { 'Artist' : { 'xpath' : artist } }
        date = {'Date' : { 'xpath' : date } }
        artist = scraper.scrapes(granadaWebsite,artist)
        date = scraper.scrapes(granadaWebsite,date)
        artist = str(artist['Artist']).strip("[']")
        date = str(date['Date']).strip("[']")
        if(artist and count <= 10):
            count += 1
            print("{}\n{}".format(artist, date))
            print
        elif(count == 10):
            break
except Exception as e:
    print ( 'Error in Granada.\n{}\n'.format(e) )
print('\n\n')





for i in range(0,10):                       # Sleep 10 seconds
    time.sleep(1)





######################
''' The Bottleneck '''
######################

print("\n\n#########################"),
print ("   The Bottleneck   "),
print ("#########################\n\n")

# url: http://thebottlenecklive.com

try :
    rBottleneck.raise_for_status()
    count = 1
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
        if(artist and count <= 10):
            count += 1
            print("{}\n{}, {} {}".format(artist, dayName, month, dayNum))
            print
        elif(count == 10):
            break
except :
    print ('Error in Bottleneck.\n{}\n'.format(e))
print("\n\n")





for i in range(0,10):                       # Sleep 10 seconds
    time.sleep(1)





#########################
''' Liberty Hall Info '''
#########################

# url: http://libertyhall.net/events

print("\n\n#########################"),
print ("    Liberty Hall   "),
print ("#########################\n\n")

try :
    rLibertyHall.raise_for_status()
    count = 1
    for i in range(1, 10):
        artist = '/html/body/div[2]/div/div/div[{}]' \
                    '/div[3]/div/h5/a'.format(str(i))
        artist = { 'Artist' : { 'xpath' : artist } }
        artist = scraper.scrapes(libertyHall, artist)
        artist = str(artist['Artist']).strip("[']")
        artist = artist.lower().title()
        date = '/html/body/div[2]/div/div/div[{}]' \
                    '/div[3]/div/p[1]'.format(str(i))
        date = { 'Date' : { 'xpath' : date } }
        date = scraper.scrapes(libertyHall, date)
        date = str(date['Date']).strip("[']")

        if(artist and count <= 10):
            count += 1
            print("{}\n{}".format(artist, date))
            print
        elif(count == 10):
            break
except :
    print ( 'Error in Liberty Hall.\n{}\n'.format(e) )
print("\n\n")





for i in range(0,10):                       # Sleep 10 seconds
    time.sleep(1)





#########################
''' Liberty Hall Info '''
#########################

# url: http://www.jackpotlawrence.com/events/list

print("\n\n#########################"),
print ("    The Jackpot   "),
print ("#########################\n\n")

try :
    rJackpot.raise_for_status()
    count = 1
    for i in range(1, 10):
        artist = '//*[@id="tribe-events-content"]/div[3]/div[{}]' \
                    '/div[1]/div[1]/div[1]/h3/a'.format(str(i))
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
        date = '//*[@id="tribe-events-content"]/div[3]/div[{}]' \
                '/div[1]/div[2]/div[1]/div[1]/div[1]/span'.format(str(i))
        date = { 'Date' : { 'xpath' : date } }
        date = scraper.scrapes(jackpot, date)
        date = str(date['Date']).strip("[']")
        date = date.split('@')
        date = date[0]
        if(artist and count <= 10):
            count += 1
            print("{}\n{}".format(artist, date))#, date))
            print
        elif(count == 10):
            break
except :
    print ( 'Error in Jackpot.\n{}\n'.format(e) )
print("\n\n")





for i in range(0,10):                       # Sleep 10 seconds
    time.sleep(1)





####################
''' CrossroadsKC '''
####################

# url: http://www.crossroadskc.com/

print ("\n\n#########################"),
print ("    Crossroads KC   "),
print ("#########################\n\n")

try :
    rCrossroads.raise_for_status()
    count = 1
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
        if(artist and count <= 10):
            count += 1
            print("{}\n{}".format(artist, date))
            print
        elif(count == 10):
            break
except :
    print ('Error in Crossroads.\n{}\n'.format(e))
print("\n\n")





for i in range(1,10):                       # Sleep 10 seconds
    time.sleep(1)





###################
''' The Midland '''
###################

print("\n\n#########################"),
print ("    Midland KC   "),
print ("#########################\n\n")



# url: http://www.midlandkc.com/events

try :
    rMidland.raise_for_status()
    formatted_result = htmlList[0]              # Get rendered html

    count = 1
    for i in range(1, 259):
        tempArtist = '//*[@id="eventsList"]/div[{}]' \
                        '/div[2]/div[1]/h3/a'.format(str(i))
        tempArtist = '//*[@id="eventsList"]/div[{}]' \
                        '/div[2]/div[1]/h3/a'.format(str(i))
        tempArtist = { 'Artist' : { 'xpath' : tempArtist } }
        tempArtist = scraper.scrapes(formatted_result, tempArtist)
        tempArtist = str(tempArtist['Artist']).strip("[']")
        tempArtist = tempArtist.replace('\\n', '')
        tempArtist = tempArtist.replace('\\t','')

        artist = tempArtist
        date = '//*[@id="eventsList"]/div[{}]' \
                '/div[2]/div[2]/span[1]/text()'.format(str(i))
        date = { 'Date' : { 'xpath' : date } }
        date = scraper.scrapes(formatted_result, date)
        date = str(date['Date']).strip("[']")
        date = date.replace('\\n', '')
        date = date.replace('\\t', '')
        date = date.replace("', '", '')
        support = '//*[@id="eventsList"]/div[{}]' \
                    '/div[2]/div[1]/h4'.format(str(i))
        support = { 'Support' : { 'xpath' : support } }
        support = scraper.scrapes(formatted_result, support)
        support = str(support['Support']).strip("[']")

        if(artist and count <= 10):             # If artist found, print
            count += 1
            if(support):
                print("{}\n{}\n{}".format(artist, support, date))
            else:
                print("{}\n{}".format(artist, date))
            print
        elif(count == 10):
            break
except :
    print ('Error in Midland.\n{}\n'.format(e) )
print("\n\n")





for i in range(1,10):                       # Sleep 10 seconds
    time.sleep(1)





##################
''' The Uptown '''
##################

print("\n\n#########################"),
print ("    The Uptown   "),
print ("#########################\n\n")

# url: http://www.uptowntheater.com/calendar.html

try :
    rUptown.raise_for_status()
    formatted_result = htmlList[1]              # Get the rendered html

    count = 1
    for i in range(1, 259):
        tempArtist = '//*[@id="id{}"]/div/div/p'.format(str(i))
        tempArtist = '//*[@id="id{}"]/div/div/p/a'.format(str(i))
        tempArtist = { 'Artist' : { 'xpath' : tempArtist } }
        tempArtist = scraper.scrapes(formatted_result, tempArtist)
        tempArtist = str(tempArtist['Artist']).strip("[']")

        if(tempArtist != 'RSVP' and             # Filter extraneous info
            tempArtist != 'HOME' and
            tempArtist != 'PRIVATE EVENTS' and
            tempArtist != 'CONTACT' and
            tempArtist != 'VIEW SEATING CHART' and
            tempArtist != 'CONCERT CALENDAR' and
            tempArtist != 'VIEW AUDIO SPECS' and
            tempArtist != 'CAREERS' and
            tempArtist != 'SEATING CHART' and
            tempArtist != 'CONTACT US' and
            tempArtist != 'FAQ' and
            tempArtist != 'VIEW NYE PHOTOS') :
            artist = tempArtist
            date = '//*[@id="id{}"]/div/div/p'.format(str(i + 1))
            date = { 'Date' : { 'xpath' : date } }
            date = scraper.scrapes(formatted_result, date)
            date = str(date['Date']).strip("[']")
            support = '//*[@id="id{}"]/div/div/p'.format(str(i+6))
            support = { 'Support' : { 'xpath' : support } }
            support = scraper.scrapes(formatted_result, support)
            support = str(support['Support']).strip("[']")

        else :
            tempArtist = ''


        if(artist and count <= 10):             # If artist found, print.
            count += 1
            if(support):
                print("{}\n{}\n{}".format(artist, support, date))
            else:
                print("{}\n{}".format(artist, date))
            print
        elif(count == 10):
            break
except :
    print ('Error in Uptown.\n{}\n'.format(e) )

print '\n\n'
