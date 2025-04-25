# Baekjoon 25304번: 영수증 (https://www.acmicpc.net/problem/25304)
# 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사

X = int(input())
N = int(input())
total = 0

for i in range(N):
    a, b = map(int, input().split())
    total += a*b

if total == X:
    print("Yes")
else:
    print("No")
