# 백준 1238 - 파티 (Gold III)
# https://www.acmicpc.net/problem/1238
#
# N명이 X마을에 모였다가 다시 자기 마을로 돌아간다.
# 각자의 (자기 마을 -> X) + (X -> 자기 마을) 단방향 최단거리 합 중 최댓값을 구한다.
#
# 정점마다 다익스트라를 N번 돌리는 건 N(N+M)logN 으로 비효율적.
# - X에서 출발하는 다익스트라 1번 -> X에서 i까지 (귀가)
# - 간선을 뒤집은 그래프에서 X 다익스트라 1번 -> i에서 X까지 (등교)
# 두 번이면 충분.
#
# 시간복잡도: O((N + M) log N)

import heapq
import sys

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist


def main():
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        reverse_graph[b].append((a, t))

    forward = dijkstra(x, graph, n)          # X -> i
    backward = dijkstra(x, reverse_graph, n)  # i -> X

    print(max(forward[i] + backward[i] for i in range(1, n + 1)))


if __name__ == "__main__":
    main()
