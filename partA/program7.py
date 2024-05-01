#7)create a calculator program

num1=float(input("enter number1"))
num2=float(input("enter number2"))
print("1.addition")
print("2.subtract")
print("3.multiplication")
print("4.division")
choice=int(input("enter the choice 1-4:"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1 * num2)
elif choice==4:
    if num2==0.0:
            print("divide by zero error")
    else:
            print(num1/num2)
else:
     print("invalid choice entry")