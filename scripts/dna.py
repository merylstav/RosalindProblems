print("Directions:")
print("\tGiven a DNA string s of length at most 1000 nt")
print("\tReturn four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s")
print("Previous problems(s):\n")

f = open("../files/rosalind_dna.txt")
dna = f.readline().strip()
print(dna)
print(str(dna.count("A")) + " " + str(dna.count("C")) + " " + str(dna.count("G")) + " " + str(dna.count("T")))
