# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

import sys
sys.stdin = open('더블 더블.txt','r')

n = int(input())

m = 1
print(m,end=' ')
for i in range(1,n+1):
    m = m * 2
    print(m, end=' ')

