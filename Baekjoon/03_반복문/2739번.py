# Baekjoon 2739번: 구구단 (https://www.acmicpc.net/problem/2739)
# N을 입력받아서 구구단 N단을 출력

N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")
