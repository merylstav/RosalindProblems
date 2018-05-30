f = open("../files/rosalind_rna.txt")
dna = f.readline().strip()
rna = dna.replace("T", "U")
print(rna)
