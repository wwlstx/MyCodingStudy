# Baekjoon 15552번: 빠른 A+B (https://www.acmicpc.net/problem/15552)
# T개의 줄에 주어진 두 정수 A, B를 더한 값을 순서대로 출력
# 빠른 입력을 위해 sys.stdin.readline().rstrip() 사용

import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

# input()은 추가적인 처리(문자열을 처리하거나 공백을 없애는 등)가 있어서 더 많은 시간 소요
# sys.stdin.readline()은 입력 받은 그대로 읽기만 하니까 더 빠르게 동작

# sys.stdin.readline()은 문자열을 반환
# rstrip() 사용시 런타임 에러: 줄바꿈 문자를 제거하려고 하면서 입력 버퍼에 문제 발생
