my_dictionary = {
    "Name": "Cindy",
    "Gender": "Annette",
    "School": "School of Engineering"}

my_dictionary = dict(
        Name="Cindy",
        gender="Female",
        school="School of Economics")
print(my_dictionary)
print(my_dictionary['Name'])
print(my_dictionary["Gender"])
my_dictionary["Gender"] = 'Female'
print(my_dictionary)
my_dictionary['Birthday'] = '18'
print(my_dictionary)

my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary2))

my_dictionary.pop('Gender') #removes the Gender
del my_dictionary
print(my_dictionary2)

for value in my_dictionary2:
    print(my_dictionary2[value])

for key in my_dictionary2:
    print(key) #print the dict key

for key,value in my_dictionary2.items():
    print(key, value) #prints the dict key and value