
def next_char(char):
	return chr(ord(char) + 1)

def next_triple(triple):
	if triple[2] < 'z':
		return triple[0:2] + next_char(triple[2])
	if triple[1] < 'z':
		return triple[0:1] + next_char(triple[1]) + 'a'
	if triple[0] < 'z':
		return next_char(triple[0]) + 'aa'
	return False

class AlphabetTriples:
	"""Iterable over all 3-letter combinations"""

	def __init__(self):
		self.current = 'aaa'

	def __iter__(self):
		return self

	def __next__(self):
		if self.current == False:
			raise StopIteration
		result = self.current
		self.current = next_triple(self.current)
		return result

def triples_list():
	result = []
	triples = AlphabetTriples()
	for triple in triples:
		result.append(triple)
	return result

if __name__ == "__main__":
	for triple in triples_list():
		print(triple)
