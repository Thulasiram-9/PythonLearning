# This program takes a number in words as input and prints the corresponding number. The user can exit the program by entering "Q".
def one():
    print("1")

def two():
    print("2")

def three():
    print("3")

def four():
    print("4")

tweak =input("Enter a number in words: ")
while tweak != "Q":
    if tweak=="one":
        one()
    elif tweak=="two":
        two()
    elif tweak=="three":
        three()
    elif tweak=="four":
        four()
    elif tweak=="Q":
        print("Exiting...")
        break
    tweak = input("Enter a number in words: ")
else:
    print("Invalid input")