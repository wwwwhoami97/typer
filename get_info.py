import  xml.dom.minidom

dom = xml.dom.minidom.parse('info.xml')
        #得到文档元素对象
root = dom.documentElement
bgpic_info=root.getElementsByTagName('path')
bgpic_info_1=bgpic_info[0].childNodes[0].data
        #去除字符串中的空格
bgpic_info_1=bgpic_info_1.replace(" ","")

width_info=root.getElementsByTagName('width')
width_info_1=width_info[0].childNodes[0].data

height_info=root.getElementsByTagName('height')
height_info_1=height_info[0].childNodes[0].data

speed_info=root.getElementsByTagName('speed')
speed_info_1=speed_info[0].childNodes[0].data

size_info=root.getElementsByTagName('size')
size_info_1=size_info[0].childNodes[0].data
        #暴力极了，一点都不优雅
color_info=root.getElementsByTagName('color')
color_info_1=color_info[0].childNodes[0].data

shape_info=root.getElementsByTagName('shape')
shape_info_1=shape_info[0].childNodes[0].data