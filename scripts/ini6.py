print("Directions:")
print("Given a string s of length at most 10000 letters, return the number of occurences of each word in s, where words are separated by spaces. Words are case-senseitive, and the lines in the output can be in any order.\n\n")

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
