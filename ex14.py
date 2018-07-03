from sys import argv
'''
PS E:\dev\code\笨方法学python3> python ex14.py Zed
Hi Zed,I'm the ex14.py script.'
I'd like to ask ypu a few questions.
Do ypu like me Zed?
>yes
Where do ypu live Zed?
>yicheng
What kind of computer do you have?
>Dell
'''
script , user_name = argv
prompt = '>'

print(f"Hi {user_name},I'm the {script} script.'")
print("I'd like to ask ypu a few questions.")
print(f"Do ypu like me {user_name}?")
likes = input(prompt)

print(f"Where do ypu live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
''')