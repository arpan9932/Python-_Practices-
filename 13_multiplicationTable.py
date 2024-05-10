# Print multiplication table from 1 to n(user input)

n=int(input("Enter how many table want to print :"))

for x in range(1,n+1):
    sum=0
    print(x,end=" ")
    for y in range(0,10):
        sum=sum+x
        print(sum,end=" ")
    
    print("\n")
        