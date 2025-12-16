# Write a program to print the multiplication table of any number using a while loop.

n = int(input("Enter the number: "))

i = 1
while(i <= 10):
    print(f"{n} x {i} = {n * i}")
    i = i + 1 
    