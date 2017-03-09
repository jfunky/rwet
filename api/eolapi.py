#by jasmine
#march 2017
#v 0.0.2
#rwet hw 5

#can we make more general so poems don't have to be about bees?
#it appears arguments can be animals but not plants, because not all
## api responses include a "description" field

import urllib
import random
import json
import sys

#list & dict init
all_names = list()
all_lines = list()
all_words = list()
long_words = list()
poem_dictionary = dict()

#hit search API
topic = sys.argv[1]
base_url1 = "http://eol.org/api/search/"
url1 = base_url1 + topic + ".json"

raw1 = urllib.urlopen(url1).read()
data1 = json.loads(raw1)

#get the first identifier
for item in data1["results"]:
  ID = str((item["id"]))
  break

#I am sorry for being lazy
base_url2 = "http://eol.org/api/pages/1.0.json?batch=false&id="
params = "&texts_page=1&iucn=false&subjects=overview&licenses=all&details=true&common_names=true&synonyms=false&references=false&taxonomy=false&vetted=0&cache_ttl=&language=en"
url = base_url2 + ID + params

raw = urllib.urlopen(url).read()
data = json.loads(raw)

# get all names & add to word list
all_names.append(data["scientificName"])

for name in data["vernacularNames"]:
  all_names.append(name["vernacularName"])

#get all the words from the descriptions and add to word list
for desc in data["dataObjects"]:
  words = desc["description"].split()
  for word in words:
    if ">" in word:
      ignore = word
    elif "&nbsp;" in word:
      ignore = word
    elif "&gt;" in word:
      ignore = word
    elif "http:" in word:
      ignore = word
    elif "<a" in word:
      ignore = word
    else:
      all_words.append(word)
  #print all_words
  #output = " ".join(all_words)
  #print output

# do this word length dictionary stuff again
for word in all_words:
    word_length = len(word)
    if word_length not in poem_dictionary:
        poem_dictionary.setdefault(word_length, []).append(word)
    else: 
        poem_dictionary[word_length].append(word)

#print poem_dictionary
#interesting
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]

#also create a list for very long words
for word in all_words:
    word_length = len(word)
    if word_length > 8:
        long_words.append(word)


#MAKE POEM
#i want my poem to look round
line1 = ["      ", random.choice(poem_dictionary[3])]
line2 = ["    ",random.choice(poem_dictionary[2]), random.choice(poem_dictionary[5]), random.choice(poem_dictionary[3])]
line3 = ["  ", random.choice(poem_dictionary[3]), random.choice(poem_dictionary[5]), random.choice(poem_dictionary[4])]
line4 = [random.choice(poem_dictionary[7]), random.choice(long_words),random.choice(poem_dictionary[6])]
line5 = ["  ",random.choice(all_names), random.choice(long_words)]
line6 = ["   ", random.choice(poem_dictionary[6]), random.choice(poem_dictionary[8])]
line6 = ["      ", random.choice(poem_dictionary[5]), random.choice(poem_dictionary[6])]
line7 = ["         ", random.choice(poem_dictionary[3]), random.choice(poem_dictionary[7])]
line8 = ["          ", random.choice(poem_dictionary[4])]


all_lines = [line1, line2, line3, line4, line5, line6, line7, line8]

#counter
x=0

for line in all_lines:
  if x%2 ==0:
    print " "
    print ' '.join(line)
  else:
    print ' '.join(line)
  x=x+1


