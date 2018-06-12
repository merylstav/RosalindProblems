print("Directions:")
print("\tGiven two dna strings s and t of equal length (not exceeding 1 kbp)")
print("\tReturn the Hamming distance dH(s,t)")
print("Previous problem(s): REVC\n")

f = open("../files/rosalind_hamm.txt")
s = f.readline().strip()
t = f.readline().strip()
#print(s)
#print(t)
count = 0
#miss_ids = []
for i in range(len(s)):
	 if s[i] != t[i]:
		count += 1
#		miss_ids.append(i)
print(count)
#print(miss_ids)
print(sum(a != b for (a,b) in zip(s,t)))
