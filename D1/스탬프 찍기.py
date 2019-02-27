# 주어진 숫자만큼 # 을 출력해보세요.
# 주어질 숫자는 100,000 이하다.

import sys
sys.stdin = open('스탬프 찍기.txt','r')

num = int(input())

# for i in range(num):
#     print("#",end='')

print(num * "#")