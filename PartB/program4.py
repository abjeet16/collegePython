#Demonstrate use of dictionaries.

currency = {"India": "Rupee", "USA": "Dollar", "Russia": "Ruble"}
print("List of Countries")
for key in currency.keys():
     print(key)
print("List of Currencies in different Countries")
for value in currency.values():
     print(value)
print('list of countries along with their currencies')
for key,value in currency.items():
     print(f"{key},'has a currency of type'{value}")
currency.update({'germany':'euro'})
print(currency)