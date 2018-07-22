print("Directions")
print("\tGiven at most 15 UniProt Protein Database access IDs.")
print("\tReturn for each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.")
print("Previous problems(s): PROT, SUBS\n")

import uniprot
import urllib
import re

for line in open("../files/rosalind_mprt.txt"):
	fasta_id = line.strip()

	protein_url="http://www.uniprot.org/uniprot/%s.fasta" % fasta_id
	f=urllib.urlopen(protein_url)
	protein_fasta=f.read()
	protein_fasta=protein_fasta.split("\n")
	protein_seq="".join(protein_fasta[1:])
	matches = [match.start()+1 for match in re.finditer(r"(?=(N[^P][ST][^P]))", protein_seq)]
	if (len(matches) > 0):
		print(fasta_id)
		print(" ".join(map(str, matches)))
