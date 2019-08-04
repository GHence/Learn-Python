'''
 第一个类的例子
'''


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

'''
 1、Python3 创建了一个空对象，里面包含了你在该类中用def指定的所有函数
 2、然后python去检查你是不是在里边创建了一个__init__ “魔法函数”  如果创建了
 他就会调用这个函数，从而对你新创建的空对象实现初始化
 3、在Song的__init__函数里，有一个多余的函数叫self  这就是Python为你创建的空对象，而
 你可以对它进行类似模拟、字典等操作，为它设置一些变量
'''