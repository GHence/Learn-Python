'''
要用super（）的原因
python支持多继承
class SuperFun(Child, BadStuff):
    pass
'''

'''
super()和__init__搭配使用
'''

# class Child(Parent):
#
#     def __init__(self):
#         self.stuff = stuff
#         super(Child, self).__init__()
#  组合

class Other(object):

    def override(self):
        print("other override()")

    def implicit(self):
        print("other implicit()")

    def altered(self):
        print("other altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()
