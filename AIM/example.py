#play with code from class tutorial
#https://pronouncing.readthedocs.io/en/latest/tutorial.html

import pronouncing
import random

#text = 'april is the cruelest month breeding lilacs out of the dead'
text = "sequoia"
out = []

for word in text.split():
	pronunciations = pronouncing.phones_for_word(word)
	pat = pronouncing.stresses(pronunciations[0])
	replacement = random.choice(pronouncing.search_stresses("^"+pat+"$"))
	out.append(replacement)

print ' '.join(out)