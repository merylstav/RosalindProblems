print("Directions:")
print("\tGiven at most 100 DNA strings in Fasta format (of length at most 1 kbp each)")
print("\tReturn the ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.")
print("Previous problem(s): REVC\n")

f = open("../files/rosalind_gc.txt")
lines = f.read().split(">")
max_id = ""
max_gc = -1
for item in lines[1:]:
	fasta = item.split("\n")
	id = fasta[0]
	string = "".join(fasta[1:])
	gc = round(((string.count("G") + string.count("C")) * 100.0 / len(string)), 6)
	if (gc > max_gc):
		max_id = id
		max_gc = gc
print(max_id)
print(max_gc)

