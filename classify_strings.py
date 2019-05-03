
import re, string

from alphabet_triples import triples_list

clean_pattern = re.compile('[\W_]+')

triples = triples_list()

cache = {}

for triple in triples:
	cache[triple] = []

test_string = ".hack//G.U. vol. 1//Rebirth (.hack//G.U. Vol.1 ??;.hack//G.U. Vol.1 Saitan;dot Hack: G.U. Vol 1. Rebirth) (2006, Namco;Bandai) (PS2)"

def clean_string(input):
	return clean_pattern.sub('', test_string).lower()

def add_to_cache(input):
	clean_input = clean_string(input)
	for triple in triples:
		if triple in clean_input:
			cache[triple].append(test_string)

if __name__ == "__main__":
	add_to_cache(test_string)
	print(cache)
