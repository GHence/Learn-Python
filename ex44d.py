class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

print("第一组Parent和son")
dad.implicit()
print("--------------------")
son.implicit()

print("第二组Parent和son")
dad.override()
print("--------------------")
son.override()

print("第三组Parent和son")
dad.altered()
print("--------------------")
son.altered()
