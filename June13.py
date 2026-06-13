# Triangle pattern using list
get = int(input("Enter a number : "))
list = [get]
for k in range(1, get):
    list.append(get - k)
# Here we can make a nessary list based on the user input, like input, input - 1, input -2,...,1
# to add a new element to the list we can use append() method and to remove an element we can use remove() method

j = len(list)
for i in range(len(list)):
    print(list)
    list.remove(list[j-1])
    j = j-1
# Here we use append method to remove the last element of the array