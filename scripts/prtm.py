print("Directions")
print("\tGiven a protein string P of length at most 1000 aa.")
print("\tReturn the total weight of P. Consult the monoisotopic mass table.")
print("Previous problem(s): PROT\n")

MassTable = {}
for line in open("../files/MonoisotopicMassTable.txt"):
	aa, mass = line.strip().split()
	MassTable[aa] = float(mass)

f = open("../files/rosalind_prtm.txt")
P = f.readline().strip()
total = 0
for a in P:
	total += MassTable[a]
print("%.3f" % total)
