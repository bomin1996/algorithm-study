# 프로그래머스 - 다리를 지나는 트럭 (Lv.2, 스택/큐)
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
#
# 길이 bridge_length 칸짜리 다리를 1초 단위로 시뮬레이션한다.
# 다리 자체를 길이 bridge_length 인 큐로 보고, 매 초마다
#   1) 다리 맨 앞 칸을 pop (트럭들이 한 칸씩 전진)
#   2) 대기 중인 트럭이 있고 (현재 다리 위 무게 + 다음 트럭 무게) <= weight 면 push,
#      안 되면 0(빈 칸)을 push 해서 다리 길이를 유지한다.
# 대기열도 비고 다리 위에도 트럭이 없을 때 종료.
#
# 매 초마다 sum(bridge) 로 무게를 계산하면 O(N * bridge_length) 이지만,
# 현재 다리 위 무게를 변수로 들고 다니면서 push/pop 시점에만 가감하면 O(N + bridge_length).
#
# 시간복잡도: O(N + bridge_length)

from collections import deque


def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    on_bridge = 0
    t = 0

    while waiting or on_bridge > 0:
        t += 1
        on_bridge -= bridge.popleft()

        if waiting:
            if on_bridge + waiting[0] <= weight:
                truck = waiting.popleft()
                bridge.append(truck)
                on_bridge += truck
            else:
                bridge.append(0)

    return t


if __name__ == "__main__":
    # 공식 예시
    assert solution(2, 10, [7, 4, 5, 6]) == 8
    assert solution(100, 100, [10]) == 101
    assert solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110

    # 트럭 1개 -> bridge_length + 1
    assert solution(5, 5, [3]) == 6

    # 다리/무게 모두 1 -> 매 step 마다 한 대씩 통과
    assert solution(1, 1, [1, 1, 1]) == 4

    # 무게가 빡빡해서 한 번에 한 대만 올릴 수 있는 경우
    # t=1 첫 트럭 진입 -> t=3 에 빠짐 -> t=3 둘째 진입 -> t=5 셋째 진입 -> t=7 셋째 빠짐
    assert solution(2, 10, [10, 10, 10]) == 7

    # 큰 트럭 뒤에 작은 트럭이 줄줄이 오는 케이스
    # 큰 트럭이 다리 위에 있는 동안 작은 트럭들이 못 올라감
    assert solution(3, 10, [7, 4, 5, 6]) == 11

    print("ok")
