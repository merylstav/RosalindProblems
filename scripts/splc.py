print("Directions")
print("\tGiven a DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.")
print("\tReturn a protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)")
print("Previous Problem(s): PROT, SUBS\n")

from Bio import SeqIO


DNA_to_Protein = {}
for line in open("../files/DNA_to_Protein.txt"):
        split = line.strip().split()
        DNA_to_Protein[split[0]] = split[1]

filename = "../files/rosalind_splc.txt"
fastas = []
for record in SeqIO.parse(filename, "fasta"):
	fastas.append("".join(map(str, record.seq)))

exon = fastas[0]
introns = fastas[1:]
for intron in introns:
	exon = exon.replace(intron, "")

n = 3
segments = [exon[i:i+n] for i in range(0, len(exon), n)]
protein = [""] * len(segments)
for i, DNA in enumerate(segments):
	if DNA_to_Protein[DNA] == "-":
		break
	protein[i] = DNA_to_Protein[DNA]
print("".join(protein))
