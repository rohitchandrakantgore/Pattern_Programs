height = int(input("Enter Height: "))
alphabet= input("Enter Alphabet: ")

print("-------------")
print("Pattern 1: ")
for i in range(height,0,-1):
    print(" "*(height-i) + (alphabet+' ')*i)
    
print("-------------")
print("Pattern 2: ")
for i in range(height,0,-1):
    print(" "*(height-i) + (chr(64+height-i+1)+' ')*i)
    
print("-------------")
print("Pattern 3: ")
for i in range(height,0,-1):
    print(" "*(height-i) + (chr(64+i)+' ')*i)
    
print("-------------")
print("Pattern 4: ")
for i in range(height,0,-1):
    print(" "*(height-i), end='')
    for j in range(i):
        print(chr(64+j+1), end=' ')
    print()
    
print("-------------")
print("Pattern 5: ")
for i in range(height,0,-1):
    print(" "*(height-i), end='')
    for j in range(i):
        print(chr(64+i-j), end=' ')
    print()
    
    
# Enter Height: 5
# Enter Alphabet: Z
# -------------
# Pattern 1:
# Z Z Z Z Z
#  Z Z Z Z
#   Z Z Z
#    Z Z
#     Z
# -------------
# Pattern 2:
# A A A A A
#  B B B B
#   C C C
#    D D
#     E
# -------------
# Pattern 3:
# E E E E E
#  D D D D
#   C C C
#    B B
#     A
# -------------
# Pattern 4:
# A B C D E
#  A B C D
#   A B C
#    A B
#     A
# -------------
# Pattern 5:
# E D C B A
#  D C B A
#   C B A
#    B A
#     A