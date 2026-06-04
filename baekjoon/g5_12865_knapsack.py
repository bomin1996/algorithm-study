# 백준 12865 - 평범한 배낭 (Gold V)
# https://www.acmicpc.net/problem/12865
#
# N개의 물건이 있고 각 물건은 무게 W, 가치 V를 가진다.
# 버틸 수 있는 무게가 K인 배낭에 담을 수 있는 가치의 최댓값을 구한다.
# (각 물건은 0개 또는 1개 -> 0/1 배낭)
#
# 접근:
#   dp[w] = 현재까지 고려한 물건들로 무게 w 이하에서 얻는 최대 가치.
#   물건을 하나씩 추가하며 갱신:
#       dp[w] = max(dp[w], dp[w - weight] + value)
#
#   주의: 같은 물건을 중복으로 담으면 안 되므로(0/1),
#   무게는 K -> weight 방향으로 "내림차순" 순회한다.
#   오름차순으로 돌면 dp[w - weight]가 이번 물건으로 이미 갱신된 값을 참조해
#   같은 물건을 여러 번 담는 무한 배낭(unbounded)이 되어버린다.
#
# 시간복잡도: O(N * K)
# 공간복잡도: O(K)

import sys


def knapsack(capacity, items):
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for w in range(capacity, weight - 1, -1):
            cand = dp[w - weight] + value
            if cand > dp[w]:
                dp[w] = cand

    return dp[capacity]


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    items = []
    for _ in range(n):
        w = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        items.append((w, v))

    print(knapsack(k, items))


if __name__ == "__main__":
    main()
