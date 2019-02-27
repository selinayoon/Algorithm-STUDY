import sys
sys.stdin = open('큰놈,작은놈,같은놈.txt', 'r')

# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

T = int(input())
for tc in range(1,T+1):
    num1, num2 = map(int, input().split())
    if num1 == num2 :
        result = "="
    elif num1 > num2:
        result = ">"
    else:
        result = "<"

    print(f"#{tc} {result}")


