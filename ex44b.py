'''
显示覆盖
隐式调用函数有一个问题就是，有时候，你需要让子类里的函数有不同的行为，这种情况下隐私继承是做不到
这时你需要覆盖子类中的函数，让她实现新的功能。具体做法：
在子类child中定义一个同名的函数就可以了。
'''
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()



