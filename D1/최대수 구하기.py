# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
import sys
sys.stdin = open('최대수 구하기.txt','r')

T = int(input())
for tc in range(1, T+1):
    li = list(map(int,input().split()))
    # print(li)

    max_num = li[0]
    for num in li:
        if num >max_num:
            max_num = num
    # print(max_num)

    print(f"#{tc} {max_num}")