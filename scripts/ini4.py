print("Directions:")
print("Given two possitive integers a and b (a < b < 10000), return the sum of all odd integers from a through b, inclusively\n\n")
f = open("../files/rosalind_ini4.txt")
a,b = map(int, f.readline().strip().split())
print("a = %i" % a)
print("b = %i" % b)
sum = 0
while (a < b):
	if (a % 2 == 1):
		sum += a
	a += 1
print(sum)
