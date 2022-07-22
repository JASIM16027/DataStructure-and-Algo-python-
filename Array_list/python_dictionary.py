"""
animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"

}
print(animaldict['name','age'])
animaldict['city_name'] = animaldict.pop('City')
animaldict['country_name'] = animaldict.pop('Country')
print(animaldict)

new_dict = {key: animaldict[key] for key in ['name', 'age']}
print(new_dict)

d = {key: animaldict[key] for key in animaldict.keys() - ['age', 'name']}
print(d)

copy_dict = animaldict.copy()
print(id(animaldict)==id(copy_dict))


fruit = {
    'apple': 100,
    'grape': 200,
    'orange': 300,
    'date': 500
}
print('min value key : ', min(fruit, key=fruit.get))
print('max value key : ', max(fruit, key=fruit.get))

print(fruit, '\nfruit length : ', len(fruit))

if 'apple' in fruit:
    del fruit['apple']

print(fruit, '\nfruit length : ', len(fruit))
fruit = {}
print(fruit, '\nfruit length : ', len(fruit))
"""

Fruit = {'Apple': 100, 'banana': 5}

Subject = {'Math': 100, 'English': 98}

animal = {'name': 'Rabbit', 'age': 1}

conacte_Dict = {}

for d in (Fruit, Subject, animal):
    conacte_Dict.update(d)

print(conacte_Dict)
print('sum of Fruit element : ', sum(Fruit.values()))

d = 'I love my country '
string_dict = {}
for word in d:
    string_dict[word] = string_dict.get(word, 0) + 1

print(string_dict)

Dict_tab = {'Students': ['Rack', 'Jack', 'John'],
            'Fruit': ['Apple', 'Banana', 'Orange'], 'Subject': ['Phy', 'Math', 'English']}

for row in zip(*([key] + value for key, value in sorted(Dict_tab.items()))):
    print(*row)

empdict = {'Racx': 12000, 'Max': 80000, 'Stack': 80000, 'John': 80000, 'jasim': 80000}

valuetofind = 80000

total_salary = sum(val for val in empdict.values() if val == valuetofind)
count = sum(val==valuetofind for val in empdict.values())
print('Total salary : ', total_salary)
print('The number of employee : ', count)
