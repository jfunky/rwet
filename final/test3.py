#by jasmine
#april 2017
#v 0.0.3
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

#dictionaries & lists
elements = list()
nouns = list()
ads = list()
chinatxt = list()
usgstxt = list()

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
#print adtest

#get rare earths list & make a dictionary of products
with open('rare_earths.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        for i in row:
            nouns.append(row[0])
            nouns.append(row[1])
#print(elements)

# read ad text
#ad_str = open('ad_text.txt').read()
ad_unicode = unicode(ad_str)

pdf_unicode = unicode(chinatxt)

for i in ad_str.split():
    ads.append(i)

#spacy on strings
addoc = nlp(ad_unicode)
pdfdoc = nlp(pdf_unicode)

for item in pdfdoc.noun_chunks:
    nouns.append(item.text)

short_sentences = []
for sentence in addoc.sents:
    short_sentences.append(sentence.text)

for sentence in short_sentences:
    print sentence
    nlpsent = nlp(sentence)
    line = []
    for item in nlpsent:
        if item.pos_ == 'NOUN':
            item = random.choice(nouns)
            line.append(item)
    print ' '.join(line)
