print("Directions:")
print("\tGiven positive integers n <= 40 and k <= 5")
print("\tReturn the total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).")
print("Previous problem(s): REVC\n")
f = open("../files/rosalind_fib.txt")
n, k = map(int, f.readline().strip().split())
print("n = %i\nk = %i" % (n, k))
F = {}
F[0] = F[1] = 1
for i in range(2, n):
	F[i] = F[i-1] + F[i-2]*k
print(F[n-1])
# The option below returns the same output
a = b = 1
for i in range(2, n):
	a, b = b, k*a + b
print(b)
