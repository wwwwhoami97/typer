#这是v0.1的box
import tkinter as tk
from turtle import bgpic, speed


#创建一个窗口，标题为“获取设置信息”，大小为300*300，位置为屏幕中央
#窗口中有3个输入框，分别是：文件路径，背景大小，移动速度
#文件路径对应like_typer.turtle.bgpic()
#背景大小对应like_typer.turtle.setup()
#移动速度对应like_typer.turtle.speed()
#窗口中有一个按钮，点击后获取设置信息，并显示在窗口中
#窗口中有一个按钮，点击后关闭窗口



root = tk.Tk()
root.title("如果你改了一个值，那么所有值都要改！")
root.geometry('400x300')                 #是x 不是*

#l1为获取设置信息的窗口中的文本框，输入文件路径w_path
l1 = tk.Label(root, text="背景文件路径(后缀为gif)：")
l1.pack()
w_path_text = tk.StringVar()
w_path=tk.Entry(root, textvariable=w_path_text)
w_path_text.set(" ")
w_path.pack()




#l2为获取turtle.setup()的相关信息，具体为背景的长w_width
l2 = tk.Label(root, text="背景画布的长：")
l2.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
w_width_text = tk.StringVar()
w_width = tk.Entry(root, textvariable = w_width_text)
#w_width_text.set(" ")
w_width.pack()

#l3为获取turtle.setup()的相关信息，具体为背景的宽w_height
l3 = tk.Label(root, text="背景画布的宽：")
l3.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
w_height_text = tk.StringVar()
w_height = tk.Entry(root, textvariable = w_height_text)
#w_height_text.set(" ")
w_height.pack()


#l4为获取turtle.speed()的相关信息，具体为移动速度w_speed

l4 = tk.Label(root, text="速度：")
l4.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
w_speed_text = tk.StringVar()
w_speed = tk.Entry(root, textvariable = w_speed_text )
#w_speed_text.set(" ")
w_speed.pack()

#l5为获取size()的相关信息，具体为文字的大小w_size
l5 = tk.Label(root, text="文字大小：")
l5.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
w_size_text = tk.StringVar()
w_size = tk.Entry(root, textvariable = w_size_text )
#w_speed_text.set(" ")
w_size.pack()


def on_click():
    path_info = w_path_text.get()
    width_info = w_width_text.get()
    height_info = w_height_text.get()
    speed_info = w_speed_text.get()
    size_info=w_size_text.get()
    #将上述变量写入info.xml文件中
    f = open("typer\info.xml", "w")
    f.write("<info>\n")
    f.write("<path>" + path_info + "</path>\n")
    f.write("<width>" + width_info + "</width>\n")
    f.write("<height>" + height_info + "</height>\n")
    f.write("<speed>" + speed_info + "</speed>\n")
    f.write("<size>" + size_info + "</size>\n")
    f.write("</info>\n")
    f.close()

    string = str("背景文件路径：%s 背景画布的长：%s 背景画布的宽：%s 速度：%s 文字大小：%s" %(path_info , width_info, height_info, speed_info, size_info))
    print("背景文件路径：%s 背景画布的长：%s 背景画布的宽：%s 速度：%s 文字大小：%s" %(path_info , width_info, height_info, speed_info, size_info))
    tk.messagebox.showinfo(title='确认你的信息', message = string)
    
tk.Button(root, text="写入", command = on_click).pack()
    
#root.mainloop()
