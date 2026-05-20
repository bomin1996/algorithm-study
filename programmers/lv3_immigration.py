# 프로그래머스 - 입국심사 (Lv.3, 이분탐색)
# https://school.programmers.co.kr/learn/courses/30/lessons/43238
#
# n 명을 처리시간이 서로 다른 심사관들이 동시에 심사한다.
# "모든 사람을 심사하는 데 걸리는 최소 시간" 을 구하는 문제.
#
# 시간 T 가 주어졌을 때, 각 심사관 i 는 T // times[i] 명을 처리할 수 있다.
# 따라서 sum(T // t for t in times) >= n 이면 T 안에 모두 끝낼 수 있다.
# T 를 키울수록 처리 가능 인원이 단조증가하므로, T 에 대해 이분탐색.
#
# 탐색 범위:
#   lo = 1
#   hi = max(times) * n   (가장 느린 심사관 한 명이 전부 처리하는 최악값)
# 각 mid 에 대해 capacity(mid) >= n 이면 hi = mid, 아니면 lo = mid + 1.
# 종료 시 lo == hi 가 답.
#
# n <= 1e9, len(times) <= 1e5, times[i] <= 1e9
# hi 는 최대 1e18, log2(1e18) 약 60. 한 step 당 O(len(times)) = O(1e5).
# 총 약 6e6 연산 -> 충분.

def solution(n, times):
    lo, hi = 1, max(times) * n

    while lo < hi:
        mid = (lo + hi) // 2
        capacity = sum(mid // t for t in times)
        if capacity >= n:
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    # 공식 예시: 6명, 심사관 [7, 10] -> 28
    # t=28: 28//7=4, 28//10=2, 합 6 -> 가능
    # t=27: 27//7=3, 27//10=2, 합 5 -> 불가
    assert solution(6, [7, 10]) == 28

    # 심사관 1명: n * times[0]
    assert solution(1, [5]) == 5
    assert solution(10, [3]) == 30

    # n=0 은 입력 조건상 없지만(1 <= n), 동일 처리시간 케이스
    # n=4, times=[5,5] -> 한 명당 5초씩, 동시에 둘이 처리하므로 10초
    assert solution(4, [5, 5]) == 10

    # 처리시간 1짜리 심사관이 섞여 있는 경우
    # n=10, times=[1, 100] -> t=10 일 때 10//1 + 10//100 = 10 -> 10
    assert solution(10, [1, 100]) == 10

    # 큰 입력 경계: n=1e9, times=[1] -> 1e9
    assert solution(10**9, [1]) == 10**9

    print("ok")
