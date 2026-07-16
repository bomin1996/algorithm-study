# 백준 13549 숨바꼭질 3 (Gold V)
# https://www.acmicpc.net/problem/13549
#
# 수빈이는 N에서 시작해 동생은 K에 있다. 걷기(X-1, X+1)는 1초,
# 순간이동(2*X)은 0초 걸린다. 동생을 찾는 가장 빠른 시간을 구한다.
#
# 풀이: 간선 가중치가 0과 1뿐이므로 0-1 BFS.
# 순간이동(가중치 0)은 덱의 앞에, 걷기(가중치 1)는 덱의 뒤에 넣으면
# 덱에서 꺼내는 순서가 항상 시간 오름차순이 되어 다익스트라 없이 최단 시간을 구할 수 있다.

import sys
from collections import deque

MAX = 100000


def solve():
    n, k = map(int, sys.stdin.readline().split())

    dist = [-1] * (MAX + 1)
    dist[n] = 0
    dq = deque([n])

    while dq:
        x = dq.popleft()
        if x == k:
            print(dist[x])
            return
        if x * 2 <= MAX and dist[x * 2] == -1:
            dist[x * 2] = dist[x]
            dq.appendleft(x * 2)
        for nx in (x - 1, x + 1):
            if 0 <= nx <= MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                dq.append(nx)


solve()
