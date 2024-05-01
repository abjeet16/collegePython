#1.Demonstrate usage of basic regular expression

import re

str = ' Rahul got 75 marks,Vijay got 56 marks'
marks = re.findall('\d{2}', str)
print(marks)
names = re.findall('[A-Z][a-z]*', str)
print(names)
result = re.search('R\w\w\w\w', str)
print(result.group())