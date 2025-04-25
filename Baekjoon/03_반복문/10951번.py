# Baekjoon 10951번: A+B - 4 (https://www.acmicpc.net/problem/10951)
# 두 정수 A와 B를 입력받아서 A+B를 출력


import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        if 0 < A < 10 and 0 < B < 10:
            print(A+B)
    except ValueError:
        break

# ZeroDivisionError: 0으로 나누기 시도
# IndexError: 리스트, 튜플 등의 인덱스 범위를 벗어나는 접근 시도
# ValueError: 함수나 연산이 잘못된 값으로 호출될 때
# TypeError: 부적절한 데이터 타입 간의 연산 시도
# FileNotFoundError: 파일을 열려고 시도했지만, 파일이 존재하지 않는 경우
# KeyError: 딕셔너리에서 존재하지 않는 키를 사용하려 할 때
# AttributeError: 객체에 존재하지 않는 속성이나 메서드를 호출하려 할 때
# ImportError: 모듈이나 객체를 찾을 수 없을 때
# NameError: 정의되지 않은 변수나 함수 사용 시
# TimeoutError: 시간 초과가 발생했을 때
# MemoryError: 프로그램이 사용할 수 있는 메모리를 모두 소진했을 때
# StopIteration: for 루프나 이터레이터에서 더 이상 값이 없을 때
# Exception: 위에서 다룬 예외를 포함하여 모든 예외의 기본 클래스
