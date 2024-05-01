num = int(input("enter the table you wanna generate"))
for j in range(1,num+1):
    for i in range(0,11):
        print(f"{j} x {i} = {j*i}")