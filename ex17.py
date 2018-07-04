from sys import argv
from os.path import exists
'''
本示例就是通过open(from_file)函数读取一个文件  然后用open(to_file,'w')写入到out_file
最后关闭掉 out_file 和 in_file 
'''
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# we  could do these two on one line,how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist?{exists(to_file)}")
print("Ready,hit RETRUN to continue,CTRL-C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright,all done.")

out_file.close()
in_file.close()