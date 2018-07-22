print("Directions")
print("\tGiven a collection of k (k<=100) DNA strings of length at most 1 kbp each in FASTA format.")
print("\tReturn a longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)")
print("Previous Problem(s): SUBS, HAMM\n")

from Bio import SeqIO
import re

def compare(str1, str2):
#	print("Comparing %s with %s" % (str1, str2))
	if (len(str1) < len(str2)):
		str1, str2 = str2, str1
	l1 = len(str1)
	l2 = len(str2)
	ids1 = range(l1)
	ids2 = range(l2)
	revids1 = reversed(ids1)
	shortids2 = ids2[1:]
	output_set = set()
#	print(output_set)
	for i in revids1:
		match = ""
		for j in ids2:
			if (i+j < l1):
				if (str1[i+j] == str2[j]):
					match += str2[j]
				else:
					output_set.add(match)
#					print("\t%s" % match)
					match = ""
#				print("%s\t%s" % (str1[i+j], str2[j]))
#		print("\t%s" % match)
		output_set.add(match)
#		print(output_set)
#	print("Forward search complete. Starting backwards search")
	for j in shortids2:
		match = ""
		for i in ids2:
			if (i+j < l2):
				if (str1[i] == str2[i+j]):
					match += str1[i]
				else:
					output_set.add(match)
#					print("\t%s" % match)
					match = ""
#				print("%s\t%s" % (str1[i], str2[i+j]))
#		print("\t%s" % match)
		output_set.add(match)
#		print(output_set)
	return(output_set)		

filename = "../files/rosalind_lcsm.txt"
fastas = []
for record in SeqIO.parse(filename, "fasta"):
	fastas.append("".join(map(str, record.seq)))
#print(fastas)

fastas.sort(key=lambda item: (len(item), item))
#print(fastas)

origSubstrings = compare(fastas[1], fastas[0])
#print(origSubstrings)

remainingFastas = fastas[2:]
for fasta in remainingFastas:
	outputSubstrings = set()
	for substring in origSubstrings:
		if re.search(substring, fasta):
			outputSubstrings.add(substring)
		else:
#			print("%s not found in %s" % (substring, fasta))
			newSubstrings = compare(fasta, substring)
			outputSubstrings = outputSubstrings.union(newSubstrings)
	origSubstrings = outputSubstrings
#	print(origSubstrings)

#print(sorted(origSubstrings, key=len, reverse = True))

print(sorted(origSubstrings, key=len, reverse = True)[0])
