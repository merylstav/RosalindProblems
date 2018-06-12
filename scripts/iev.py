print("Directions:")
print("\tGiven six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes (1) AA-AA (2) AA-Aa (3) AA-aa (4) Aa-Aa (5) Aa-aa (6) aa-aa")
print("\tReturn the expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.")
print("Previous problem(s): IPRB\n")

f = open("../files/rosalind_iev.txt")
data = map(int, f.readline().strip().split())
#print(data)
probsTimes2 = [2.0, 2.0, 2.0, 1.5, 1.0, 0.0]
offsprings = sum([a * b for (a, b) in zip(data, probsTimes2)])
print(offsprings)

