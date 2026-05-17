food=["Choco Waffales","Mango","Masala Dosa","Gulab Jamun","Lazania French Pasta"]

print(len(food))        #size of the list

print("first value of mylist:",food[0])     #access the indexing value
print("first value of mylist:",food[3])


#Methods in list

#INDEXING
#Lists are MUtable
marks = [89,100,92,78,83]

marks[1] = 99
print(marks)


#STRINGS are IMMUTABLE 
#name="Saumya"
#name[1] ="o"
#print(name)



#Slicing
print(marks[1:3] )

print(max(marks) )

print(min(marks) )

#Lists Methods

marks.append(62)
print(marks)
marks.sort()
print(marks)
marks.remove(92)
print(marks)
marks.pop(2)
print(marks)
marks.insert(1,92)
print(marks)
marks.reverse()
print(marks)

#Write a program that takes names of 3 favorite foods from the user and stores them in a list. Then print the list and its length. 

food1=input("Enter Your First Favourite Food Name:")
food2=input("Enter Your Second Favourite Food Name:")
food3=input("Enter Your Third Favourite Food Name:")


#method-1 to print like this,
list=[]
list.append(food1)
list.append(food2)
list.append(food3)
print(list)

print(len(list))

# method-2 to print like this

foodlist=[food1,food2,food3]

print(foodlist)

print(len(food))
