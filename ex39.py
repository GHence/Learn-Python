'''
 字典，可爱的字典
'''

# things = ['a','b','c','d']
# print(things[1])
#
# print("-----------------------")
# things[1] = 'z'
# print(things[1])
#
# print("---------------------")
# print(things)

# stuff = {'name':'Zed','age':39,'height':6*12+2}
# print(stuff['name'])
# print(stuff['age'])
# print(stuff['height'])
#
# stuff['city'] = 'SF'
# print(stuff['city'])
#
# del stuff['city']
# # del stuff[1]
# # del stuff[2]
# print(stuff)

'''
字典的例子   P121
'''

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print('NY State has:',cities['NY'])
print('OR State has:', cities['OR'])

# print some state
print('-'*10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"abbrev has the city {city}")

# now do both at the same time
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
# safely grt a abbrevistion by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')

print(f"The city for the state 'TX' is {city}")
