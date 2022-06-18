#读取最新的剪切板内容
import pyperclip

def read_clip():
    read_content=[]
    read_content=pyperclip.paste()
    #对read_content进行处理，去除换行符，替换符号为空格
    read_content=read_content.replace("\n"," ")
    read_content=read_content.replace(","," ")
    read_content=read_content.replace("，"," ")
    read_content=read_content.replace("."," ")
    read_content=read_content.replace("。"," ")
    #在read_content的开头插入一个空格，以便从第一个字符开始绘制
    read_content=" "+read_content
    return read_content




