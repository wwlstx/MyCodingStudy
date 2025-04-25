#Baekjoon 8393번: 합 (https://www.acmicpc.net/problem/8393)
#n이 주어졌을 때, 1부터 n까지 합

import random

n = random.randint(1, 10000)
print(n)
total = 0
for i in range(1, n+1):
    total += i
print(total)
