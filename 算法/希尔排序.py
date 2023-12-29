def shell_sort(arr):
    n = len(arr)        # 获取列表的长度
    gap = n//2          # 获取间隔
    while gap > 0:      # 循环到不能分割
        for i in range(gap, n):     # 插入排序，认为第一个数据就是已经排序好的
            tmp = arr[i]            # 记录下来要比较的数据
            j = i                   # 记录位置
            while j >= gap and arr[j-gap] > tmp:    # 判断是否要做插入排序
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = tmp
        gap = gap // 2


if __name__ == '__main__':
    nums = [5, 2, 6, 4, 7, 3, 1]
    shell_sort(nums)
    print(nums)

