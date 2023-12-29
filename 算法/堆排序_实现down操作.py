def down(heap0: list[int], index: int, size: int):
    """
   维护堆的特性
   """
    # 建立一个变更，来存储最大值的索引
    max_index = index
    # 获取左节点的索引
    left = max_index * 2 + 1
    # 获取右节点的索引
    right = max_index * 2 + 2
    # 进行比较获取出最大值索引来
    if left < size and heap0[max_index] < heap0[left]:
        max_index = left
    if right < size and heap0[max_index] < heap0[right]:
        max_index = right
    # 如果max_index 和 index 值不一样，说明需要进行交换
    if max_index != index:
        heap0[max_index], heap0[index] = heap0[index], heap0[max_index]
        down(heap0, max_index, size)


def heap_sort(heap1: list[int]):
    # 获取堆有多少数据
    size = len(heap1)
    # 打印原始数据
    print(heap1)
    # 建堆
    for i in range(size // 2, -1, -1):  # 为了保证一次性取到最大值，所以让索引倒取
        down(heap1, i, size)
    # 打印维护后数据
    print(heap1)
    # 排序
    for i in range(size - 1, 0, -1):
        # 将最大值和未排序的最一个索引进行交换
        heap1[i], heap1[0] = heap1[0], heap1[i]
        # 维护堆的特性
        down(heap1, 0, i)
    print(heap1)


if __name__ == "__main__":
    heap = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    heap_sort(heap)
