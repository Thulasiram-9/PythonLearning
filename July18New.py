a = input("Enter a number : ")
try:
    a = int(a)
except ValueError:
    print("Please enter a valid integer.")

for i in range(1, a+1):
    print(a*"*", end="")
    print()