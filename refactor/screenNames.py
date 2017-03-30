#by jasmine
#march 2017
#v 0.0.2

#read my custom library
import aimDef

# read in text
input_str = open('SequoiaNatPark.txt').read()

pairs = []

#super simple - just do screen names
words = aimDef.wordList(input_str)

#first pair
pair1 = aimDef.screenName(words)

print pair1[0] + " has entered the chat."
print pair1[1] + " has left the chat."

#second pair
pair2 = aimDef.screenName(words)

print pair2[0] + " has entered the chat."
print pair2[1] + " has entered the chat."

#third pair
pair3 = aimDef.screenName(words)

print pair3[0] + " has left the chat."
print pair3[1] + " has entered the chat."
