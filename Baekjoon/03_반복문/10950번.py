#Baekjoon 10950번: A+B - 3 (https://www.acmicpc.net/problem/10950)
#두 정수 A와 B를 입력받아서 A+B를 출력

import random
T = random.randint(1, 10)
print(T)
for i in range(T):
    A, B = map(int, input("A와 B를 입력하시오: ").split())
    print(A+B)
