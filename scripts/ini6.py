f = open("../files/rosalind_ini6.txt")
s = f.readline().strip()
print(s)
list = s.split()
print(list)
dict = {}
for word in list:
	if word in dict:
		dict[word] += 1
	else:
		dict[word] = 1
for key in dict:
	print(key + " " + str(dict[key]))
