#Q. Write a program that takes total bill amount and number of friends as input.
#Calculate how much each friend will pay.
#Also print the data type of each variable used.
#{Use float() and division operator}

#<CODE STARTS>

Total_bill_Amount=float(input("Enter the Total Bill Amount:"))
Total_Friends=int(input("How many friends:"))
x=Total_bill_Amount/Total_Friends
print("Each friend will pay:",x)
print("the data type of Total Bill Amount is:",type(x))


