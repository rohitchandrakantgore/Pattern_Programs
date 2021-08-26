height = int(input("Enter Height: "))

print('Pattern 1: ')
for i in range(height,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    print()

print('--------------------')
print('Pattern 2: ')
for i in range(height,0,-1):
    for j in range(i):
        print(height-j,end=' ')
    print()


print('--------------------')
print('Pattern 4: ')
for i in range(height,0,-1):
    for j in range(i):
        print(height-i+1,end=' ')
    print()
        
print('--------------------')
print('Pattern 4: ')
for i in range(height,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()