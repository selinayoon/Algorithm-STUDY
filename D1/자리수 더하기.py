import sys
sys.stdin = open('자리수 더하기.txt','r')

n = int(input())

one = n%10
if n>=1000:
    tho = n//1000
    hun = (n%1000)//100
    ten = (n%100)//10

    print(one)
    print(ten)
    print(hun)
    print(tho)

    print(tho+hun+ten+one)
elif n>=100:
    hun = n//100
    ten = (n%100)//10
    print(hun+ten+one)
elif n>=10:
    ten = n//10
    print(ten+one)
else:
    print(one)