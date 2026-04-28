# 프로그래머스 - 디스크 컨트롤러 (Lv.3)
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
#
# 평균 대기시간을 최소화하려면 매 시점 "이미 도착한 작업 중 소요시간이 가장 짧은 것"부터
# 처리하는 SJF(Shortest Job First) 전략이 최적이다.
#
# - 도착 큐: 도착시간 오름차순 deque
# - 대기열: (소요시간, 도착시간) 기준 min-heap
# - 대기열이 비면 시간을 다음 도착시간으로 점프
#
# 시간복잡도: O(N log N)

import heapq
from collections import deque


def solution(jobs):
    jobs.sort()
    pending = deque(jobs)
    waiting = []

    now = 0
    total = 0
    n = len(jobs)

    while pending or waiting:
        while pending and pending[0][0] <= now:
            arrived, duration = pending.popleft()
            heapq.heappush(waiting, (duration, arrived))

        if not waiting:
            now = pending[0][0]
            continue

        duration, arrived = heapq.heappop(waiting)
        now += duration
        total += now - arrived

    return total // n


if __name__ == "__main__":
    # 예시 1
    assert solution([[0, 3], [1, 9], [2, 6]]) == 9
    # 한 번에 들어와도 짧은 것부터: 3, 6, 9 순서 -> 대기 3 + 9 + 18 = 30, 평균 10
    assert solution([[0, 3], [0, 9], [0, 6]]) == 10
    # 단일 작업
    assert solution([[0, 5]]) == 5
    print("ok")
