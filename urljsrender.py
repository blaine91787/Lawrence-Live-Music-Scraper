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
        self.frame = None
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()



r = Render(sys.argv[1])
#result is a QString.
result = r.frame.toHtml()



formatted_result = str(result.toAscii())

print formatted_result
