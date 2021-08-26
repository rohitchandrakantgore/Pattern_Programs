

height = int(input("Enter Height: "))
digit = int(input("Enter Digit: "))
print("-----------")
print("Pattern 1: ")
for i in range(height,0,-1):
    print(' '*(height-i)+((str(digit)+' ') *i))
    
print("-----------")
print("Pattern 2: ")
for i in range(height,0,-1):
    print(" "*(height-i), end='')
    for j in range(i):
        print(j+1, end=' ')
    print()
    
    
print("-----------")
print("Pattern 3: ")
for i in range(height,0,-1):
    print(" "*(height-i), end='')
    for j in range(i):
        print(i-j, end=' ')
    print()

print("-----------")
print("Pattern 4: ")
for i in range(height,0,-1):
    print(" "*(height-i), end='')
    for j in range(i):
        print(height-i+1, end=' ')
    print()

print("-----------")
print("Pattern 5: ")
for i in range(height,0,-1):
    print(" "*(height-i), end='')
    for j in range(i):
        print(i, end=' ')
    print()
    
# Enter Height: 5
# Enter Digit: 8
# -----------
# Pattern 1:
# 8 8 8 8 8
#  8 8 8 8
#   8 8 8
#    8 8
#     8
# -----------
# Pattern 2:
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
# -----------
# Pattern 3:
# 5 4 3 2 1
#  4 3 2 1
#   3 2 1
#    2 1
#     1
# -----------
# Pattern 4:
# 1 1 1 1 1
#  2 2 2 2
#   3 3 3 
#    4 4
#     5
# -----------
# Pattern 5:
# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1