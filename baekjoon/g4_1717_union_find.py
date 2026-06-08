# 백준 1717 - 집합의 표현 (Gold IV)
# https://www.acmicpc.net/problem/1717
#
# 0부터 n까지 n+1개의 원소가 각각 자기 자신만을 포함한 집합으로 시작한다.
# 다음 두 연산을 m번 처리한다.
#   0 a b : a가 속한 집합과 b가 속한 집합을 합친다 (합집합).
#   1 a b : a와 b가 같은 집합에 속하는지 확인한다 (YES / NO).
#
# 접근:
#   분리 집합(Union-Find). 각 원소의 대표(root)를 parent 배열로 관리한다.
#     find(x): x의 루트를 찾는다. 경로 압축으로 트리를 평탄하게 만든다.
#     union(a, b): 두 루트를 잇되, 랭크가 낮은 트리를 높은 트리 밑에 붙여
#                  트리 높이가 불필요하게 커지지 않게 한다 (union by rank).
#
#   n이 최대 1,000,000 이라 재귀 find 는 재귀 한도에 걸린다.
#   따라서 find 를 반복문으로 구현하고, 찾은 루트로 경로 압축을 한 번 더 돈다.
#
# 시간복잡도: 연산당 거의 상수 (역 아커만 함수) -> O((n + m) * alpha)
# 공간복잡도: O(n)

import sys


def find(parent, x):
    # 루트 탐색.
    root = x
    while parent[root] != root:
        root = parent[root]
    # 경로 압축: 지나온 노드를 전부 루트에 직접 연결.
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root


def union(parent, rank, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return
    # 랭크가 낮은 쪽을 높은 쪽 밑에 붙인다.
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    out = []
    for _ in range(m):
        op = data[idx]; idx += 1
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1

        if op == b"0":
            union(parent, rank, a, b)
        else:
            out.append("YES" if find(parent, a) == find(parent, b) else "NO")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    main()
