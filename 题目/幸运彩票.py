"""
题目描述：
彩票的号码有 6 位数字，若一张彩票的前 3 位上的数之和等于后 3 位上的数之和，则称这张彩票是幸运的。本题就请你判断给定的彩票是不是幸运的。

输入格式：
输入在第一行中给出一个正整数 N（≤ 100）。随后 N 行，每行给出一张彩票的 6 位数字。

输出格式：
对每张彩票，如果它是幸运的，就在一行中输出 You are lucky!；否则输出 Wish you good luck.。

输入样例：
2
233008
123456
输出样例：
You are lucky!
Wish you good luck.
"""
N = int(input())
for _ in range(N):
    ticket = input()
    sum1 = sum(map(int, ticket[:3]))
    sum2 = sum(map(int, ticket[3:]))
    if sum1 == sum2:
        print("You are lucky!")
    else:
        print("Wish you good luck.")
