import eventful
from config import *

# Create a config.py file with this structure:
#
# from collections import namedtuple
#
# config = namedtuple("config", "EVENTFUL_KEY")
# config.EVENTFUL_KEY = 'YOUR_EVENTFUL_API_KEY'
#
api = eventful.API(config.EVENTFUL_KEY)

# If you need to log in:
# api.login('username', 'password')

# Search for events with the following search criteria.
# Currently only prints.
# TODO: Save information to database to limit API calls.
#
events = api.call('/events/search', category='livemusic', l='Lawrence, KS', sort_order='date', page_size=100)

for event in events['events']['event']:
    print ("######### %s ##########" % event['venue_name'])
    print ("%s at %s \n\n" % (event['start_time'], event['title']))


#print(events);
# Search for events with the following search criteria.
# Currently only prints.
# TODO: Save information to database to limit API calls.
#

venues = api.call('/venues/search', l='66047', within=100, units='mi', page_size=15)
for venue in venues['venues']['venue']:
    print ("%s" % (venue['name']))

# Simply print search categories and they're IDs. Mostly for experimenting.
# Currently only prints.
categories = api.call('/categories/list')
for category in categories['category']:
    print ("%s  : ID - %s" % (category['name'], category['id']))

