def count_sort(arr0):
    # 如果数组长度小于 2 则直接返回
    if len(arr0) < 2:
        return arr0
    # 获取数组中最小值
    min_num = min(arr0)
    # 获取数组中最大值
    max_num = max(arr0)
    count = max_num - min_num
    # 开辟一个计数列表(长度为取值范围)
    count_list = [0 for _ in range(count + 1)]
    # 循环操作下标位置数+1(等于是记录每个数在数组中出现了多少次)
    for val in arr0:
        index = val - min_num
        count_list[index] += 1
    # 原数组清空，留待下面重新插入
    arr0.clear()
    # 遍历计数列表中的值和下标(值的数量)，
    # 从0开始，所以最终是从小到大排序
    for ind, val in enumerate(count_list):
        # 下面按照值中的数量进行循环
        for i in range(val):
            # 有多少，则会追加多少次
            arr0.append(ind + min_num)
    return arr0


if __name__ == "__main__":
    print('----------- 排序前数组内容 -----------------')
    arr = [2, 3, 8, 7, 1, 2, 3, 2, 7, 3, 9, 8, 2, 1, 6, 2, 4, 6, 9, 2]
    print(arr)
    count_sort(arr)
    print('------------ 排序后的结果 ------------------')
    print(arr)
