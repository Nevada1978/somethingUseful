import os
selectPath = input("请输入新建文件名\n")
def text_create(name):
	# 自动获取桌面路径
    desktop_path = os.path.join(os.path.expanduser('~'),"Desktop/")
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    return full_path

currentFilePath = text_create(selectPath)
currentFilePath_1 = text_create(selectPath+'1')

# 删除桌面已存在的my_txt文件
# os.remove(currentFilePath)
# os.remove(currentFilePath_1)

# 文本注释：
print("1.请确保文本是.txt格式\n")
print("2.请确保编码是UTF-8\n")
print("3.您的my_txt文件将在桌面上被创建\n")
print("4.仅支持中英文已分开的文档\n")
fileName = input("请输入你的txt文本路径（绝对路径）（请不要包含任何引号）\n")

# coding = utf-8
def is_chinese(strings):
    for _char in strings:
        if '\u4e00' <= _char <= '\u9fa5':
            return True

with open(fileName, mode="r+", encoding="utf-8") as file:
    for line in file:
        if is_chinese(line):
            with open(currentFilePath, mode='a', encoding='utf-8') as mon:
                mon.write(line)

def clearBlankLine():

    file1 = open(currentFilePath, 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open(currentFilePath_1, 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()

if __name__ == '__main__':
    clearBlankLine()
