import time

b = int(time.time())
print(b)
totalMinutes = b//60
print(totalMinutes)
totalDays = totalMinutes//(60*24)
totalYears = totalDays//365    # 不考虑闰年
print(totalDays)
print(totalYears)

name = input("请输入名字:")
salary = int(input("请输入月薪:"))
print("名字："+name)
print("年薪："+str(salary*12))