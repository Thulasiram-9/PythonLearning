#find the remainder when a number is divided by 2
a = int(input("Enter a number : "))
mod = a % 2
if mod == 0:
    print("The remainder is 0, the number is even.")
else:
    print("The remainder is 1, the number is odd.")