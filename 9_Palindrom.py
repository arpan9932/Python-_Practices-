# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

num=int(input("enter a number : "))
n=num
sum=0
while(n>0):
    rem=n%10
    sum=(sum*10)+rem
    n=int(n/10)

if(num==sum):
    print(num , " is a palidrom number.")
else:
    print(num," is not a palidrom number.")

