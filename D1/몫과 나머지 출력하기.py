# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

import sys
sys.stdin = open('몫과 나머지 출력하기.txt','r')

T = int(input())
for tc in range(1,T+1):
    n1,n2 = list(map(int,input().split()))

    print(f"#{tc} {n1//n2} {n1%n2}")