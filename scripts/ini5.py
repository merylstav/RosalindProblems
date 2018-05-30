print("Directions:")
print("Given a file containing at most 1000 files, return a file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.\n\n")

input = open('../files/rosalind_ini5.txt', 'r')
lines = input.readlines()
output = open('../files/output.txt', 'w')
for i in range(len(lines)):
	if (i % 2 == 1):
		output.write(lines[i])
		print(lines[i].strip())
input.close()
output.close()
