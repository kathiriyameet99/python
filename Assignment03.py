#Ask the user for their 3 favorite movies and store them in a list.

movie1 = input("Enter the movie1:")
movie2 = input("Enter the movie2:")
movie3 = input("Enter the movie3:")

movie_list = [movie1, movie2, movie3]

print(movie_list)

#Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min().

marks = (87, 64, 33, 95, 76)

print(min(marks))
print(max(marks))


#Write a program to check grade based on marks (A/B/C/D) using if-elif-else.

marks = int(input("Enter the marks number:"))

if(marks >= 90):
    print("Your grade is A")
elif(marks >= 80):
    print("Your grade is B")
elif(marks >= 70):
    print("Your grade is C")
elif(marks >= 60):
    print("Your grade is D")
else:
    print("You are fail.")

