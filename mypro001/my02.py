import turtle   #导入模块

turtle.showturtle()     #显示箭头
turtle.write("小鸭，你好")
turtle.forward(300)     #前进300个像素
turtle.color("red")     #改变画笔的颜色为red
turtle.left(90)         #箭头左转90度
turtle.forward(300)
turtle.goto(0,0)        #回到坐标系原点
turtle.penup()          #抬起笔，路径就不会画出来
turtle.goto(0,50)
turtle.pendown()
turtle.circle(100)

turtle.done()           #程序结束，可以保持窗口一直在