#by jasmine
#march 2017
#v 0.0.2

#read my custom library
import aimDef

# read in text
input_str = open('SequoiaNatPark.txt').read()

#call create AIM conversation
aimDef.createPoem(input_str)
