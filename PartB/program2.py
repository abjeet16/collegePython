#2.demonstrate use of advanced regular expression for data validation.

import re
pattern="(?=.{8,20})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%])"
password=input("enter the password")
result=re.findall(pattern,password)
if(result):
    print("valid password")
else:
    print("invalid password")