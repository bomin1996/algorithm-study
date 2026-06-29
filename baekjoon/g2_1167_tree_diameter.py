# 백준 1167 - 트리의 지름 (Gold II)
# https://www.acmicpc.net/problem/1167
#
# 가중치가 있는 트리가 주어진다. 트리의 지름(임의의 두 정점 사이 경로 중 가장 긴 것)을 구한다.
#
# 접근:
#   "임의의 정점에서 가장 먼 정점 u 를 찾으면, u 는 반드시 지름의 한 끝점이다" 라는 성질을 이용한다.
#   1) 아무 정점(여기선 1번)에서 BFS 로 가장 먼 정점 u 를 찾는다.
#   2) u 에서 다시 BFS 해 가장 먼 거리를 구하면 그게 지름이다.
#   정점 수가 최대 10만이라 재귀 DFS 는 한계에 걸릴 수 있어 반복 BFS 로 구현한다.
#
# 시간복잡도: O(V) (트리이므로 간선 = V-1, BFS 2회)
# 공간복잡도: O(V)

import sys
from collections import deque


def bfs_farthest(start, graph, n):
    # start 에서 각 정점까지의 거리를 BFS 로 구하고, 가장 먼 정점과 그 거리를 돌려준다.
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    far_node, far_dist = start, 0
    while q:
        cur = q.popleft()
        for nxt, w in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + w
                if dist[nxt] > far_dist:
                    far_dist = dist[nxt]
                    far_node = nxt
                q.append(nxt)
    return far_node, far_dist


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(n):
        u = int(data[idx]); idx += 1
        # 각 줄은 (연결 정점, 거리) 쌍이 반복되다가 -1 로 끝난다.
        while True:
            v = int(data[idx]); idx += 1
            if v == -1:
                break
            w = int(data[idx]); idx += 1
            graph[u].append((v, w))

    # 1) 1번에서 가장 먼 정점 u 를 찾고, 2) u 에서 가장 먼 거리를 구한다.
    u, _ = bfs_farthest(1, graph, n)
    _, diameter = bfs_farthest(u, graph, n)

    sys.stdout.write(str(diameter) + "\n")


if __name__ == "__main__":
    main()
