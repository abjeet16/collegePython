#8)Explore string functions

str='this is  core python class'
print(str.capitalize())
print(str.count('c',0,len(str)))
print(len(str))
print(str.startswith('t',0,len(str)))
print(str.endswith('e',0,len(str)))
print(str.isupper())
print(str.islower())
print(str.upper())
print(str.lower())
print(str[0:5])
print(str[::])
print(str.split())
str1=['course','bca']
str2=':'.join(str1)
print(str2)