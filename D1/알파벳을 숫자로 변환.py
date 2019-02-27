# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

import sys
sys.stdin = open('알파벳을 숫자로 변환.txt','r')

moonja =  str(input())

#내가 처음 풀었던 방식.
# d = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,NOPQRSTUVWXYZ}


for m in moonja:
    print(ord(m)-64,end=' ')
