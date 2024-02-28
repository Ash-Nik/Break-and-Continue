# Write a program to skip printing even numbers using a while loop.
print("Enter the range of number ")
x = int(input("PLease enter the first number = "))
y = int(input("Please enter the second number = "))
while x < y:
    if x % 2 != 0:
        print(x)
    x += 1
