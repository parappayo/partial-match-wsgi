
import re, string

clean_pattern = re.compile('[\W_]+')

test_string = ".hack//G.U. vol. 1//Rebirth (.hack//G.U. Vol.1 ??;.hack//G.U. Vol.1 Saitan;dot Hack: G.U. Vol 1. Rebirth) (2006, Namco;Bandai) (PS2)"

def clean_string(input):
	return clean_pattern.sub('', test_string).lower()

print(clean_string(test_string))
