import cmath
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
if d>0:
    print('two distinct real roots')
elif d==0:
    print('two equal real roots')
else:
    print('two complex roots')
print(f"the solutions are {sol1} and {sol2}")