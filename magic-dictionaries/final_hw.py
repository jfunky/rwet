#by jasmine
#march 2017
#v 0.0.4

#import sys
import random

# read in texts
mushrooms_str = open('mushroomRecipes.txt').read()
magic_str = open('ArtifactsEnchantments.txt').read()

# create empty dictionaries
magic_words = {}
mushroom_words = {}

#final poem
all_lines = []

# create arrays of words of different lengths
# mushroom text
for word in mushrooms_str.split():
    #remove parethesis, other punctuation doesn't bother me
    word_r1 = word.replace("[", " ")
    word_r2 = word_r1.replace("]", " ")
    word_r3 = word_r2.replace("(", " ")
    word_r4 = word_r3.replace(")", " ")
    word_length = len(word_r4)

    if word_length not in mushroom_words:
        #mushroom_words[word_length] = word_r4
        #need to use an array to append multiple words as values
        mushroom_words.setdefault(word_length, []).append(word_r4)
    else: 
        mushroom_words[word_length].append(word_r4)

#checks
#print mushroom_words.keys()
#print mushroom_words[9]
#cool


# create arrays of words of different lengths
# magic text
for word in magic_str.split():
    word_r1 = word.replace("\"", "")
    word_r2 = word_r1.replace("(", " ")
    word_r3 = word_r2.replace(")", " ")
    word_length = len(word_r3)

    if word_length not in magic_words:
        magic_words.setdefault(word_length, []).append(word_r3)
    else: 
        magic_words[word_length].append(word_r3)

#checks
#print magic_words.keys()
#print magic_words[7]
#cool

for i in range(10):
    if i % 2 == 0:
        first = random.choice(magic_words[4])
        second = random.choice(magic_words[2])
        third = random.choice(mushroom_words[3])
        fourth = random.choice(mushroom_words[6])
        fifth = random.choice(magic_words[2])
        sixth = random.choice(mushroom_words[5])
        line = [first, second, third, fourth, fifth, sixth]
        print ' '.join(line)
    elif i % 3 == 0:
        first = random.choice(mushroom_words[6])
        second = random.choice(magic_words[5])
        third = random.choice(mushroom_words[9])
        fourth = random.choice(mushroom_words[11])
        fifth = random.choice(magic_words[5])
        sixth = random.choice(magic_words[4])
        line = [first, second, third, fourth, fifth, sixth]
        print ' '.join(line)
    else:
        first = random.choice(mushroom_words[3])
        second = random.choice(magic_words[7])
        third = random.choice(magic_words[3])
        fourth = random.choice(mushroom_words[9])
        fifth = random.choice(magic_words[4])
        sixth = random.choice(mushroom_words[5])
        line = [first, second, third, fourth, fifth, sixth]
        print ' '.join(line)

