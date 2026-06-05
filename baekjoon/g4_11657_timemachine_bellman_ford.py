# 백준 11657 - 타임머신 (Gold IV)
# https://www.acmicpc.net/problem/11657
#
# N개의 도시와 M개의 버스 노선이 있다. 노선 (A, B, C)는
# A -> B 로 이동하는 데 걸리는 시간이 C라는 뜻이며, C는 음수일 수 있다.
# 1번 도시에서 나머지 각 도시로 가는 가장 빠른 시간을 구한다.
#
# 접근:
#   간선 가중치에 음수가 있으므로 다익스트라를 쓸 수 없고 벨만-포드를 쓴다.
#   dist[1] = 0 에서 시작해 모든 간선을 (N-1)번 완화(relax)한다.
#   N-1번이면 음수 사이클이 없는 한 최단거리가 확정된다.
#
#   음수 사이클 판정:
#     N번째로 한 번 더 완화를 돌려서 갱신되는 간선이 있으면,
#     무한히 과거로 돌아갈 수 있는 경로가 존재하므로 -1을 출력한다.
#
#   주의: 1번에서 도달 불가능한 도시(dist == INF)는 완화 대상이 아니다.
#   도달 불가능한 정점을 출발로 한 간선까지 음수 사이클로 오판하면 안 되므로,
#   완화 시 출발 정점이 INF인 간선은 건너뛴다.
#
# 시간복잡도: O(N * M)
# 공간복잡도: O(N + M)

import sys

INF = float("inf")


def bellman_ford(n, edges, start):
    dist = [INF] * (n + 1)
    dist[start] = 0

    # N번 반복: 1..N-1번은 최단거리 확정, N번째는 음수 사이클 판정용.
    for i in range(n):
        for a, b, c in edges:
            if dist[a] == INF:
                continue
            if dist[a] + c < dist[b]:
                dist[b] = dist[a] + c
                if i == n - 1:
                    # 마지막 반복에서도 갱신 -> 음수 사이클 존재.
                    return None

    return dist


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    edges = []
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        c = int(data[idx]); idx += 1
        edges.append((a, b, c))

    dist = bellman_ford(n, edges, 1)

    out = []
    if dist is None:
        out.append("-1")
    else:
        for node in range(2, n + 1):
            out.append("-1" if dist[node] == INF else str(dist[node]))

    print("\n".join(out))


if __name__ == "__main__":
    main()
