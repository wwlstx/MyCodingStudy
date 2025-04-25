# Baekjoon 10952번: A+B - 5 (https://www.acmicpc.net/problem/10952)
# 두 정수 A와 B를 입력받아서 A+B를 출력
# 입력의 마지막에는 0 두 개

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A != 0 or B != 0:
        print(A+B)
    else:
        break
