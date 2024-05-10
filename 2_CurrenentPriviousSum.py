# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

current=0
prev=0
print("Printing current and previous number sum in a range(10)")
while(current<10):
    print("Current Number : ",current," Previous Number : " , prev,"  Sum: ", (current+prev))
    prev=current
    current=current+1



