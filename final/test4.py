#by jasmine
#april 2017
#v 0.0.4
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
chinatxt = list()
usgstxt = list()
sources = list()

#get pdf pages
#only want pages with relevant info (not title pages, etc)
#create word list
chinapdf = pyPdf.PdfFileReader(open("china_rare_earths.pdf", "rb"))
definitions.pdfpages(p=chinapdf, start=3, end=13, out=chinatxt)

# read ad text
ad_str = open('ad_text.txt').read()
for i in ad_str.split():
    ads.append(i)

#markov chain stuff with the ads
admodel = markov.build_model(ad_str, 4)
ad_str = ''.join(markov.generate(admodel, 4))


#get rare earths list & make a dictionary of products
with open('rare_earths.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        for i in row:
            nouns.append(row[0])
            nouns.append(row[1])

# read ad text
ad_unicode = unicode(ad_str)
pdf_unicode = unicode(chinatxt)

for i in ad_str.split():
    ads.append(i)

#spacy on strings
addoc = nlp(ad_unicode)
pdfdoc = nlp(pdf_unicode)

for item in pdfdoc.ents:
    if item.label_ == 'GPE':
        sources.append(item.text.strip())
    elif item.label_ == 'ORG':
        sources.append(item.text.strip())

for item in pdfdoc.noun_chunks:
    nouns.append(item.text.strip())

#make a function so I can call it a lot if I feel like it
p1 = definitions.sourcesent(s=sources, n=nouns, txtin=addoc)
p2 = definitions.sourcesent(s=sources, n=nouns, txtin=addoc)

all_words = []
for word in p1.split():
    all_words.append(word)
for word in p2.split():
    all_words.append(word)

#construct & print poem
n=1
x=1
while n < len(all_words):
    print " ".join(all_words[n-x:n])
    n = n + (2*x)
    x = x + (1*x)
