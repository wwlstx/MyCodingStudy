# Baekjoon 2438번: 별 찍기 - 1 (https://www.acmicpc.net/problem/2438)
# N번째 줄에는 별 N개 출력

import sys

N = int(sys.stdin.readline())
for i in range(1, N+1):
    print("*"*i)
