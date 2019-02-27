# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
import sys
sys.stdin = open('홀수만 더하기.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    li = list(map(int, input().split()))

    sum = 0
    for i in li:
        if i%2 == 1:
            sum += i

    print(f"#{tc} {sum}")