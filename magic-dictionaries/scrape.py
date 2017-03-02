#by jasmine
#march 2017
#v 0.0.1
#take mtg multiverseid as argument(s) and creates dictionary
#right now all this does is get the html :)

import urllib2
import sys

#set url
mtg = "http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid="
card = sys.argv[1] 
url = mtg + card 
#check type
#print type(card)

page = urllib2.urlopen(url)
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(page)
#soup = BeautifulSoup(page, 'html.parser')

#print(soup.get_text())
