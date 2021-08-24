dim = int(input("Enter Rows: "))
print("Pattern 1 : ")
for i in range(dim):
    print((chr(65+i)+" ")*dim)
 
print("-------------------------")
print("Pattern 2: ")   
for i in range(dim):
    print((chr(64+dim-i)+" ")*dim)
    
    
print("-------------------------")
print("Pattern 3: ")
for i in range(dim):
    for j in range(dim):
        print(chr(65+j),end=' ')
    print()

print("-------------------------")
print("Pattern 4: ")
for i in range(dim):
    for j in range(dim):
        print(chr(64+dim-j),end=' ')
    print()
    
# Enter Rows: 4
# Pattern 1 : 
# A A A A 
# B B B B 
# C C C C 
# D D D D 
# -------------------------
# Pattern 2: 
# D D D D 
# C C C C 
# B B B B 
# A A A A 
# -------------------------
# Pattern 3:
# A B C D
# A B C D
# A B C D
# A B C D
# -------------------------
# Pattern 4:
# D C B A
# D C B A
# D C B A
# D C B A