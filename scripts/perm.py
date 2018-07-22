print("Directions:")
print("\tGiven a positive integer n <= 7.")
print("\tReturn The total number of permutations of length n, followed by a list of all such permutations (in any order).")
print("Previous Problems: HAMM\n")

f = open("../files/rosalind_perm.txt")
n = int(f.readline().strip())

def permutation(lst):
    if len(lst) < 1:
        return([])
    if len(lst) == 1:
        return([lst])
    l = []
    range_lst_len = range(len(lst))
    for i in range_lst_len:
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l
 
 
perms = permutation([x+1 for x in range(n)])
print(str(len(perms)))
for p in perms:
    print(" ".join(map(str, p)))
