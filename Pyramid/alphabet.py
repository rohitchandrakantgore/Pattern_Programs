height = int(input("Enter Height: "))
alphabet = input("Enter Alphabet: ")
print("pattern 1: ")
for i in range(height):
    print(" "*(height-i-1)+(alphabet+' ') *(i+1))

print('-------------')
print("pattern 2: ")
for i in range(height):
    print(" "*(height-i-1)+(chr(65+i)+' ') *(i+1))

print('-------------')
print("pattern 2: ")
for i in range(height):
    print(" "*(height-i-1)+(chr(64+height-i)+' ') *(i+1))


print('-------------')
print("pattern 3: ")
for i in range(height):
    print(" "*(height-i-1),end='')
    for j in range(i+1):
        print(chr(65+j), end=' ')
    print()
    
print('-------------')
print("pattern 4: ")
for i in range(height):
    print(" "*(height-i-1),end='')
    for j in range(i+1):
        print(chr(64+height-j), end=' ')
    print()


# Enter Height: 5
# Enter Alphabet: H
# pattern 1: 
#     H
#    H H
#   H H H
#  H H H H
# H H H H H
# -------------
# pattern 2:
#     A
#    B B
#   C C C
#  D D D D
# E E E E E
# -------------
# pattern 2:
#     E
#    D D
#   C C C
#  B B B B
# A A A A A
# -------------
# pattern 3:
#     A
#    A B
#   A B C
#  A B C D
# A B C D E
# -------------
# pattern 4:
#     E
#    E D
#   E D C
#  E D C B 
# E D C B A