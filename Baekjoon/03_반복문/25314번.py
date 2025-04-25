# Baekjoon 25314번: 코딩은 체육과목 입니다 (https://www.acmicpc.net/problem/25314)
# long을 N/4번 반복하고 마지막에 int를 붙여 출력

N = int(input())
for i in range(N//4):
    print("long", end=' ')
print("int")
