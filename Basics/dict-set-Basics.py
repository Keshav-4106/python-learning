# Dictionary Basics

student = {
    "name":    "Keshav Somani",
    "class":   "12th",
    "age":       22,
    "subject":  "Commerce",
    "rollNo":    "11",
    "city":     "Bassi",
    "name":     "Soumya",
    "name1":     "Shreya",
}

print(type(student))
print(student["name"])
print(student)
print(student["subject"])
print(student["city"])
student["city"]="Hyderabad"
print(student)
student["favSubject"]="Accounts"
print(student)
student.pop("name1")
print(student)
print(student.values())
print(student.keys())
print(student.get("favSubject"))
print(student.items())

# Practice Question 1 Create a dictionary named marks to store marks of 3 subjects.
#  Add the subjects one by one and print the final dictionary. 

marks = {}

marks[ "Accounts"] =  99
marks["Busines Studies"] = 92
marks["Economics"] = 96
print(marks)



# Sets Basics

languages = {"Python", "Java", "C++", "Python"} 
print(languages)
 # Output: {'C++', 'Java', 'Python'}


#Creating a Set 
empty_set = set()      # Empty set
nums = {1, 2, 3, 4}    # Non-empty set 

#Adding and Removing Elements
nums = {1, 2, 3}
nums.add(4)
nums.remove(2)
print(nums)   # {1, 3, 4} 


# Practice Question 
#You are given a list of programming languages: ["Python", "Java", "C++", "Python", "Java", "C"] 
# Convert it into a set and print how many unique languages Divya knows. 


programmingList=["Python","Java","C++","Python","Java","C"]
print(type(programmingList))

# How to convert list into set 

programmingSet= set(programmingList)
print(type(programmingSet))
print("Divya knows these languages",len(programmingSet))



