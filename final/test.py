#code to create a dictionary from csv
#from https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file

import csv
import random
import markov
import pyPdf
import definitions

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

#print chinatxt[0:10]
#print chinatxt[0]
#print string

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
ad_str = open('ad_text.txt').read()
#ad_str = open('wired.txt').read()
for i in ad_str.split():
    ads.append(i)

#ad part
admodel = markov.build_model(ad_str, 4)
#markov.generate(admodel, 3)
#print ''.join(markov.generate(model, 4))

#rare earth part
reemodel = markov.build_model(chinatxt, 3)
#markov.generate(reemodel, 2)
# model_REE = markov.build_model(chinatxt, 3)
# generated_REE = markov.generate(model_REE, 2)

#for now just pick random rare earths from the dictionary

#print poem
for i in range(8):
    print ''.join(markov.generate(admodel, 4))
    print ' '.join(markov.generate(reemodel, 2))


#####
# testing different markov options
#####

# NAH
# markov.char_level_generate(ads, 7, count=4)
# print ''.join(markov.char_level_generate(ad_str, 6, count=8))


# works pretty well !!
# #test markov stuff
# model = markov.build_model(ad_str.split(), 3)
# generated = markov.generate(model, 2)
#
# print ' '.join(generated)
