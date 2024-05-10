# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False

def compair(numberlist):
    first=numberlist[0]
    last=numberlist[-1]
    if(first==last) : 
        return True
    else:
        return False

numList=[10,20,40,10]
print("the list is : ",numList)
print("The result is : ",compair(numList))