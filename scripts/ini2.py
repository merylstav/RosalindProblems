print("Directions:")
print("Given 2 positive integers a and b less than 100, return the integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b\n\n")
f = open("../files/rosalind_ini2.txt")
a,b = map(int, f.readline().strip().split())
print("a = %i" % a)
print("b = %i" % b)
c_sqrd = a ** 2 + b ** 2
print(c_sqrd)
