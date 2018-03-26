f = open("../files/rosalind_dna.txt")
dna = f.readline().strip()
print(dna)
#A = 0
#C = 0
#T = 0
#G = 0
#for letter in dna:
#	if letter == "A":
#		A += 1
#	if letter == "C":
#		C += 1
#	if letter == "T":
#		T += 1
#	if letter == "G":
#		G += 1
#print(str(A) + " " + str(C) + " " + str(G) + " " + str(T))
print(str(dna.count("A")) + " " + str(dna.count("C")) + " " + str(dna.count("G")) + " " + str(dna.count("T")))
