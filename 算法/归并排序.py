def merge_sort(lists):
    # 如果要需要归并排序的列表长度少于1,无法分割,直接返回
    if len(lists) <= 1:
        return lists
    # 设置要分割的索引
    num = int(len(lists) / 2)
    # 分割
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    # 合并left+ right
    return merge(left, right)


def merge(left, right):
    rs = []
    l, r = 0, 0
    # 判断是否有需要根据排序添加数据
    while l < len(left) and r < len(right):
        # 从小到大排序，谁小谁加到rs里
        if left[l] <= right[r]:
            rs.append(left[l])
            # 向后挪一个索引
            l += 1
        else:
            rs.append(right[r])
            r += 1
    # 拼接上剩余没有比较的元素
    rs += list(left[l:])
    rs += list(right[r:])
    return rs


if __name__ == '__main__':
    nums = [5, 2, 6, 4, 7, 3, 1]
    tmp = merge_sort(nums)
    print(tmp)
