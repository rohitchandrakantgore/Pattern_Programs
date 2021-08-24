dim = int(input("Enter Rows: "))
print("Pattern 1: ")
for i in range(dim):
    print((str(i+1)+" ")*dim)
 
print('--------------')   
print("Pattern 2: ")
for i in range(dim):
    print((str(dim-i)+" ")*dim)
    
print('--------------')   
print("Pattern 3: ")
for i in range(dim):
    for j in range(dim):
        print(str(j+1)+" ", end='')
    print()    
print('--------------')   
print("Pattern 4: ")
for i in range(dim):
    for j in range(dim):
        print(str(dim-j)+" ", end='')
    print() 
    
# Enter Rows: 5
# Pattern 1: 
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
# --------------
# Pattern 2:
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1
# --------------
# Pattern 3:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# --------------
# Pattern 4:
# 5 4 3 2 1 
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1