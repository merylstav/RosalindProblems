print("Directions:")
print("\tGiven a protein string of length at most 1000 aa")
print("\tReturn the total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)")
print("Previous problem(s): PROT\n")

ProteinCount = {}
for line in open("../files/RNA_to_Protein.txt"):
	split = line.strip().split()
	if split[1] in ProteinCount.keys():
		ProteinCount[split[1]] += 1
	else:
		ProteinCount[split[1]] = 1
f = open("../files/rosalind_mrna.txt")
Strand = f.readline().strip()
options = 1
for protein in Strand:
	options = (options * ProteinCount[protein]) % 1000000
#	print("%s : %i : %i" % (protein, ProteinCount[protein], options))
options = (options * ProteinCount["-"]) % 1000000
#print("STOP : %i : %i" % (ProteinCount["-"], options))
print(options)
