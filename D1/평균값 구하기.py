#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)
import sys
sys.stdin = open('평균값 구하기.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    s = 0
    for i in li:
        s = s + i
    # 반올림 함수 round()
    avg = round(s / len(li))

    print(f"#{tc} {avg}")
