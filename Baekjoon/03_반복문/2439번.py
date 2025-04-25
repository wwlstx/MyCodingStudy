# Baekjoon 2439번: 별 찍기 - 2 (https://www.acmicpc.net/problem/2439)
# 오른쪽을 기준으로 정렬하여 N번째 줄에 N개의 별 출력

import sys

N = int(sys.stdin.readline())
for i in range(1, N+1):
    print(f"{'*'*i:>{N}}")

# print(("*"*i).rjust(N))
# print(f"{'*'*i:>{N}}")
# print("{:>{}}".format("*"*i, N))
