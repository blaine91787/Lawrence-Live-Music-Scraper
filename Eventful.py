import eventful
from config import *


api = eventful.API(config.EVENTFUL_KEY)

# If you need to log in:
# api.login('username', 'password')

events = api.call('/events/search', category='music && ', l='Kansas City, MO', sort_order='date')
for event in events['events']['event']:
    print "######### %s ##########" % event['venue_name']
    print "%s at %s \n\n" % (event['start_time'], event['title'])

venues = api.call('/venues/search', l='66047', within=100, units='mi', page_size=15)
for venue in venues['venues']['venue']:
    print "%s" % (venue['name'])


cats = api.call('/categories/list')
for cat in cats['category']:
    print "%s  : ID - %s" % (cat['name'], cat['id'])
