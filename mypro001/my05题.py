
num = input("输入一个数字: ")
if int(num) < 10:
    print("小于10的数:"+num)

if 3:
    print("ok")
a = []
if a:
    print("空列表，False")
s = "False"
if s:
    print("非空字符串，是True")
c = 9
if 3 < c < 20:
    print("3<c<20")
if 3 < c and c < 20:
    print("3<c and c<20")
if True:
    print("True")

num = input("输入一个数字：")
if int(num)<10:
    print(num)
else:
    print("数字太大")

# 三元条件运算符
num = input("请输入一个数字")
print(num if int(num) < 10 else "数字太大")

"""
输入一个学生的成绩，将其转化成简单描述：
不及格(小于60)、及格(60-79)、良好(80-89)、优秀(90-100)
"""
score = int(input("请输入分数"))
grade = ''
if(score<60):
   grade = "不及格"
if(60<=score<80):
   grade = "及格"
if(80<=score<90):
   grade = "良好"
if(90<=score<=100):
   grade = "优秀"
print("分数是{0},等级是{1}".format(score, grade))

score = int(input("请输入分数"))
grade = ''
if score< 60:
   grade = "不及格"
elif score < 80:
   grade = "及格"
elif score < 90:
   grade = "良好"
elif score <= 100:
   grade = "优秀"
print("分数是{0},等级是{1}".format(score, grade))

x = int(input("请输入x坐标"))
y = int(input("请输入y坐标"))
if(x==0 and y==0):print("原点")
elif(x==0):print("y轴")
elif(y==0):print("x轴")
elif(x>0 and y>0):print("第一象限")
elif(x<0 and y>0):print("第二象限")
elif(x<0 and y<0):print("第三象限")
else:
   print("第四象限")

score = int(input("请输入一个在0-100之间的数字："))
degree = "ABCDE"
num = 0
if score > 100 or score < 0:
   score = int(input("输入错误！请重新输入一个在0-100之间的数字："))
else:
   num = score//10
   if num < 6:
       num = 5
print("分数是{0},等级是{1}".format(score, degree[9-num]))

num = 0
sum_all = 0         # 1-100所有数的累加和
while num <= 100:
   sum_all += num
   num += 1         # 迭代，改变条件表达式，使循环趋于结束
print("1-100所有数的累加和", sum_all)

for x in (20, 30, 40):
   print(x*3)

for x in "sxt001":
   print(x)

d = {'name': 'gaoqi', 'age': 18, 'address': '西三旗001号楼'}
for x in d:              # 遍历字典所有的key
   print(x)
for x in d.keys():       # 遍历字典所有的key
   print(x)
for x in d.values():     # 遍历字典所有的value
   print(x)
for x in d.items():      # 遍历字典所有的"键值对"
   print(x)

"""
利用for循环，计算1-100之间数字的累加和；
计算1-100之间偶数的累加和，计算1-100之间奇数的累加和。
"""
sum_all = 0         # 1-100所有数的累加和
sum_even = 0        # 1-100偶数的累加和
sum_odd = 0         # 1-100奇数的累加和
for num in range(101):
   sum_all += num
   if num % 2 == 0: sum_even += num
   else: sum_odd += num
print("1-100累加总和{0},奇数和{1},偶数和{2}".format(sum_all, sum_odd, sum_even))

# 利用嵌套循环打印九九乘法表
for m in range(1, 10):
   for n in range(1, m+1):
       print("{0}*{1}={2}".format(m, n, (m*n)), end="\t")
   print()

r1 = dict(name="高小一", age=18, salary=30000, city="北京")
r2 = dict(name="高小二", age=19, salary=20000, city="上海")
r3 = dict(name="高小三", age=20, salary=10000, city="深圳")
tb = [r1, r2, r3]
for x in tb:
   if x.get("salary") > 15000:
       print(x)

while True:
   a = input("请输入一个字符（输入Q或q结束）")
   if a.upper() == 'Q':
       print("循环结束，退出")
       break
   else:
       print(a)

"""
要求输入员工的薪资，若薪资小于0则重新输入。
最后打印出录入员工的数量和薪资明细，以及平均薪资
"""
empNum = 0
salarySum = 0
salarys = []
while True:
   s = input("请输入员工的薪资（按Q或q结束）")
   if s.upper() == 'Q':
       print("录入结束")
       break
   if float(s) < 0:
       print("无效！继续录入！")
       continue
   print("录入成功！")
   empNum += 1
   salarys.append(float(s))
   salarySum += float(s)
print("员工数{0}".format(empNum))
print("录入薪资：",salarys)
print("总发薪资：",salarySum)
print("平均薪资{0}".format(salarySum/empNum))

# 测试zip()并行迭代
names = ("高淇", "高老二", "高老三", "高老四")
ages = (18, 16, 20, 25)
jobs = ("老师", "程序员", "公务员")
for name, age, job in zip(names, ages, jobs):
   print("{0}--{1}--{2}".format(name, age, job))

# 统计文本中字符出现的次数：
my_text = ' i love you, i love sxt, i love gaoqi'
char_count = {c : my_text.count(c) for c in my_text}
print(char_count)

# 绘制多个同心圆
import turtle
p = turtle.Pen()  # 画笔对象
radius = [x*10 for x in range(1, 11)]   # 10,20,30,40...
my_colors = ("red", "green", "yellow", "black")
p.width(4)
for r, i in zip(radius, range(len(radius))):
   p.penup()
   p.goto(0, -r)
   p.pendown()
   p.color(my_colors[i % len(my_colors)])
   p.circle(r)
turtle.done()   # 程序执行完毕，窗口在

# 绘制18*18棋盘
import turtle
width = 30
num = 18
x1 = [(-400, 400), (-400+width*num, 400)]
y1 = [(-400, 400), (-400, 400-width*num)]
t = turtle.Pen()
t.speed(10)
# t.goto(x1[0][0],x1[0][1])
# t.goto(x1[1][0],x1[1][1])
for i in range(num+1):
   t.penup()
   t.goto(x1[0][0], x1[0][1]-30*i)
   t.pendown()
   t.goto(x1[1][0], x1[1][1]-30*i)
for i in range(num+1):
    t.penup()
    t.goto(y1[0][0] + 30 * i, y1[0][1])
    t.pendown()
    t.goto(y1[1][0] + 30 * i, y1[1][1])
t.hideturtle()  # 隐藏画笔
turtle.done()  # 保证运行窗口不被自动关闭