print("Directions:")
print("\tGiven a DNA string t having length at most 1000 nt")
print("\tReturn the transcribed RNA string of t")
print("Previous problems(s): DNA\n")

f = open("../files/rosalind_rna.txt")
dna = f.readline().strip()
rna = dna.replace("T", "U")
print(rna)
