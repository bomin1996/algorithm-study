# 백준 1655 - 가운데를 말해요 (Gold II)
# https://www.acmicpc.net/problem/1655
#
# 수빈이가 정수를 하나씩 외칠 때마다, 지금까지 외친 수 중 중앙값을 말해야 한다.
# 지금까지 외친 수가 짝수 개라면 중앙에 있는 두 수 중 작은 수를 말한다.
#
# 접근:
#   매번 정렬하면 O(n^2 log n) 으로 시간 초과. 두 개의 힙으로 중앙값을 유지한다.
#     - lower: 작은 절반을 담는 최대 힙 (파이썬 heapq 는 최소 힙이라 부호를 뒤집어 저장).
#     - upper: 큰 절반을 담는 최소 힙.
#   불변식:
#     - len(lower) == len(upper)  또는  len(lower) == len(upper) + 1
#     - max(lower) <= min(upper)
#   이 불변식이 유지되면 중앙값(짝수 개일 때는 작은 쪽)은 항상 lower 의 top 이다.
#
# 삽입 규칙:
#   두 힙의 크기를 같게 맞추기 위해, 개수가 짝수였으면 lower 에, 홀수였으면 upper 에 넣는다.
#   넣은 뒤 두 top 의 대소가 어긋나면(lower top > upper top) 서로 교환해 불변식을 회복한다.
#
# 시간복잡도: 삽입당 O(log n) -> 전체 O(n log n)
# 공간복잡도: O(n)

import sys
import heapq


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])

    lower = []  # 최대 힙 (값을 음수로 저장)
    upper = []  # 최소 힙
    out = []

    for i in range(1, n + 1):
        num = int(data[i])

        # 짝수 개였으면 lower, 홀수 개였으면 upper 에 넣어 크기 균형을 맞춘다.
        if len(lower) == len(upper):
            heapq.heappush(lower, -num)
        else:
            heapq.heappush(upper, num)

        # 두 힙 모두 비어있지 않고 경계가 어긋났으면(top 끼리 교환) 회복.
        if upper and -lower[0] > upper[0]:
            small = -heapq.heappop(lower)
            big = heapq.heappop(upper)
            heapq.heappush(lower, -big)
            heapq.heappush(upper, small)

        # 중앙값은 항상 lower 의 top.
        out.append(str(-lower[0]))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
