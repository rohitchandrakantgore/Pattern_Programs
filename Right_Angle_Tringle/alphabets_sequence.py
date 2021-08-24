height = int(input("Enter Height: "))

print("Pattern 1: ")
for i in range(1,height+1):
    for j in range(i):
        print(chr(65+j), end=' ')
    print()
    
print('----------------')
print("Pattern 2: ")
for i in range(1,height+1):
    for j in range(i):
        print(chr(65+height-1-j), end=' ')
    print()
    
print('----------------')
print("Pattern 3: ")
for i in range(1,height+1):
    for j in range(i):
        print(chr(64+i), end=' ')
    print()
    
print('----------------')
print("Pattern 4: ")
for i in range(1,height+1):
    for j in range(i):
        print(chr(65+height-i), end=' ')
    print()
    
# Enter Height: 5
# Pattern 1: 
# A
# A B
# A B C
# A B C D
# A B C D E
# ----------------
# Pattern 2:
# E
# E D
# E D C
# E D C B
# E D C B A
# ----------------
# Pattern 3:
# A
# B B
# C C C
# D D D D
# E E E E E
# ----------------
# Pattern 4:
# E
# D D
# C C C
# B B B B
# A A A A A