#by jasmine
#february 2017
#v 0.0.2

#import sys
import random

# read in mushroom recipes
mushrooms_str = open('mushroomRecipes.txt').read()

# create empty lists
magic_words = []
mushroom_words = []

#array for picking out random mushrooms, but this didn't work
random_mushroom = []
x = 0 

#final poem
all_lines = []

# iterate over each word in mushrooms
# pick some words
for word in mushrooms_str.split():
    if len(word) > 3:
        mushroom_words.append(word)

# read in magic the gathering text
for line in open('ArtifactsEnchantments.txt'):
    line = line.strip()
    if len(line) > 0:
        line_words = line.split()
        line_length = len(line_words);
        if line_length > 2:
            magic = random.sample(line_words, line_length-1)
    all_lines.append(magic)

#put together poem by mashing together words
for line in all_lines:
    x = x + 1
    if x % 2 > 0:
        if len(line) < 4:
            two_mushrooms = random.sample(mushroom_words,2)
            line = single_mushroom + line[:1] + two_mushrooms + line[2:]
            print ' '.join(line)   
        if len(line) > 4:
            single_mushroom = random.sample(mushroom_words,1)
            three_mushrooms = random.sample(mushroom_words,3)
            #full_line = line[:1] + single_mushroom + line[2:3] + three_mushrooms + line[4:]
            #line = random.sample(full_line,6)
            line = line[:1] + single_mushroom + line[2:3] + three_mushrooms + line[4:]
            #line = line[:3] + two_mushrooms + line[4:]
            print ' '.join(line)   
