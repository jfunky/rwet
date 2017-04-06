#by jasmine
#april 2017
#v 0.0.2
#rwet hw 8

import pyPdf
import markov

#learned about pyPdf from:
#https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text?noredirect=1&lq=1
pdf = pyPdf.PdfFileReader(open("2018_blueprint.pdf", "rb"))

budgetWords = list()
budgetLines = list()
parkLines = list()
allWords = list()

#split budget lines & create word list
for page in pdf.pages:
    string = page.extractText()
    # line = string.split(".")
    line = string.replace(".","\n")
    # print line
    if len(line) > 0:
        budgetLines.append(line)
        for word in line.split():
            if len(word) > 0:
                budgetWords.append(word)
                allWords.append(word)

# read in text
park_str = open('SequoiaNatPark.txt').read()

#split park lines
for line in park_str.split("."):
    # line1 = line.split(" ")
    line1 = line.replace(".","\n")
    parkLines.append(line1)
    for word in line1.split():
        if len(word) > 0:
            allWords.append(word)

#markov stuff
#return generative text based off of the 2018 budget
model_budget = markov.build_model(budgetWords, 2)
generated_budget = markov.generate(model_budget, 2)
print "budget"
print ' '.join(generated_budget)

#return generative text based off of the parks dept manual
model_park = markov.build_model(park_str.split(), 2)
generated_park = markov.generate(model_park, 2)
print "park"
print ' '.join(generated_park)

#try combining both texts and creating a model
model_combined = markov.build_model(allWords, 2)
generated_combined = markov.generate(model_combined, 2)
print "combined"
print ' '.join(generated_combined)
