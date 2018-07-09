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

stuff = {'name':'Zed','age':39,'height':6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = 'SFa'
print(stuff['city'])

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)