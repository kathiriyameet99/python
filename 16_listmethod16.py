#Method in list

#indexing 

marks = [99, 100, 90, 95]
print(marks[1])

marks[1] = 98
print(marks)

#Slicing
print(marks[1:3])


#min and max marks
print(min(marks))
print(max(marks))

#Append value
marks.append(92)
print(marks)

#Sorted value

marks.sort()
print(marks)

#Pop remove element
marks.pop(1)
print(marks)

#insert and remove element

marks.remove(99)
print(marks)

marks.insert(1, 100)
print(marks)