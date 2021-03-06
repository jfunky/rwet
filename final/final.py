#by jasmine
#april 2017
#v 0.0.5
#final

#code to create a dictionary from csv
#from https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
from __future__ import unicode_literals
import spacy
import codecs
import csv
import random
import markov
import pyPdf
import definitions

#load english
nlp = spacy.load('en')

#lists
nouns = list()
ads = list()
usgstxt = list()
sources = list()
rare_earth = list()

#get pdf pages
#only want pages with relevant info (not title pages, etc)
#create word list
chinapdf = pyPdf.PdfFileReader(open("china_rare_earths.pdf", "rb"))
pdf_unicode = definitions.pdfpages(p=chinapdf, start=3, end=13)

# read ad texts
ad_str = open('ad_text.txt').read()
wired_str = open('wired.txt').read()
for i in ad_str.split():
    ads.append(i)
for j in wired_str.split():
    ads.append(j)

#get rare earths list
with open('rare_earths.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        for i in row:
            nouns.append(row[0])
            nouns.append(row[1])
            rare_earth.append(row[0])
            rare_earth.append(row[1])

#read ad text
for i in ad_str.split():
    ads.append(i)

#spacy on the pdf text
pdfdoc = nlp(pdf_unicode)

for item in pdfdoc.ents:
    if item.label_ == 'GPE':
        sources.append(item.text.strip())
    elif item.label_ == 'ORG':
        sources.append(item.text.strip())

for item in pdfdoc.noun_chunks:
    nouns.append(item.text.strip())


#make a function so I can call it a lot if I feel like it
p1 = definitions.sourcesent(s=sources, n=nouns, txtin=ad_str)
p2 = definitions.sourcesent(s=sources, n=nouns, txtin=ad_str)
p3 = definitions.sourcesent(s=sources, n=nouns, txtin=ad_str)

#create a long list with the words in all poems
all_words = []
for word in p1.split():
    if word == "rare-earth":
        word = word.replace("rare-earth",random.choice(rare_earth))
    all_words.append(word)
for word in p2.split():
    if word == "rare-earth":
        word = word.replace("rare-earth",random.choice(rare_earth))
    all_words.append(word)
for word in p3.split():
    if word == "rare-earth":
        word = word.replace("rare-earth",random.choice(rare_earth))
    all_words.append(word)


#construct & print poem
n=1
x=1
whitespace = ""
while n < len(all_words):
    if n == 1:
        print " ".join(all_words[n-x:n])
        n = n + (2*x)
        x = x + (1*x)
        print " ".join(all_words[n-x:n])
        print " "
    else:
        n = n + (2*x)
        x = x + (1*x)
        print whitespace, " ".join(all_words[n-x:n])
        whitespace = whitespace + "   "
