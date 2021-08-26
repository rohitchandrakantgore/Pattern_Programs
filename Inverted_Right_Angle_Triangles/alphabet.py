height = int(input("Enter Height: "))
alphabet = input("Enter alphabet: ")

for i in range(height,0,-1):
    for j in range(i):
        print(alphabet, end=' ')
    print()
    
# Enter Height: 5
# Enter alphabet: V
# V V V V V 
# V V V V
# V V V
# V V
# V