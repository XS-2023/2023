"""
链接：https://ac.nowcoder.com/acm/contest/72266/A
来源：牛客网

题目描述
小红去淘宝买了n件物品，第i件物品价格是ai，其中部分物品小红不满意选择退货，
退货可以原价退但需要收取max(5,⌊ai/100⌋)的运费。小红想知道自己最终花费了多少钱。
⌊x⌋代表对x向下取整。例如：⌊3.7⌋=3。
输入描述:
第一行输入一共整数n代表小红购买了n件物品。
第二行输入n正整数ai，代表n件物品的价格。
第三行输入一个长度为n且仅包含'T'和’F‘的字符串，'T'代表购买，'F'代表退货。
1 ≤ n ≤ 10^3
1 ≤ ai ≤ 10^9
输出描述:
输出一共整数，代表小红最终花费的金额。
示例1
输入
5
100 1000 200 700 800
FFTTT
输出
1715
说明
第一件退货，5元，
第二件退货，10元，
第三件购买，200元，
第四件购买，700元，
第五件购买，800元。
"""

n = int(input())
a = list(map(int, input().split()))
b = str(input())
sum0 = 0
for i in range(n):
    if b[i] == "T":
        sum0 += a[i]
    else:
        sum0 += max(5, a[i] // 100)
print(sum0)
