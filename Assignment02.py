# #Data type

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

print("Your name is:",name)
print("Your age is:",age)

print(type(name))
print(type(age))

# #Operator

a = 5
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Coding :- smart tempreture converter

celsius = float(input("Enter the celsius: "))

Fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.5

print("The fahrenheit value is: ",Fahrenheit)
print("The kelvin value is: ",kelvin)


#Bill split calculator

total_bill = float(input("Enter the total bill amount: "))

friends = 4

per_person = total_bill / 4

print("The per-person bill amount is: ",per_person)
