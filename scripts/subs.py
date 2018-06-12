print("Directions:")
print("\tGiven two DNA strings s and t (each of length at most 1 kbp)")
print("\tReturn all locations of t as a substring of s")
print("Previous problem(s): REVC\n")

f = open("../files/rosalind_subs.txt")
s = f.readline().strip()
t = f.readline().strip()
import re
ids = [m.start()+1 for m in re.finditer("(?=%s)" % t, s)]
print(" ".join(map(str, ids)))
