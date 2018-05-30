input = open('../files/rosalind_ini5.txt', 'r')
lines = input.readlines()
output = open('../files/output.txt', 'w')
for i in range(len(lines)):
	if (i % 2 == 1):
		output.write(lines[i])
		print(lines[i].strip())
input.close()
output.close()
