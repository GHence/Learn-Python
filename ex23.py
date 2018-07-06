from sys import argv
script, encoding, error = argv    # 命令行参数处理


def main(language_file, encoding,errors):
    line = language_file.readline()            # 就是用readline（）处理文本
    if line:                                   # 防止函数永远循环下去
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):     # 对languages.txt中的每一行进行编码
    next_lang = line.strip()     # 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    raw_bytes = next_lang.encode(encoding,errors = errors)
    cooked_string =  raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>",cooked_string)

languages = open("language.txt",encoding = "utf-8")

main(languages, encoding, error)
