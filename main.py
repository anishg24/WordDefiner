import requests
import argparse

parser = argparse.ArgumentParser(description="Define a list of words given in a file.")
parser.add_argument("infile", metavar="in", nargs="?", type=str, help="input file full of words to define")
parser.add_argument("outfile", metavar="out", nargs="?", type=str, help="output file of definitons (default: out.txt)")
parser.add_argument("-n", help="don't show noun definitions", action="store_true")
parser.add_argument("-v", help="don't show verb definitions", action="store_true")
parser.add_argument("-a", help="don't show adjectives definitions", action="store_true")
args = parser.parse_args()

black_listed_defs = []

def get_definition(word):
	try:
		response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}").json()[0]
		assert(response["word"] in word.lower())
	except:
		print("ERROR WITH " + word)
		return (None, None)

	result = []
	for meaning in response["meanings"]:
		definitions = []
		for d in meaning["definitions"]:
			definitions.append(d["definition"])

		result.append((meaning["partOfSpeech"], tuple(definitions)))
	return result


with open(args.infile, "r") as file:
	words = list(filter(lambda y: bool(y), map(lambda x: x.split(".")[::-1][0].strip(), file.readlines())))
	print("GETTING DEFINITIONS...")
	definitions = list(map(lambda w: (w, get_definition(w)), set(words)))
	print("GOT ALL DEFINITIONS...")
	with open(args.outfile, "w+") as outfile:
		for index, definition in enumerate(definitions):
			outfile.write(f"{index + 1}. {definition[0]}\n")
			for meaning in definition[1]:
				for m in meaning[1]:
					outfile.write(f"\t({meaning[0]}) - {m}\n")

print("DONE")