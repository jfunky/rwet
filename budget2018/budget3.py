#by jasmine
#april 2017
#rwet hw 8

import pyPdf
import markov

#learned about comparing dictionaries from:
#https://stackoverflow.com/questions/4527942/comparing-two-dictionaries-in-python
def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return same

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
model_budget = markov.build_model(budgetWords, 3)
generated_budget = markov.generate(model_budget, 2)

#return generative text based off of the parks dept manual
model_park = markov.build_model(park_str.split(), 3)
generated_park = markov.generate(model_park, 2)

# combine based on what these texts have in common
combined = dict_compare(model_budget, model_park)

for element in combined:
    print ' '.join(element)
    print ' '.join(generated_budget)
    print ' '.join(generated_park)
