#by jasmine
#april 2017
#v 0.0.1
#rwet hw 8

import pyPdf
import markov

#learned about pyPdf from:
#https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text?noredirect=1&lq=1
pdf = pyPdf.PdfFileReader(open("2018_blueprint.pdf", "rb"))

lines = list()

for page in pdf.pages:
    string = page.extractText().strip()
    line = string.replace(".","\n")
    if len(line) > 0:
        lines.append(line)

print lines
# markov.word_level_generate(lines, 3, count=4)
markov.char_level_generate(lines, 3, count=4)
# print '\n'.join(markov.word_level_generate(lines, 2, count=2))
#print '\n'.join(markov.char_level_generate(lines, 6, count=8))
