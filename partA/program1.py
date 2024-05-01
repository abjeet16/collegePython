n=int(input('enter the number'))
c=0
a=1
b=1
if n==0 or n==1:
    print(n,'is a fibonnaci number')
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print(n,'is a fibonnaci number')
    else:
        print(n,' is not a fibonnaci number')