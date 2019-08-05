'''
你的第一个网站

运用flask 编写一个简单的“Hello World”项目
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
