# 프로그래머스 - 단어 변환 (Lv.3, BFS)
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
#
# begin 에서 시작해 한 번에 한 글자씩만 바꿔 target 으로 변환한다.
# 변환 중간에 나오는 단어는 반드시 words 안에 있어야 한다.
# target 으로 바꾸는 최소 변환 횟수를 구하고, 불가능하면 0 을 반환.
#
# 접근:
#   - "한 글자만 다른" 관계를 간선으로 보는 그래프 최단경로 문제.
#   - 모든 단어 길이가 같으므로 두 단어가 인접한지는 다른 글자 수가 1인지로 판단.
#   - 가중치가 모두 1 이므로 BFS 로 begin 에서 각 단어까지의 최소 변환 횟수를 구한다.
#   - target 이 words 에 없으면 도달 불가 -> 0.
#
# 시간복잡도: O(N^2 * L) — 단어 쌍마다 길이 L 만큼 비교. (N=len(words), L=단어 길이)
# 공간복잡도: O(N) — 방문 집합과 큐.

from collections import deque


def _adjacent(a, b):
    # 길이가 같은 두 단어가 정확히 한 글자만 다른지 판단.
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = {begin}
    queue = deque([(begin, 0)])

    while queue:
        word, steps = queue.popleft()
        if word == target:
            return steps

        for nxt in words:
            if nxt not in visited and _adjacent(word, nxt):
                visited.add(nxt)
                queue.append((nxt, steps + 1))

    return 0


if __name__ == "__main__":
    # 공식 예시
    assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
    assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0

    # begin 에서 바로 한 글자 차이로 target 도달
    assert solution("aaa", "aac", ["aac"]) == 1

    # target 이 목록에 있어도 경로가 끊기면 0
    assert solution("aaa", "ddd", ["aab", "ddd"]) == 0

    # 여러 경로 중 최단 길이를 선택 (둘 다 길이 2)
    assert solution("aaa", "aac", ["aba", "aac", "aab"]) == 1

    print("ok")
