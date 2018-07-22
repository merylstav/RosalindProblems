print("Directions")
print("\tGiven a DNA string s of length at most 1 kbp in FASTA format.")
print("\tReturn every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.")
print("Previous Problem(s): PROT, SUBS\n")

import uniprot
import re
filename = "../files/rosalind_orf.txt"
seqid, keyval = uniprot.read_fasta(filename)
DNA = keyval.values()[0]['sequence']
RNA = DNA.replace("T", "U")

RNA_to_Protein = {}
for line in open("../files/RNA_to_Protein.txt"):
	split = line.strip().split()
	RNA_to_Protein[split[0]] = split[1]

def possible_strings(input_strand):
	ORF = [match.group(1) for match in re.finditer(r"(?=(AUG(.{3}){0,}?((UAA)|(UAG)|(UGA))))", input_strand)]

	n = 3
	output = []
	for strand in ORF:
		segments = [strand[i:i+n] for i in range(0, len(strand), n)]
		Protein = [""] * len(segments)
		for i, AA in enumerate(segments):
			if (RNA_to_Protein[AA] == "-"):
				break
			Protein[i] = RNA_to_Protein[AA]
		output.append("".join(Protein))
	return output

a = possible_strings(RNA)

def reverse_complement(input_strand):
	lookup = {"A" : "U", "U" : "A", "G" : "C", "C" : "G"}
	return ''.join([lookup[c] for c in reversed(input_strand)])

b = possible_strings(reverse_complement(RNA))
c = list(set().union(a,b))
for Protein in c:
	print(Protein)
