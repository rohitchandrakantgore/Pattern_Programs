height= int(input("Enter  Height: "))

for i in range(height):
    print(" "*(height-i-1)+"* "*(i+1))
for i in range(height,0,-1):
    print(" "*(height-i+1)+"* "*(i-1))
    
# Enter  Height: 5
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *