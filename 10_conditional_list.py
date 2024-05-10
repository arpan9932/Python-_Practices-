# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3=[]
n=len(list1)
for i in range(0,n):
    if(list1[i]%2!=0):
        list3.append(list1[i])

for i in range(0,n):
    if(list2[i]%2==0):
        list3.append(list2[i])

print(list3)