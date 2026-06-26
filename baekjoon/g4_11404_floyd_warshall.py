# 백준 11404 - 플로이드 (Gold IV)
# https://www.acmicpc.net/problem/11404
#
# n개의 도시와 m개의 버스가 있다. 각 버스는 a -> b 로 가는 비용 c 를 가진다.
# 모든 도시 쌍 (i, j) 에 대해 i 에서 j 로 가는 최소 비용을 구한다.
# 갈 수 없으면 0 을 출력한다.
#
# 접근:
#   도시 수가 n <= 100 으로 작고 모든 쌍의 최단거리가 필요하므로 플로이드-워셜.
#   dist[i][j] 를 직접 간선으로 초기화하되, 같은 (a, b) 가 여러 번 주어질 수 있으니 최솟값만 남긴다.
#   경유지 k 를 하나씩 늘려가며 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 로 갱신한다.
#
# 시간복잡도: O(n^3)
# 공간복잡도: O(n^2)

import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    INF = float("inf")
    # dist[i][j]: i 에서 j 로 가는 최소 비용. 자기 자신은 0.
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    for _ in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); c = int(data[idx + 2])
        idx += 3
        # 같은 노선이 여러 번 주어질 수 있으므로 더 싼 비용만 남긴다.
        if c < dist[a][b]:
            dist[a][b] = c

    # 경유지 k 를 거쳐 가는 경로로 갱신.
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    out = []
    for i in range(1, n + 1):
        row = dist[i]
        # 도달 불가능한 경우 0 으로 출력.
        out.append(" ".join(str(row[j]) if row[j] != INF else "0" for j in range(1, n + 1)))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
