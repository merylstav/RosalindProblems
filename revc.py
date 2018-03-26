f = open("../files/rosalind_revc.txt")
dna = f.readline().strip()
print(dna)
print("")
rev = dna.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()[::-1]
print(rev)
