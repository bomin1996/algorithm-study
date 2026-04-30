# 프로그래머스 - 캐시 (Lv.2, 2018 KAKAO BLIND RECRUITMENT)
# https://school.programmers.co.kr/learn/courses/30/lessons/17680
#
# LRU(Least Recently Used) 캐시 정책을 구현하는 문제다.
# - cacheSize == 0 이면 모든 요청이 miss (총 실행시간 = 5 * len(cities))
# - 도시명은 대소문자 구분 없음 -> 비교 전 소문자 정규화
# - hit  : 캐시에 있으면 1, 해당 항목을 "가장 최근 사용"으로 갱신
# - miss : 없으면 5, 가득 찼으면 가장 오래된 항목을 제거하고 새 항목 추가
#
# collections.deque 로 직접 구현해도 되지만, "기존 키 접근 시 맨 뒤로 이동"
# 연산이 O(1)인 OrderedDict.move_to_end 가 더 자연스럽다.
#
# 시간복잡도: O(N), N = len(cities)

from collections import OrderedDict


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cache = OrderedDict()
    elapsed = 0

    for city in cities:
        key = city.lower()

        if key in cache:
            cache.move_to_end(key)
            elapsed += 1
        else:
            if len(cache) >= cacheSize:
                cache.popitem(last=False)
            cache[key] = True
            elapsed += 5

    return elapsed


if __name__ == "__main__":
    # 예시 1: cacheSize=3, 모두 miss -> 5*8 = 40 ... 가 아니라
    # Jeju, Pangyo, Seoul, NewYork(이후 LA로 Jeju 제거), SanFrancisco(Pangyo 제거),
    # Seoul(hit), Rome, Paris -> 50
    assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                        "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50
    # 예시 2: cacheSize=3, 마지막 SanFrancisco 만 hit
    assert solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo",
                        "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21
    # 예시 3: cacheSize=2
    assert solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                        "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                        "NewYork", "Rome"]) == 60
    # 예시 4: cacheSize=5, 모두 miss
    assert solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25
    # 예시 5: cacheSize=2, 모두 같은 도시 -> 첫 1번만 miss
    assert solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16
    # 예시 6: cacheSize=0 -> 전부 miss
    assert solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25
    print("ok")
