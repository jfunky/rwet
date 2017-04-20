from __future__ import unicode_literals
import spacy
import random
import markov
import pyPdf

#load english
nlp = spacy.load('en')

#out must be an already defined list
#incr must be an already defined number variable
def pdfpages(p, start, end, out):
    n = 0
    for page in p.pages:
        if n > start and n < end:
            string = page.extractText()
            line = string.replace(".","\n")
            line2 = string.replace("''"," ")
            if len(line2) > 0:
                out.append(line2)
                for word in line2.split():
                    if len(word) > 0:
                        out.append(word)
        n = n + 1

def sourcesent(s, n, txtin):
    #random places & nouns
    poem = []
    for i in range(3):
        poem.append(random.choice(s))
        poem.append(random.choice(n))

    #sentences from ads
    ad_sentences = []
    for sentence in txtin.sents:
        ad_sentences.append(sentence.text)

    #append all words
    for sentence in ad_sentences:
        for word in sentence.split(" "):
            poem.append(word)
        nlpsent = nlp(sentence)
        for item in nlpsent:
            if item.pos_ == 'NOUN':
                poem.append(random.choice(n))
            else:
                poem.append(item.text.strip())
    #output text
    return " ".join(poem)
