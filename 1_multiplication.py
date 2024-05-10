# Take two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
 
m=int(input("enter 1st number"))
n=int(input("enter 2nd number"))

def multiplication(m,n):
    return (m*n)
def add(m,n):
    return (m+n)

reselt=multiplication(m,n);
if(reselt > 1000):
    reselt=add(m,n)
    print( " the addition is : ",reselt)
else:
    print("the multiplication is : ",reselt)

