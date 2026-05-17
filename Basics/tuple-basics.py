# Create a tuple of your favorite 5 fruits. Then print: 1. The total number of fruits 2. The index of one selected fruit 
favfood=("Mango","Pineapple","Lichi","Pomegranate","Watermelon")



print(favfood)
print("Total favourite food =" ,len(favfood))
print("Index of Watermelon =",favfood.index("Watermelon"))



#PRACTICE ASSIGNMENT [1. Ask the user for their 3 favorite movies and store them in a list and then print.
#  2. Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min().
#  3. Write a program to check grade based on marks (A/B/C/D) using if-elif-else. ]


movie1=input("Enter Yiur First Movie Name=")
movie2=input("Enter Your Second Movie Name=")
movie3=input("Enter Your Third Movie Name=")


movielist=(movie1,movie2,movie3)
print(movielist)


marks=(87,64,33,95,76)
print(max(marks))
print(min(marks))


if(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("Grade B")
elif(marks>=60):
    print("Grade C")
else:
    print("Grade D")


