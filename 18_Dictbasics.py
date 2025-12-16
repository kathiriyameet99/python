#Dictionary Basics

students = {
    "Name" : "Patel Raju",
    "City" : "Surat",
    "Age" : 25,
    "RollNumber" : 23
}

print(type(students))
print(students["Name"])
students["City"] = "Hyderabad"
print(students)
students["favSubject"] = "Maths"
print(students)

#removing item

students.pop("favSubject")
print(students)