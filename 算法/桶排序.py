# 插入排序的算法
def insertion_sort(arr0):
    for i in range(1, len(arr0)):
        # 循环子序列的时候，就要反着来！
        for j in range(i, 0, -1):
            # 如果后面一个数，大于前面的一个数，就交换位置
            if arr0[j] < arr0[j - 1]:
                arr0[j], arr0[j - 1] = arr0[j - 1], arr0[j]
    return arr0


# 桶排序
def bucket_sort(nums, bucket_size=5):
    max_val, minVal = max(nums), min(nums)
    # 数据分为 bucketCount 组，这一个是根据每组的数量决定的
    bucket_count = (max_val - minVal) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]  # 二维桶
    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:
        buckets[(num - minVal) // bucket_size].append(num)
    # 清空 nums
    nums.clear()
    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:
        insertion_sort(bucket)  # 假设使用插入排序
        nums.extend(bucket)  # 将排序好的桶依次放入到 nums 中
    return nums


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(arr)
    tmp = bucket_sort(arr)
    print(tmp)
