# 백준 2110 - 공유기 설치 (Gold IV)
# https://www.acmicpc.net/problem/2110
#
# 수직선 위 서로 다른 좌표에 집 n개가 있다. 공유기 c개를 집에 설치하되,
# 가장 인접한 두 공유기 사이의 거리를 최대로 하려고 한다. 그 최댓값을 구한다.
#
# 접근:
#   "인접 거리 d 이상으로 c개를 설치할 수 있는가?" 는 d가 커질수록
#   가능 -> 불가능 으로 단조롭게 바뀐다. 답(거리)을 직접 이분탐색한다 (파라메트릭 서치).
#
#   집 좌표를 정렬한 뒤, 특정 거리 d 가 가능한지 판정(feasible):
#     첫 집에 설치하고, 마지막 설치 위치에서 d 이상 떨어진 다음 집마다 탐욕적으로 설치.
#     설치 개수가 c 이상이면 d 는 가능.
#
#   가능한 가장 큰 d 를 찾는다. lo=1, hi=(최대좌표 - 최소좌표).
#
# 시간복잡도: 정렬 O(n log n) + 이분탐색 O(log(범위)) * 판정 O(n)
# 공간복잡도: O(n)

import sys


def feasible(houses, c, d):
    # 인접 거리 d 이상으로 공유기를 몇 개 설치할 수 있는지로 판정.
    count = 1
    last = houses[0]
    for x in houses[1:]:
        if x - last >= d:
            count += 1
            last = x
            if count >= c:
                return True
    return count >= c


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    c = int(data[idx]); idx += 1

    houses = [int(data[idx + i]) for i in range(n)]
    idx += n
    houses.sort()

    lo, hi = 1, houses[-1] - houses[0]
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(houses, c, mid):
            # mid 가 가능하면 더 큰 거리를 노린다.
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(best)


if __name__ == "__main__":
    main()
