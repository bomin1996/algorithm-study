# 백준 7576 토마토 (Gold V)
# https://www.acmicpc.net/problem/7576
#
# 창고의 익은 토마토(1)가 하루마다 인접(상하좌우)한 안 익은 토마토(0)를 익게 한다.
# 모든 토마토가 익는 최소 일수를 구하고, 불가능하면 -1을 출력한다.
#
# 풀이: 익은 토마토 전체를 시작점으로 하는 멀티 소스 BFS.
# 큐에 (행, 열)을 넣고 거리 배열 대신 격자에 일수를 직접 기록한다.
# BFS 종료 후 0이 남아 있으면 -1, 아니면 기록된 최댓값 - 1이 답.

import sys
from collections import deque

input = sys.stdin.readline


def solve():
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    queue = deque()
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))

    days = 0
    for row in grid:
        if 0 in row:
            print(-1)
            return
        days = max(days, max(row))

    print(days - 1)


solve()
