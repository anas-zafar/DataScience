#Question4
y = [1,3,6,78,35,55]
z = [12,24,35,24,88,120,155]

def intersection(y, z):
    return(set(y) & set(z))

print(intersection(y, z))