print("Directions:")
print("Given a DNA string t having length at most 1000 nt, return the transcribed RNA string of t\n\n")

f = open("../files/rosalind_rna.txt")
dna = f.readline().strip()
rna = dna.replace("T", "U")
print(rna)
