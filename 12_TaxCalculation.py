#  Calculate income tax for the given income by adhering to the rules below
# TaxableIncome	    Rate (in %)
# First  $10,000	    0
# Next $10,000	        10
# The remaining     	20

income=int(input("Please enter your income : "))
if income<=10000 : 
    tax=0
elif income<=20000 : 
    tax=(income-10000)*(10/100)
else : 
    tax=(10000*(10/100))+((income-20000)*(20/100))

print("The payble tax is : ",tax)