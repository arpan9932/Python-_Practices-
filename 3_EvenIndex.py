# Write a program to accept a string from the user and display characters that are present at an even index number.

str=input("enter a string : ")
n=len(str)
for x in range (0,n):
     if(x%2==0):
         print(str[x])