# Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

n=5
for x in range(0,n):
    for y in range(n-x,0,-1):
        print("*",end=" ")
    print("\n")