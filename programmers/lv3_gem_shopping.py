# 프로그래머스 - 보석 쇼핑 (Lv.3, 슬라이딩 윈도우 / 투 포인터)
# https://school.programmers.co.kr/learn/courses/30/lessons/67258
#
# 진열대에 gems 가 일렬로 놓여 있다. 모든 종류의 보석을 적어도 하나씩
# 포함하는 가장 짧은 연속 구간 [start, end] (1-based, end 포함) 를 구한다.
# 길이가 같은 구간이 여럿이면 start 가 가장 작은 구간을 반환.
#
# 접근:
#   - 전체 보석 종류 수 kinds = len(set(gems)).
#   - 오른쪽 포인터 right 를 늘리며 윈도우에 보석을 추가하고,
#     윈도우가 모든 종류를 담는 순간 왼쪽 포인터 left 를 최대한 줄인다.
#   - 윈도우 안 종류 수가 kinds 와 같아지면 현재 길이를 후보로 비교.
#   - left 보석의 카운트가 1 일 때 더 줄이면 종류가 빠지므로, 그 직전까지만 축소.
#
# 왜 최소 start 가 자동으로 보장되나:
#   - right 를 0 부터 단조 증가시키며, 같은 길이의 더 짧은 갱신만 채택한다
#     (best_len 보다 "엄격히 작을 때"만 갱신). 따라서 같은 길이라면 먼저
#     발견된, 즉 start 가 더 작은 구간이 유지된다.
#
# 시간복잡도: O(N) — left, right 각각 최대 N 번 전진. (N = len(gems))
# 공간복잡도: O(K) — 윈도우 카운트 dict, K = 보석 종류 수.

from collections import defaultdict


def solution(gems):
    kinds = len(set(gems))
    counts = defaultdict(int)

    left = 0
    have = 0  # 현재 윈도우가 담은 보석 "종류" 수
    best_start, best_end = 0, len(gems) - 1  # 최악의 경우: 전체 구간

    for right in range(len(gems)):
        if counts[gems[right]] == 0:
            have += 1
        counts[gems[right]] += 1

        # 모든 종류를 담았으면 left 를 최대한 줄인다.
        while have == kinds:
            if right - left < best_end - best_start:
                best_start, best_end = left, right

            counts[gems[left]] -= 1
            if counts[gems[left]] == 0:
                have -= 1
            left += 1

    # 1-based 인덱스로 변환
    return [best_start + 1, best_end + 1]


if __name__ == "__main__":
    # 공식 예시
    assert solution(
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    ) == [3, 7]
    assert solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3]
    assert solution(["XYZ", "XYZ", "XYZ"]) == [1, 1]
    assert solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5]

    # 모든 보석이 한 종류 -> 길이 1 구간, 가장 앞선 start
    assert solution(["A", "A", "A"]) == [1, 1]

    # 앞쪽 A 중복은 버리고 마지막 A,B 만 담는 길이 2 구간이 최소
    assert solution(["A", "A", "A", "B"]) == [3, 4]

    # 같은 길이의 최소 구간이 여럿 -> start 가 더 작은 쪽
    assert solution(["A", "B", "A", "B"]) == [1, 2]

    print("ok")
