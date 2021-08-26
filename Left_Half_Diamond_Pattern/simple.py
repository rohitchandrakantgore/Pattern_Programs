
height = int(input("enter height oddno.: "))
max_l= int((height+1)/2)

for i in range(0,max_l):
    print(' '*((max_l-i-1)*2)+ "* "*(i+1))

for i in range(max_l-1,0,-1):
    print(" "*((max_l-i)*2)+ "* "*i)
    
    
# enter height oddno.: 5
#     * 
#   * *
# * * *
#   * *
#     *