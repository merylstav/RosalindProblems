print("Directions:")
print("\tGiven an RNA string s corresponding to a strand of mRNA (of length at most 10 kbp)")
print("\tReturn the protein string encoded by s")
print("Previous problem(s): REVC\n")

RNA_to_Protein = {}
for line in open("../files/RNA_to_Protein.txt"):
	split = line.strip().split()
	RNA_to_Protein[split[0]] = split[1]

#print(RNA_to_Protein)

f = open("../files/rosalind_prot.txt")
RNA = f.readline().strip()
Protein = ""
for i in range(0, len(RNA), 3):
	if (RNA_to_Protein[RNA[i:i+3]] == "-"):
		break
	Protein = Protein + RNA_to_Protein[RNA[i:i+3]]
print(Protein)
