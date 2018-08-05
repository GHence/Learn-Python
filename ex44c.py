'''
首先像上例一样覆盖函数，不过接着用Python的内置函数 super来调用
父类Parent里的版本
'''

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
print("-----------------------------")
son.altered()
