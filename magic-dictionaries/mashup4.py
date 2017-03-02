#by jasmine
#march 2017
#v 0.0.3

#import sys
import random

# read in texts
mushrooms_str = open('mushroomRecipes.txt').read()
magic_str = open('ArtifactsEnchantments.txt').read()

# create empty dictionaries
magic_words = {}
mushroom_words = {}

#final poem
all4keys = []
all_lines = []

# iterate over each word in mushrooms
# pick some words
for word in mushrooms_str.split():
    #remove parethesis, other punctuation doesn't bother me
    word_r1 = word.replace("[", " ")
    word_r2 = word_r1.replace("]", " ")
    word_r3 = word_r2.replace("(", " ")
    word_r4 = word_r3.replace(")", " ")
    mushroom_words[word_r4] = len(word_r4)

#check, cool
#for mushroom in mushroom_words.keys():
#    print mushroom + ": " + str(mushroom_words[mushroom])

for word in magic_str.split():
    word_r1 = word.replace("\"", "")
    magic_words[word_r1] = len(word_r1)

#check, cool
#for magic in magic_words.keys():
#    print magic + ": " + str(magic_words[magic])

#trying to figure out pulling out keys by value, but actually
#I think I have the dictionaries I want backwards
for key, value in mushroom_words.items():
    if mushroom_value == value:
    all4keys.append(key) 

print random.choice(all4keys)

 
