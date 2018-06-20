print("Directions:")
print("\tGiven two positive integers k (k <= 7) and N (N <= 2^k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.")
print("\tReturn the probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.")
print("Previous problem(s): IPRB\n")

import operator as op
def ncr(n, r):
	r = min(r, n-r)
	numer = reduce(op.mul, xrange(n, n-r, -1), 1)
	denom = reduce(op.mul, xrange(1, r+1), 1)
	return numer//denom

f = open("../files/rosalind_lia.txt")
k,n = map(int, f.readline().strip().split())
max = 2**k
print("k = %i <= 7\nn = %i <= 2^%i = %i" % (k, n, k, max))
result = 0
for i in range(n,max+1):
	result += ncr(max, i)*(0.25**i)*(0.75**(max - i))
print("%1.3f" % result)
