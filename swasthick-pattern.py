n = int(input())
print("*",end=" ")
for i in range(int((n-3)/2)):
    print(" ", end = " ")
for i in range(int((n+1)/2)):
    print("*",end = " ")
print("")
for i in range(int((n-3)/2)):
    print("*",end=" ")
    for j in range(int((n-3)/2)):
        print(" ",end = " ")
    print("*")
for i in range(n):
    print("*",end = " ")
print("")
for i in range(int((n-3)/2)):
    for j in range(int((n-3)/2)+1):
        print(" ",end = " ")
    print("*", end = " ")
    for k in range(int((n-3)/2)):
        print(" ", end = " ")
    print("*")
for i in range(int((n+1)/2)):
    print("*",end = " ")
for i in range(int((n-3)/2)):
    print(" ",end =" ")
print("*")
