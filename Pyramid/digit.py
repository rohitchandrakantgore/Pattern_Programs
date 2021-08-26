height = int(input("Enter Height: "))
digit = int(input("Enter Digit: "))
print("Pattern 1: ")
for i in range(height):
    print(" "*(height-i-1)+(str(digit)+' ') *(i+1))

print('---------------')
print("Pattern 2: ")
for i in range(height):
    print(" "*(height-i-1)+(str(i+1)+' ') *(i+1))

print('----------------')
print("Pattern 3: ")
for i in range(height):
    print(" "*(height-i-1)+(str(height-i)+' ') *(i+1))


print('----------------')
print("Pattern 3: ")
for i in range(height):
    print(" "*(height-i-1), end='')
    for j in range(i+1):
        print(str(j+1), end=' ')
    print()

print('----------------')
print("Pattern 4: ")
for i in range(height):
    print(" "*(height-i-1), end='')
    for j in range(i+1):
        print(str(height-j), end=' ')
    print()

# Enter Height: 5
# Enter Digit: 7
# Pattern 1: 
#     7 
#    7 7 
#   7 7 7 
#  7 7 7 7 
# 7 7 7 7 7 
# ---------------
# Pattern 2: 
#     1 
#    2 2   
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5 
# ----------------
# Pattern 3: 
#     5 
#    4 4 
#   3 3 3 
#  2 2 2 2 
# 1 1 1 1 1 
# ----------------
# Pattern 3: 
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
# ----------------
# Pattern 4:     
#     5 
#    5 4 
#   5 4 3 
#  5 4 3 2 
# 5 4 3 2 1 