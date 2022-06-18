""" 这是0.2用box """



#from re import L
import tkinter as tk
#from turtle import right
import get_info as gi
import like_typer as lt



#创建一个窗口，标题为“获取设置信息”，大小为300*300，位置为屏幕中央
#窗口中有3个输入框，分别是：文件路径，背景大小，移动速度
#文件路径对应like_typer.turtle.bgpic()
#背景大小对应like_typer.turtle.setup()
#移动速度对应like_typer.turtle.speed()
#窗口中有一个按钮，点击后获取设置信息，并显示在窗口中
#窗口中有一个按钮，点击后关闭窗口



root = tk.Tk()
root.title("注意：如果你改了一个值，那么所有值都要改！")
root.geometry('600x400')                 #是x 不是*

#l1为获取设置信息的窗口中的文本框，输入文件路径w_path
l1 = tk.Label(root, text="背景文件路径(后缀为gif)：")
l1.pack()
w_path_text = tk.StringVar()
w_path=tk.Entry(root, textvariable=w_path_text)
w_path_text.set("")
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

#l6为获取color()的相关信息，具体为文字的颜色w_color
l6 = tk.Label(root, text="文字颜色：(输入颜色的英文单词)")
l6.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
w_color_text = tk.StringVar()
w_color = tk.Entry(root, textvariable = w_color_text )
#w_speed_text.set(" ")
w_color.pack()


#设置一个下拉菜单，用于选择要显示的文字样式
#C7为获取shape()的相关信息的下拉列表框，具体为文字的样式w_shape
l7 = tk.Label(root, text="文字样式：")
w_shape_text = tk.StringVar()
C7 = tk.OptionMenu(root, w_shape_text, "宋体", "华文楷体", "华文隶书", "华文细黑", "华文行楷")
l7.pack() #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
C7.pack()

#box中的label:box_text，显示上述获取的设置信息的当前值
#box_text位置靠右
#box的文字均可被选中
box_text = tk.Label(root, text = "当前设置：")
box_text.place(x=20, y=20)

#box_bgpic，显示当前的背景图片路径
box_bgpic = tk.Label(root, text = "图片路径："+gi.bgpic_info_1)
box_bgpic.place(x=20, y=50)
#box_width
box_width = tk.Label(root, text = "画布的长："+gi.width_info_1)
box_width.place(x=20, y=80)
#box_height
box_height = tk.Label(root, text = "画布的宽："+gi.height_info_1)
box_height.place(x=20, y=110)
#box_speed
box_speed = tk.Label(root, text = "移动速度："+gi.speed_info_1)
box_speed.place(x=20, y=140)
#box_size
box_size = tk.Label(root, text = "文字大小："+gi.size_info_1)
box_size.place(x=20, y=170)
#box_color
box_color = tk.Label(root, text = "文字颜色："+gi.color_info_1)
box_color.place(x=20, y=200)
#box_shape
box_shape = tk.Label(root, text = "文字样式："+gi.shape_info_1)
box_shape.place(x=20, y=230)



def restart_click():
    #此按钮重启程序
    lt.run_words()




def on_click():
    path_info = w_path_text.get()
    width_info = w_width_text.get()
    height_info = w_height_text.get()
    speed_info = w_speed_text.get()
    size_info=w_size_text.get()
    color_info=w_color_text.get()
    shape_info=w_shape_text.get()
    while shape_info=="宋体":
        shape_info="STSONG"
    while shape_info=="华文楷体":
        shape_info="STKAITI"
    while shape_info=="华文隶书":
        shape_info="STLITI"
    while shape_info=="华文细黑":
        shape_info="STXIHEI"
    while shape_info=="华文行楷":
        shape_info="STXingkai"
    

    #将上述变量写入info.xml文件中
    #如果检测到输入为空，则保持原值，否则更新值
    if path_info == "":
        path_info = gi.bgpic_info_1
    if width_info == "":
        width_info = gi.width_info_1
    if height_info == "":
        height_info = gi.height_info_1
    if speed_info == "":
        speed_info = gi.speed_info_1
    if size_info == "":
        size_info = gi.size_info_1
    if color_info == "":
        color_info = gi.color_info_1
    if shape_info == "":
        shape_info = gi.shape_info_1
    

    f = open("info.xml", "w") 
    f.write("<info>\n")
    f.write("<path>" + path_info + "</path>\n")
    f.write("<width>" + width_info + "</width>\n")
    f.write("<height>" + height_info + "</height>\n")
    f.write("<speed>" + speed_info + "</speed>\n")
    f.write("<size>" + size_info + "</size>\n")
    f.write("<color>" + color_info + "</color>\n")
    f.write("<shape>" + shape_info + "</shape>\n")
   
    f.write("</info>\n")
    f.close()

    string = str("背景文件路径：%s 背景画布的长：%s 背景画布的宽：%s 速度：%s 文字大小：%s 文字颜色:%s 文字样式:%s"%(path_info , width_info, height_info, speed_info, size_info, color_info, shape_info))
    print("背景文件路径：%s 背景画布的长：%s 背景画布的宽：%s 速度：%s 文字大小：%s 文字颜色:%s 文字样式:%s"%(path_info , width_info, height_info, speed_info, size_info, color_info, shape_info))
    tk.messagebox.showinfo(title='确认你的信息', message = string)
    
tk.Button(root, text="写入(退出后才生效)", command = on_click).pack(side=tk.RIGHT)
tk.Button(root, text="退出", command = root.quit).pack(side=tk.RIGHT)
tk.Button(root, text="启动(可能要点两次)", command = restart_click).pack(side=tk.RIGHT)
    
#root.mainloop()
