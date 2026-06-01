# 프로그래머스 - 여행경로 (Lv.3, DFS + 백트래킹)
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
#
# 항공권 tickets 를 전부 사용해서 "ICN" 출발 경로를 만든다.
# 가능한 경로가 둘 이상이면 사전순으로 가장 앞선 경로를 반환.
#
# 접근:
#   - 출발지별 도착지 리스트를 dict[str, list[str]] 로 구성.
#   - 각 도착지 리스트를 알파벳순 정렬해두면, 인덱스 0 부터 시도하는 것이 곧 사전순 최소.
#   - ICN 에서 DFS, 사용한 티켓은 pop. 모든 티켓을 못 쓰고 막다른 길이면
#     pop 한 위치에 다시 insert 해서 백트래킹.
#
# 종료조건: len(path) == len(tickets) + 1 (모든 티켓 사용 완료)
#
# 주의:
#   - tickets 최대 10,000장 -> 재귀 깊이 최대 10,001.
#     Python 기본 재귀 한도(1000) 초과 가능 -> sys.setrecursionlimit 으로 상향.
#
# 시간복잡도:
#   - 사전순 정렬된 리스트의 첫 가지가 대부분 성공 -> 실측 평균 O(N).
#     이론적 백트래킹 최악은 O(N!) 이지만 문제 제약상 등장하지 않는다.

import sys
from collections import defaultdict

sys.setrecursionlimit(20000)


def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for k in graph:
        graph[k].sort()

    target_len = len(tickets) + 1
    path = []

    def dfs(airport):
        path.append(airport)
        if len(path) == target_len:
            return True
        nexts = graph[airport]
        for i in range(len(nexts)):
            next_airport = nexts.pop(i)
            if dfs(next_airport):
                return True
            nexts.insert(i, next_airport)
        path.pop()
        return False

    dfs("ICN")
    return path


if __name__ == "__main__":
    # 공식 예시 1
    assert solution(
        [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    ) == ["ICN", "JFK", "HND", "IAD"]

    # 공식 예시 2: 같은 출발지에 도착지 여럿 -> 사전순으로 선택
    assert solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    ) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

    # 백트래킹 검증:
    # graph[ICN] = [A, B] (정렬됨). A 부터 시도하면 ICN -> A -> D 에서 막힘
    # (B, ICN 티켓 미사용). 백트래킹 후 ICN -> B -> ICN -> A -> D 가 정답.
    assert solution(
        [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"]]
    ) == ["ICN", "B", "ICN", "A", "D"]

    # 티켓 1장
    assert solution([["ICN", "JFK"]]) == ["ICN", "JFK"]

    print("ok")
