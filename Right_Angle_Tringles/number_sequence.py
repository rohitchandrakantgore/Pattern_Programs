height = int(input("Enter Height: "))

print("Pattern 1: ")
for i in range(1,height+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print("-----------------")

print("Pattern 2: ")
for i in range(1,height+1):
    for j in range(1,i+1):
        print(height+1-j,end=' ')
    print()
    
print("-----------------")
print("Pattern 3: ")
for i in range(1,height+1):
    for j in range(i):
        print(i,end=' ')
    print()

print("-----------------")
print("Pattern 3: ")
for i in range(1,height+1):
    for j in range(i):
        print(height+1-i,end=' ')
    print()
    
# Enter Height: 5
# Pattern 1: 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# -----------------
# Pattern 2:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
# -----------------
# Pattern 3:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# -----------------
# Pattern 3:
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1