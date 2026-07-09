# 백준 9251 LCS (Gold V)
# https://www.acmicpc.net/problem/9251
# 두 문자열의 최장 공통 부분 수열(LCS) 길이를 구한다.
# dp[i][j] = A의 앞 i글자, B의 앞 j글자까지 봤을 때 LCS 길이
# 공간 절약을 위해 직전 행만 유지한다.

import sys


def solve() -> None:
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    prev = [0] * (len(b) + 1)
    for ch in a:
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if ch == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur

    print(prev[len(b)])


if __name__ == "__main__":
    solve()
