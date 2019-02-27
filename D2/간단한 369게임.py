# 1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.
# 2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.
# 예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
# 입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를 게임 규칙에 맞게 출력하는 프로그램을 작성하라.
# 박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
# 여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다.
#
# import sys
# sys.stdin = open('간단한 369게임.txt','r')
#
# num = int(input())
# for i in range(1,num+1):
#     cnt = 0
#     while i>0:
#         o = i%10
#         i = i//10
#         if o == 3 or o == 6 or o == 9:
#             cnt += 1
#     if cnt == 0:
#         print(i,end=' ')
#     print("-----")
#     # print(cnt,end=' ')

# x = int(input("숫자를 입력하세요: "))
# count = 0
#
# if x > 1000:
#     print("1000이하 숫자를 입력하세요")
#
# elif x >= 100:
#     a = x // 100
#     b = (x % 100) // 10
#     c = x % 10
#     for i in [a, b, c]:
#         if i % 3 == 0:
#             count += 1
#
# elif x >= 10:
#     a = x // 10
#     b = x % 10
#     # print(a, b)
#     count = 0
#     for i in [a, b]:
#         if i % 3 == 0:
#             count += 1
#
# else:
#     if x % 3 == 0:
#         count += 1
#
# if count == 3:
#     print("짝짝짝")
# elif count == 2:
#     print("짝짝")
# else:
#     print("짝")
#
# print(x)
