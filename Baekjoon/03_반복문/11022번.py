# Baekjoon 11022번: A+B - 8 (https://www.acmicpc.net/problem/11022)
# 두 정수 A와 B를 입력받아서 A+B를 출력

import sys

T = int(sys.stdin.readline())
for x in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{x}: {A} + {B} = {A+B}")
