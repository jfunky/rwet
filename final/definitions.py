from __future__ import unicode_literals
import spacy
import random
import markov
import pyPdf

#load english
nlp = spacy.load('en')

#incr must be an already defined number variable
def pdfpages(p, start, end):
    n = 0
    for page in p.pages:
        if n > start and n < end:
            string = page.extractText()
            string += string
        n = n + 1
    return string

def sourcesent(s, n, txtin):

    #markov chain stuff with the ads
    admodel = markov.build_model(txtin, 4)
    txtin = ''.join(markov.generate(admodel, 4))

    # read ad text
    ad_unicode = unicode(txtin)

    #spacy on strings
    addoc = nlp(ad_unicode)

    #little poem
    poem = []

    #sentences from ads
    ad_sentences = []
    for sentence in addoc.sents:
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
