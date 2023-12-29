# try_except基本结构
while True:
    try:
        x = int(input("请输入一个数字:"))
        print("您输入的数字是:", x)
    except:
        print(("异常，输入的不是数字！"))