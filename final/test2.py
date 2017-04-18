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
elements = dict()
ads = list()
chinatxt = list()
usgstxt = list()

#get pdf pages
#only want pages with relevant info (not title pages, etc)
chinapdf = pyPdf.PdfFileReader(open("china_rare_earths.pdf", "rb"))
usgspdf = pyPdf.PdfFileReader(open("us_deposits.pdf", "rb"))

#split budget lines & create word list
definitions.pdfpages(p=chinapdf, start=3, end=13, out=chinatxt)
#definitions.pdfpages(p=usgspdf, start=7, end=29, out=usgstxt)

#get rare earths list & make a dictionary of products
with open('rare_earths.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        for i in row:
            k = row[0]
            v = row[1]
            elements = {k:v}
        #print(elements)

# read ad text
#ad_str = open('wired.txt').read()
ad_str = open('ad_text.txt').read()
ad_unicode = unicode(ad_str)

pdf_unicode = unicode(chinatxt)


for i in ad_str.split():
    ads.append(i)

#spacy on ad string
addoc = nlp(ad_unicode)
for word in addoc:
    print word.text, word.lemma_

pdfdoc = nlp(pdf_unicode)
print pdfdoc[0:20]
n = 0
for word in pdfdoc:
    n = n + 1
    if n < 10:
        print word.text, word.lemma_
