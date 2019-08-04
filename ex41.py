'''
 学习面向对象术语
 --------------------------------------------
 专有词汇练习
 类（class）
 对象（object）
 实例(instance)
 def :这是在类里边定义函数的方法
 self：在类的函数中，self指代被哦访问的对象或者实例的一个变量
 继承（inheritance）:指一个类可以继承另一个类的特性，和父子关系类似
 组合（composition）:指一个类可以别的类作为它的部件构建起来，有点像车子和车轮的关系
 属性（attribute）：类的一个属性，它来自于组合，而且通常是一个变量
 是什么（is-a):用来描述继承关系，如：cat is an animal
 有什么（has-a):用来描述某个东西是由另外一些东西组成的，或者某个东西有某个特征，如 cat有尾巴
'''

'''
 class X(Y):  创建一个叫X的类，它是Y的一种
 class X(object): def __init__(self,J):类X有一个__init__,它接收self和J作为参数
 class X(object): def M(self,J) : 类X有一个名为M的函数，它接收self和J作为参数
 foo = X():将foo设为类X的一个实例
 foo.M(J):从foo中找到M函数，并使用self和J参数调用它
 foo.K = Q: 从foo中获取K属性，并将其设为Q
'''

import random
from urllib.request import   urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\t def ***(self,@@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "eiglish":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS,snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS,param_count)
        ))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%",word,1)   # replace 函数  replace(old,new,max)  max最大不超过的次数

        # fake other names
        for word in other_names:
            result = result.replace("***",word,1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@",word,1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question
            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
