# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# [22220228 -> 2222/02/28] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다
# [1월:~31/ 2월:28/ 3월:31/ 4월:30일/ 5월:31/ 6월:30/ 7월:31/ 8월:31/ 9월:30/ 10월:31/ 11월:30/ 12월 31]



import sys
sys.stdin = open('연월일 달력.txt','r')

T = int(input())
for tc in range(1,T+1):
    #숫자 자리수 맞추기

    day = int(input())
    year = ("0000"+str((day//10000)))[-4:]
    month = ("00"+str(day%10000//100))[-2:]
    date = ("00"+str(day%100))[-2:]

    #유효성 판단
    md = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    if int(month) >=1 and int(month)<=12:
        if  int(date) <1 or int(date) > md[int(month)]:
            print(f"#{tc} -1")
        else:
            print(f"#{tc} {year}/{month}/{date}")
    else:
        print(f"#{tc} -1")




