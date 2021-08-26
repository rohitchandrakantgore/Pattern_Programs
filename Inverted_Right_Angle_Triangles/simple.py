height = int(input("Enter Height: "))

for i in range(height,0,-1):
    for j in range(i):
        print('*', end=' ')
    print()
    
# Enter Height: 5
# * * * * * 
# * * * *
# * * *
# * *
# *