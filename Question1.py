#Question 1
import math
a, b, c = input("Enter the values of a, b and c: ").split()
#Enter values of a, b and c separated by space
a = int(a)
b = int(b)
c = int(c)
D = (b*b) - (4*a*c)
print("Determinant = ", D)
if (D>0):
    root = math.sqrt(D)
    x1 = (-b + root) / (2*a)
    x2 = (-b - root) / (2*a)
    print("Roots = ",x1,x2)
elif (D == 0):
    root = -b / (2*a)
    print("Root = ",root)
else:
    print("Only complex roots!")


