print("Directions:")
print("Given a DNA string s of length at most 1000 bp, return the reverse complement sc of s.\n\n")

f = open("../files/rosalind_revc.txt")
dna = f.readline().strip()
#print(dna)
#print("")
rev = dna.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()[::-1]
print(rev)
