#lcm finder
#Getting inputs
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b :
    predic=a   
else:
    predic=b
#so predic means prediction it may be the LCM if a and b are factors of predic
while True:
    if predic%a==0 and predic%b==0 :
        print(f"The lcm of {a} and {b} is : {predic}")
        break#if not then we'll move to next number
    predic=predic+1