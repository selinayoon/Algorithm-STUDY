import sys
sys.stdin  = open('아주 간단한 계산기.txt','r')

n1,n2 = list(map(int,input().split()))

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1//n2)
