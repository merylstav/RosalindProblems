print("Directions:")
print("Given three positive integers k, m, and n, representing a population containing k + m + n organisms: k individiuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive, return the probability that two randomly selected mating organisms will produce an individual possesing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.\n\n")

f = open("../files/rosalind_iprb.txt")
k,m,n = map(float, f.readline().strip().split())
t0 = k + m + n
t1 = t0 - 1
print("%i + %i + %i = %i" % (k, m, n, t0)) 
pk = (k/t0)
pm = (m/t0)*((k/t1) + 0.75*((m-1)/t1) + 0.5*(n/t1))
pn = (n/t0)*((k/t1) + 0.5*(m/t1))
#print(str(pk))
#print(str(pm))
#print(str(pn))
p = pk + pm + pn
print(str(p))
