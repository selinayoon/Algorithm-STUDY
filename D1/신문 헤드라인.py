# 신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.
# 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결라.과를 출력하는 프로그램을 작성하

import sys
sys.stdin = open('신문 헤드라인.txt','r')

line = str(input())

# for li in line:
#
#     if ord(li)>96 and ord(li)<123:
#         print(chr(ord(li)-32),end='')
#
#     else:
#         print(li,end='')

print(line.upper())


