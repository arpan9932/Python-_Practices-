# Iterate the given list of numbers and print only those numbers which are divisible by 5

numList=[]
n=int(input("enter total number of element want to enter : "))
print("Enter ",n," numbers : ")
for i in range(0,n):
    x=int(input())
    numList.append(x)
print("the numbers devisable by 5 are : ")
for i in range(0,n):
    if(numList[i]%5==0):
        print(numList[i])
