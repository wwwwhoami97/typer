# 0 使用说明
0.ctrl+C需要的文字后打开main.exe,点按启动按钮即可运行
1.背景文件的地址输入绝对地址,地址中不能有中文字符
2.背景文件的后缀不必须是.gif,.jpg也能通过测试
3.按钮通常需要按两次，是因为将报错窗口给屏蔽了
4.设置信息写入dist\main\info.xml,可以直接在此文件中修改设置,该文件不支持中文
5.当发现启动后需要过一段时间才在窗口中显示文字,此为正常现象,问题出自python.turtle库的性能问题
6.若dist\main\info.xml写坏了,可以将typer\info.xml复制进dist/main
7.显示文字遇到空格,逗号,句号才会换行
8.程序生成的是画布,而非窗口,因此不能随着复制的文字的量自适应,可修改画布大小和文字大小
# 1 基本逻辑
获取剪切板最近的内容    pyperclip.paste()
将内容显示在一个背景中
内容要一个字符一个字符显示 
# 2 封装
# 3 GUI
程序启动和暂停
显示剪切板内容和清除内容
改显示字符大小和样式
改背景
# 4 打包
pip3 install pyinstaller


# 版本
## v0.1 day6.17
box获取背景，长，宽，速度写入info.xml
like_typer获取info.xml中的数据
目前字体大小，颜色，样式写死
bug:打包后文件路径找不到  <!--  done:put info.xml into typer\dist\main,pyinstaller at \typer -->

## v0.2 day6.18
target:
1.add: 字体样式，颜色，大小修改功能<!-- done -->
2.add：like_typer.py从box.py启动功能 <!-- done -->
3.add: box显示当前值功能 <!-- done -->