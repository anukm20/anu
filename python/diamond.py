for i in range(0,0):
    for j in range(0,6-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print("\n")
for i in range(0,6-1):
    for j in range(0,i+1):
        print(" ",end="")
    for j in range(0,6-i-1):
        print("* ",end="")
    print("\n")