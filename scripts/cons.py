print("Directions:")
print("\tGiven a collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.")
print("\tReturn a consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.")
print("Previous problem(s): FIBS, SUBS, HAMM\n")

import uniprot

filename = "../files/rosalind_cons.txt"
seqids, keyvals = uniprot.read_fasta(filename)
fastas = [d['sequence'] for d in keyvals.values()]

strlen = len(fastas[0])
A = [0] * strlen
T = [0] * strlen
C = [0] * strlen
G = [0] * strlen
for fasta in fastas:
	for i, ATCG in enumerate(fasta):
		if ATCG == "A":
			A[i] += 1
		elif ATCG == "T":
			T[i] += 1
		elif ATCG == "C":
			C[i] += 1
		else:
			G[i] += 1
consensus = [""] * strlen
for i in range(strlen):
	if max(A[i], T[i], C[i], G[i]) == A[i]:
		consensus[i] = "A"
	elif max(A[i], T[i], C[i], G[i]) == T[i]:
		consensus[i] = "T"
	elif max(A[i], T[i], C[i], G[i]) == C[i]:
		consensus[i] = "C"
	else:
		consensus[i] = "G"
print("".join(consensus))
print("A: %s" % " ".join(map(str, A)))
print("C: %s" % " ".join(map(str, C)))
print("G: %s" % " ".join(map(str, G)))
print("T: %s" % " ".join(map(str, T)))
