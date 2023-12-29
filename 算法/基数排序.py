def jishu_sort(array0):
    # 获取最多需要被排序几次
    times = len(str(max(array0)))
    for i in range(times):
        # 分配
        bukt = [[] for _ in range(10)]
        for eachnum in array0:
            weishu = eachnum // (10 ** i) % 10
            bukt[weishu].append(eachnum)
        # 收集
        array0 = []
        for j in range(10):
            array0 += bukt[j]
        print(array0)


if __name__ == '__main__':
    array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    jishu_sort(array)
