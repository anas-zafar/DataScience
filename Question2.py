#Question 2
def smaller(x, a, b):
    count = 0
    for i in x:
        if (b > i):
            count = count + 1
    return count



x = []
s = int(input("Input the number of elements: "))
print("Enter array elements: ")
for j in range(0,s):
    no = int(input())
    x.append(no)

n = int(input("Please enter n:"))
ans = smaller(x, s, n)
print("answer: ", ans)


