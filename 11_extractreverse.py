# Write a Program to extract each digit from an integer in the reverse order.

num=int(input("enter a number : "))
n=num
sum=0
while(n>0):
    rem=n%10
    print(rem,end=" ")
    n=int(n/10)