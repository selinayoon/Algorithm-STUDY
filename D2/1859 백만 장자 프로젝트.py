# 25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
# 다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
#
#     1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
#     2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
#     3. 판매는 얼마든지 할 수 있다.
#
# 예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
import sys
sys.stdin = open('1859 백만 장자 프로젝트.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    days = list(map(int,input().split()))
    maxc = 0
    revenue = 0
    for i in range(N-1,-1,-1):
        if days[i]>maxc:
            maxc = days[i]
        else:
            revenue += maxc - days[i]

    print(f"#{tc} {revenue}")