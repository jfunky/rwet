import random
import pronouncing

#adapted from stack overflow
#https://stackoverflow.com/questions/17865563/capitalise-every-other-letter-in-a-string-in-python
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

#adapted from allison parrish's class example
#https://pronouncing.readthedocs.io/en/latest/tutorial.html
def rhymingLine(w):
    out = list()
    for word in w.split():
        rhymes = pronouncing.rhymes(word)
    if len(rhymes) > 0:
        out.append(random.choice(rhymes))
    else:
        out.append(word)
    return ' '.join(out)

#function that replaces one char with another char
def replaceOne(s, old=",", new=""):
    return s.replace(old, new)

#function that replaces a list
#specifically want for punctuation
def replaceList(s, rList=[",","."], repl=""):
    #create currentString, which we will modify
    currentString = s
    #loop through list and call replace function
    for element in rList:
        currentString = replaceOne(currentString, element, repl)
    return currentString

#make a list of 2 screen names
def screenName(s):
    sn_word = []
    sn_numb = []
    #I don't know how to cycle through this in a mutually exclusive way?
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for element in s:
        #don't include $ in screen names
        element.replace("$", "")
        #screen name numbers
        if "1" in element:
            sn_numb.append(element)
        elif "2" in element:
            sn_numb.append(element)
        elif "3" in element:
            sn_numb.append(element)
        elif "4" in element:
            sn_numb.append(element)
        elif "5" in element:
            sn_numb.append(element)
        elif "6" in element:
            sn_numb.append(element)
        elif "7" in element:
            sn_numb.append(element)
        elif "8" in element:
            sn_numb.append(element)
        elif "9" in element:
            sn_numb.append(element)
        elif "0" in element:
            sn_numb.append(element)
        else:
            #screen name words
            if len(element) > 3 and len(element) < 8:
                sn_word.append(aimCase(element))

    sn1 = ''.join([random.choice(sn_word), random.choice(sn_word), random.choice(sn_numb)])
    sn2 = ''.join([random.choice(sn_word), random.choice(sn_numb), random.choice(sn_word)])

    screen_names = [sn1, sn2]
    return screen_names

#create a list of 3 random lines
def pick3(s):
    lines = []
    for line in s.split('.'):
        remove = ["[","]","-","(",")"]
        line = replaceList(line,remove)
        line1 = line.split(",")
        lines.append(line)

    return random.sample(lines,3)

#print the conversation
def printConv(snList, textList, wordsList):
    line1 = [snList[0], "(5:31:09 PM): sup ;)"]
    line2 = [snList[1], "(5:31:49 PM):", textList[0]]
    line3 = [snList[0], "(5:32:15 PM):", random.choice(wordsList), random.choice(wordsList), rhymingLine(textList[0])]
    line4 = [snList[1], "(5:31:49 PM):", textList[1]]
    line5 = [snList[0], "(5:32:15 PM):", random.choice(wordsList), rhymingLine(textList[1])]
    line6 = [snList[1], "(5:31:49 PM):", random.choice(wordsList), random.choice(wordsList), rhymingLine(textList[1])]
    line7 = [snList[0], "(5:32:15 PM):", textList[2]]
    line8 = [snList[0], "(5:32:15 PM):", random.choice(wordsList), random.choice(wordsList), rhymingLine(textList[2])]
    line9 = [snList[1], "(5:32:42 PM): ;)"]
    line10 = [snList[0], "(5:32:44 PM): <3"]

    all_lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]

    #print poem
    for line in all_lines:
        #when I try return here it only prints the first line?
        print ' '.join(line)

def wordList(s):
    # create empty lists
    words = []
    # iterate over each word
    # pick some words
    for word in s.split():
        remove = [",",".","[","]",";",":","-","(",")","'"]
        word = replaceList(word,remove)
        #all words
        words.append(word)
    return words

def createPoem(instr):
    #make word list & lines
    words = wordList(instr)
    textLines = pick3(instr)
    #make screen names from words
    sn = screenName(words)
    #print poem
    printConv(sn, textLines, words)
