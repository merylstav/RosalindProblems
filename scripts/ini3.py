print("Directions:")
print("Given a string s of length at most 200 letters and four integers a, b, c and d, return the slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elemets s]b] and s[d] in our slice\n\n")

f = open("../files/rosalind_ini3.txt")
s = f.readline().strip()
a, b, c, d = map(int, f.readline().strip().split())

new_s = s[a:b+1] + " " + s[c:d+1]
print(s)
print("ids: %i, %i, %i, and %i" % (a, b, c, d))
print(new_s)
