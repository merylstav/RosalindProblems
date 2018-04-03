f = open("../files/rosalind_iprb.txt")
k,m,n = map(float, f.readline().strip().split())
t0 = k + m + n
t1 = t0 - 1
print("%i + %i + %i + %i" % (k, m, n, t0)) 
pk = (k/t0)
pm = (m/t0)*((k/t1) + 0.75*((m-1)/t1) + 0.5*(n/t1))
pn = (n/t0)*((k/t1) + 0.5*(m/t1))
print(str(pk))
print(str(pm))
print(str(pn))
p = pk + pm + pn
print(str(p))
