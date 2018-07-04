from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that,hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

# input()
input("?")           # 输入提示

print("Opening the file...")
target = open(filename,'w')        # 以写的方式打开文件

print("Truncating the file. Gooodby!")
target.truncate()                  # truncate 截断  第哦啊用trucate()函数，将输入的字符串写入文件中

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")                   # 提示line 1：让你输入一行字符串
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to wwrite these to the file.")

target.write(line1)                       # 将第一行的数据写入到filename文件中
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()                           # 读完之后 调用close函数