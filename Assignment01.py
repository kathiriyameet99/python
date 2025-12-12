#Question :- Take diameter as input and calculate the area of a circle

Diameter = int(input("Enter the value of the diameter: "))

radius = Diameter/2
area = 3.14 * (radius ** 2)
print(f"The area of circle is:{area}")