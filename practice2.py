#Question on slicing
#Taake input and print middle 3 characters , last character

str = input("Enter the value:")
mid = len(str) // 2
output1 = str[mid-1:mid+2]
print(output1)

output2 = str[-2:]
print(output2)