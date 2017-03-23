#by jasmine
#march 2017
#v 0.0.1

#import sys
import pronouncing
import random

# read in text
input_str = open('SequoiaNatPark.txt').read()

# create empty lists
words = []
lines = []
sn = []
numbers = []

#counter
x=0

#final poem
all_lines = []

def aimCase(w):
    wordout = ""
    i = True  # capitalize
    for char in w:
        if i:
            wordout += char.lower()
        else:
            wordout += char.upper()
        if char != ' ':
            i = not i
    return wordout

def rhymingLine(w):
    out = list()
    for word in w.split():
        rhymes = pronouncing.rhymes(word)
    if len(rhymes) > 0:
        out.append(random.choice(rhymes))
    else:
        out.append(word)
    return ' '.join(out)

# iterate over each word in mushrooms
# pick some words
for word in input_str.split():
    #remove punctuation
    #there has to be a better way to do this
    word1 = word.replace(",", "")
    word2 = word1.replace(".", "")
    word3 = word2.replace("]", "")
    word4 = word3.replace("[", "")
    word5 = word4.replace(";", "")
    word6 = word5.replace("-", "")
    word7 = word6.replace(")", "")
    word8 = word7.replace("(", "")
    word9 = word8.replace("'", "")
    if "1" in word:
        numbers.append(word9)
    elif "2" in word:
        numbers.append(word9)
    elif "3" in word:
        numbers.append(word9)
    elif "4" in word:
        numbers.append(word9)
    elif "5" in word:
        numbers.append(word9)
    elif "6" in word:
        numbers.append(word9)
    elif "7" in word:
        numbers.append(word9)
    elif "8" in word:
        numbers.append(word9)
    elif "9" in word:
        numbers.append(word9)
    elif "0" in word:
        numbers.append(word9)
    else:
        #screen names
        if len(word6) > 3 and len(word6) < 8:
            sn.append(aimCase(word9))
        #all words
        words.append(word9)

for word in input_str.split():
    #remove punctuation
    word1 = word.replace(",", "")
    word2 = word1.replace(".", "")
    word3 = word2.replace("]", "")
    word4 = word3.replace("[", "")
    word5 = word4.replace(";", "")
    word6 = word5.replace("-", "")
    if "1" in word:
        numbers.append(word6)
    elif "2" in word:
        numbers.append(word6)
    elif "3" in word:
        numbers.append(word6)
    elif "4" in word:
        numbers.append(word6)
    elif "5" in word:
        numbers.append(word6)
    elif "6" in word:
        numbers.append(word6)
    elif "7" in word:
        numbers.append(word6)
    elif "8" in word:
        numbers.append(word6)
    elif "9" in word:
        numbers.append(word6)
    elif "0" in word:
        numbers.append(word6)
    else:
        #screen names
        if len(word6) > 3 and len(word6) < 8:
            sn.append(aimCase(word6))
        #all words
        words.append(word6)

#split lines
for line in input_str.split('.'):
    line1 = line.split(",")
    lines.append(line1)


#make "screen names"
sn1 = ''.join([random.choice(sn), random.choice(sn), random.choice(numbers)])
sn2 = ''.join([random.choice(sn), random.choice(numbers), random.choice(sn)])

#conversation text
text1  = ' '.join(random.choice(lines))
rhyme1 = rhymingLine(text1)
text2  = ' '.join(random.choice(lines))
rhyme2a = rhymingLine(text2)
rhyme2b = rhymingLine(text2)
text3  = ' '.join(random.choice(lines))
rhyme3 = rhymingLine(text3)


#MAKE AIM CONVERSATION POEM
line1 = [sn1, "(5:31:09 PM): sup ;)"]
line2 = [sn2, "(5:31:49 PM):", text1]
line3 = [sn1, "(5:32:15 PM):", random.choice(words), random.choice(words), rhyme1]
line4 = [sn2, "(5:31:49 PM):", text2]
line5 = [sn1, "(5:32:15 PM):", random.choice(words), rhyme2a]
line6 = [sn2, "(5:31:49 PM):", random.choice(words), random.choice(words), rhyme2b]
line7 = [sn1, "(5:32:15 PM):", text3]
line8 = [sn1, "(5:32:15 PM):", random.choice(words), random.choice(words), rhyme3]
line9 = [sn2, "(5:32:42 PM): ;)"]
line10 = [sn1, "(5:32:44 PM): <3"]

all_lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]

#print poem
for line in all_lines:
    print ' '.join(line)
