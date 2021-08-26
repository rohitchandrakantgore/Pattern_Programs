
height = int(input("enter height oddno.: "))
max_l= int((height+1)/2)

for i in range(1,max_l+1):
    print("* "*i)

for i in range(max_l-1,0,-1):
    print("* "*i)
    
    
# enter height oddno.: 5
# * 
# * *
# * * *
# * *
# *