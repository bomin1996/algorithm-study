# 백준 2470 - 두 용액 (Gold V)
# https://www.acmicpc.net/problem/2470
#
# 산성(양수)/알칼리성(음수) 용액 n개가 주어진다. 두 용액을 섞은 특성값(합)이
# 0에 가장 가까운 조합을 찾아 두 용액의 특성값을 오름차순으로 출력한다.
#
# 접근:
#   특성값을 정렬한 뒤 양 끝에서 투 포인터로 좁혀 온다.
#     합 > 0 이면 합을 줄여야 하므로 오른쪽 포인터를 왼쪽으로,
#     합 < 0 이면 합을 키워야 하므로 왼쪽 포인터를 오른쪽으로 이동.
#   매 단계에서 |합| 이 지금까지의 최소보다 작으면 답을 갱신한다.
#   합이 정확히 0이면 더 좋아질 수 없으므로 즉시 종료.
#
# 시간복잡도: 정렬 O(n log n) + 투 포인터 O(n)
# 공간복잡도: O(n)

import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = sorted(int(x) for x in data[1 : 1 + n])

    lo, hi = 0, n - 1
    best = (values[lo], values[hi])
    best_abs = abs(values[lo] + values[hi])

    while lo < hi:
        total = values[lo] + values[hi]
        if abs(total) < best_abs:
            best_abs = abs(total)
            best = (values[lo], values[hi])
            if best_abs == 0:
                break
        if total > 0:
            hi -= 1
        else:
            lo += 1

    print(best[0], best[1])


if __name__ == "__main__":
    main()
