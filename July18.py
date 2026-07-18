a =input("Input a number : ")
try:
    a = int(a)
except ValueError:
    print("Please enter a valid integer.")

for i in range(1, a + 1):
    for j in range(1, a+1):
        print((i-1)*a+j, end=" ")
    print()
print()
print(f"The square of {a} is {i*j}")

#This code takes an integer input from the user and prints a square pattern of numbers. It also calculates and prints the square of the input number.