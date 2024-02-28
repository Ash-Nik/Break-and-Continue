# Write a program to iterate through a list and stop when encountering a specific element.
specific_element = 9
lst = [1, 2, 3, 6, 93, 2, 5, 9, 5, 3, 2]
for i in lst:
    if i == specific_element:
        break
    print(i)
