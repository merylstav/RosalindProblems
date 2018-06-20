print("Directions:")
print("\tGiven positive integers n <= 100 and m <= 20")
print("\tReturn the total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.")
print("Previous problem(s): FIB\n")

f = open("../files/rosalind_fibd.txt")
n,m = map(int, f.readline().strip().split())
#print("n = %i, m = %i" % (n, m))
F = {}
F[0] = F[1] = 1
#print("F[0] = %i\nF[1] = %i" % (F[0], F[1]))
for i in range(2, m):
	F[i] = F[i - 1] + F[i - 2]
#	print("F[%i] = F[%i] + F[%i] = %i" % (i, i-1, i-2, F[i]))
F[m] = F[m-1] + F[m-2] - 1
#print("F[%i] = F[%i] + F[%i] - 1 = %i + %i - 1 = %i" % (m, m-1, m-2, F[m-1], F[m-2], F[m]))

for i in range(m+1, n):
	F[i] = F[i - 1] + F[i - 2] - F[i - m - 1]
#	print("F[%i] = F[%i] + F[%i] - F[%i] = %i + %i - %i = %i" % (i, i-1, i-2, i-m-1, F[i-1], F[i-2], F[i-m-1], F[i]))
print(F[n-1])
