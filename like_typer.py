#turtle
import turtle
import time
from read_clip import read_clip
#coding=utf-8
import  get_info as gi


def run_words():

    #setup()参数使用info.xml中width和height
    turtle.setup(int(gi.width_info_1),int(gi.height_info_1))
    #读取info.xml里的<path>

    turtle.bgpic(gi.bgpic_info_1)#背景图像的文件路径
    turtle.hideturtle() 
    turtle.speed(float(gi.speed_info_1))
    turtle.penup()
    #改颜色
    turtle.color(gi.color_info_1)

    size=int(gi.size_info_1)#文字大小

    line=read_clip()
    words=list(line)

    row=line.count(" ")
    y=size*1.5*row/2
    x=-7*size*1.5/2

    turtle.goto(x,y)



    #依次打字，遇到空格或者逗号或者句号，换行
    for word in words:
        if word==" ":
            #出现空格或者句号或逗号，在绘制完他们之后再goto
        
            
            y-=size*1.5
            turtle.goto(x,y)
            
        turtle.write(word,align="center", font=(gi.shape_info_1, size, "normal"))#华文行楷，黑体，宋体，楷体
        #改变背景
        """ turtle.bgcolor("green") """
        time.sleep(float(gi.speed_info_1))
        turtle.forward(size*1.5)

    turtle.done()

""" run_words() """

