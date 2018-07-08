'''
 列表的操作

'''

ten_things = "Apples Orange Crows Telephone Light Sugar"

print("Wait there are not 10 thing in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee",
              "Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:",stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])   # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))   # what? cool
print('#'.join(stuff[3:5]))   # super stellar!


'''
 本段代码主要讲了 列表、 append()函数  pop函数（类似与栈的操作） split()分割函数  join()函数 
 还涉及到python的切片操作
 
 split()调用方式  stuff.split(' ')
 append()函数调用方法 stuff.append(next_one)
 join函数的调用方法为 ''.join(stuff)
'''