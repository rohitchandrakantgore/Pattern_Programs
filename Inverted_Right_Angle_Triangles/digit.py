height = int(input("Enter Height: "))
digit = int(input("Enter Digit: "))

for i in range(height,0,-1):
    for j in range(i):
        print(str(digit), end=' ')
    print()
    
# Enter Height: 5
# Enter Digit: 6
# 6 6 6 6 6 
# 6 6 6 6
# 6 6 6
# 6 6
# 6
