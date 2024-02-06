# Exercises - Dictonary

# 1 Create an empty dictionary called dog
empty_dictionary = {}
print(empty_dictionary)

# 2 Add name, color, breed, legs, age to the dog dictionary
dog_dictionary = {
    'name' : 'Sheru',
    'color' : 'Brown and white',
    'breed' : 'Siberian Husky',
    'legs' : 4,
    'age' : 6,
}

for info, details in dog_dictionary.items():
    print(f"{info.title()} : {details}")

"""3 Create a student dictionary and add first_name, last_name, gender, age,
marital status, skills, country, city and address as keys for the dictionary"""
student = {
    'first_name' : 'Chhayanxi',
    'last_name' : 'Chotaliya',
    'gender' : 'Female',
    'age' : '20',
    'marital status' : 'unmarried',
    'skills' : ['sleeping', 'playing'],
    'country' : 'india',
    'city' : 'rajkot',
    'address' : 'rajkot',
}

# 4 Get the length of the student dictionary
length = len(student)
print(length)

# 5 Get the value of skills and check the data type, it should be a list
skills = student['skills']
data_type = type(skills)
print(data_type)

# 6 Modify the skills values by adding one or two skills
modify_skill = student['skills'].append('gaming')
for value in student['skills']:
    print(value)
print(student)

# 7 Get the dictionary keys as a List
list_keys = list(student.keys())
print(list_keys)

# 8 Get the dictionary values as a list
list_values = list(student.values())
print(list_values)

# 9 Change the dictionary to a list of tuples using items() method
tuple_student = student.items()
print(tuple_student)

# 10 Delete one of the items in the dictionary
deleted_item = student.pop('age')
print(deleted_item)
print(student)

# 11 Delete one of the dictionaries
del student
print(student)