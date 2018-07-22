print("Directions:")
print("\tGiven a DNA string of length at most 1 kbp in FASTA format.")
print("\tReturn the position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.")
print("Previous problem(s): SUBS\n")

from Bio import SeqIO

def reverse_complement(input_strand):
    lookup = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}
    return ''.join([lookup[c] for c in reversed(input_strand)])

filename = "../files/rosalind_revp.txt"
for record in SeqIO.parse(filename, "fasta"):
    fasta = ("".join(map(str, record.seq)))

windows = range(4,13)
for w in windows:
    startids = fasta[:len(fasta)-w+1]
    for i, s in enumerate(startids):
        substring = fasta[i:i+w]
        if substring == reverse_complement(substring):
            print("%i %i" % (i+1, w))
