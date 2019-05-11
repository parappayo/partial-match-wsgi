
import re, string, time

from alphabet_triples import triples_list

words_file_path = '/usr/share/dict/words'

clean_pattern = re.compile('[\W_]+')

triples = triples_list()

cache = {}
cache_lines_added = 0

for triple in triples:
	cache[triple] = []

def clean_string(input):
	return clean_pattern.sub('', input).lower()

def add_to_cache(input):
	global cache_lines_added
	clean_input = clean_string(input)
	for triple in triples:
		if triple in clean_input:
			cache[triple].append(input)
	cache_lines_added += 1

def populate_cache(input_file_path, line_limit):
	with open(input_file_path) as input_file:
		for input_line in input_file:
			if line_limit > 0 and cache_lines_added >= line_limit:
				break
			add_to_cache(input_line)

if __name__ == "__main__":
	start = time.time()
	populate_cache(words_file_path, 1000)
	seconds = time.time() - start
	print(f"added {cache_lines_added} input lines in {seconds} seconds")
