# Lawrence-Live-Music-Scraper
Scrape the webz and find upcoming showz.

#### Lawrence
- ~~The Granada~~
- ~~The Bottleneck~~
- ~~Liberty Hall~~
- ~~Jackpot~~
- ~~Jazzhaus~~
- ~~The Replay~~
- ~~Taproom~~

#### Kansas City
- Crossroads
- The Midland
- The Uptown
- ~~The Riot Room~~

#### Scraper Source
__source__: https://github.com/fjavieralba/scraper

## Setup
Dependencies:
- sudo apt-get install python-qt4 (I've had quite a few issues with installing)
- pip install lxml
- Download and Install Eventful API:
__source__: http://api.eventful.com/libs/python/

```
Download

eventfulpy-0.3.tar.gz
Installation

python setup.py install should do the trick.
Requirements

eventful.py requires simplejson and httplib2.

pip install simplejson
pip install httplib2
```

- Create Config files (not needed if just using scrape.py for cml use)

```
# Create a config.py file with this structure:
from collections import namedtuple

config = namedtuple("config", "EVENTFUL_KEY") #Do not replace EVENTFUL_KEY
config.EVENTFUL_KEY = 'YOUR_EVENTFUL_API_KEY'
```

```
# Create a config.js file with this structure:

var config = {
        PLACES_KEY : 'YOUR_GOOGLE_PLACES_API_KEY'
}

var script = document.createElement('script');
script.src = "https://maps.googleapis.com/maps/api/js?key=" + config.PLACES_KEY + "&libraries=places&callback=getLocation";
document.body.appendChild(script);
```
