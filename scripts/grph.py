print("Directions:")
print("\tGiven a collection of DNA strings in FASTA format having total length at most 10 kbp.")
print("\tReturn the adjacency list corresponding to O3. You may return edges in any order.")
print("Previous problem(s): GC, SUBS\n")

fasta_dic = {}
f = open("../files/rosalind_grph.txt")
lines = f.read().split(">")
for fasta in lines[1:]:
	item = fasta.split("\n")
	fasta_dic[item[0]] = "".join(item[1:])

for key1, value1 in fasta_dic.iteritems():
	for key2, value2 in fasta_dic.iteritems():
		if(key1 == key2):
			continue;
		if(value1.endswith(value2[:3])):
			print("%s %s" % (key1, key2))
#			print("%s %s" % (value1, value2))
