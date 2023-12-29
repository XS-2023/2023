"""
链接：https://ac.nowcoder.com/acm/contest/71593/A
来源：牛客网

题目描述
小红拿到了两个正整数x和y，她希望构造两个正整数a和b，满足以下性质：
对x执行a次以下操作：使x加上b。操作结束后使得x等于y。
请你构造任意合法解。共有t组询问。
输入描述:
第一行输入一个正整数t，代表询问的次数。
接下来的t行，每行输入两个正整数x和y，代表一次询问。
1≤t,x,y≤100
输出描述:
对于每次询问，如果无解，则输出两个-1。
否则输出两个正整数，代表一个合法解。
有多解时输出任意即可。
示例1
输入
2
1 5
2 2
输出
2 2
-1 -1
说明
第一组询问，对1进行两次加2操作，即可使其变成5。
第二组询问，显然没有任何合法操作。
"""
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if y <= x:
        a, b = -1, -1
    else:
        a = y - x
        b = 1
    print(a, b)
