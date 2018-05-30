n = 31
k = 3
f = {}
f[0] = f[1] = 1
for i in range(2, n):
	f[i] = f[i-1] + f[i-2]*k
print(f[n-1])
a = b = 1
for i in range(2, n):
	a, b = b, k*a + b
print(b)
