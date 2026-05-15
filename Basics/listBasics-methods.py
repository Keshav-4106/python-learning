food=["Choco Waffales","Mango","Masala Dosa","Gulab Jamun","Lazania French Pasta"]

print(len(food))        #size of the list

print("first value of mylist:",food(0))     #access the indexing value
print("first value of mylist:",food(3))


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
 

