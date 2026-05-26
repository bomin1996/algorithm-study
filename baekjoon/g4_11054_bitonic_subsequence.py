# 백준 11054 - 가장 긴 바이토닉 부분 수열 (Gold IV)
# https://www.acmicpc.net/problem/11054
#
# 어떤 위치 k를 기준으로 왼쪽은 증가, 오른쪽은 감소(strictly)하는 부분 수열의
# 최대 길이를 구한다. k가 양 끝이면 한 방향만 있어도 된다(증가만/감소만).
#
# 풀이 메모
# - lis[i]: arr[i]로 끝나는 최장 증가 부분 수열 길이
# - lds[i]: arr[i]로 시작하는 최장 감소 부분 수열 길이
# - 정점 i를 봉우리로 쓰는 바이토닉 길이는 lis[i] + lds[i] - 1 (i가 양쪽에 중복 포함)
# - 답은 max(lis[i] + lds[i] - 1) for i in [0..n-1]
#
# N <= 1000 이므로 O(N^2) DP 로 충분 (1e6 연산).

import sys


def longest_bitonic(arr):
    n = len(arr)
    if n == 0:
        return 0

    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    lds = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i] and lds[j] + 1 > lds[i]:
                lds[i] = lds[j] + 1

    return max(lis[i] + lds[i] - 1 for i in range(n))


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = [int(x) for x in data[1 : 1 + n]]
    print(longest_bitonic(arr))


if __name__ == "__main__":
    main()
