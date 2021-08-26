height = int(input("Enter Height: "))

print('Pattern 1: ')
for i in range(height,0,-1):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()

print('--------------------')
print('Pattern 2: ')
for i in range(height,0,-1):
    for j in range(i):
        print((chr(64+height-j)),end=' ')
    print()
    
print('--------------------')
print('Pattern 3: ')
for i in range(height,0,-1):
    for j in range(i):
        print((chr(65+i-1)),end=' ')
    print()


print('--------------------')
print('Pattern 4: ')
for i in range(height,0,-1):
    for j in range(i):
        print(chr(65+height-i),end=' ')
    print()
    
# Enter Height: 5
# Pattern 1: 
# A B C D E
# A B C D
# A B C
# A B
# A
# --------------------
# Pattern 2:
# E D C B A
# E D C B
# E D C
# E D
# E
# --------------------
# Pattern 3:
# E E E E E
# D D D D
# C C C
# B B
# A
# --------------------
# Pattern 4:
# A A A A A
# B B B B
# C C C
# D D
# E