# 프로그래머스 - 주식가격 (Lv.2, 스택/큐)
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
#
# 각 시점 i 에 대해 "가격이 떨어지지 않은 기간"을 구한다.
# 즉, j > i 이면서 prices[j] < prices[i] 인 가장 빠른 j 를 찾아 j - i,
# 그런 j 가 없으면 (n - 1) - i 가 답이다.
#
# 순진하게 이중 루프로 풀면 O(N^2). N <= 100,000 이므로 통과는 하지만
# 스택을 쓰면 O(N) 으로 줄일 수 있다.
#
# 스택에는 "아직 가격이 떨어진 시점을 못 만난" 인덱스를 보관한다.
# 새 가격 prices[i] 가 스택 top 의 가격보다 낮으면, 그 top 은 i 에서
# 처음으로 가격이 떨어진 것이므로 result[top] = i - top 으로 확정하고 pop.
# 더 이상 떨어지지 않으면 i 를 스택에 push.
# 루프가 끝난 뒤 스택에 남은 인덱스들은 끝까지 안 떨어진 것이므로
# result[idx] = (n - 1) - idx.
#
# 시간복잡도: O(N) (각 인덱스가 스택에 1번 push, 1번 pop)


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 인덱스만 보관

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = (n - 1) - top

    return answer


if __name__ == "__main__":
    # 공식 예시
    assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]

    # 계속 오르기만 -> 모두 끝까지 안 떨어짐
    assert solution([1, 2, 3, 4, 5]) == [4, 3, 2, 1, 0]

    # 계속 떨어지기만 -> 다음 시점에 바로 떨어짐
    assert solution([5, 4, 3, 2, 1]) == [1, 1, 1, 1, 0]

    # 동일 가격은 "떨어지지 않은" 것으로 본다
    assert solution([3, 3, 3, 3]) == [3, 2, 1, 0]

    # 단일 원소
    assert solution([10]) == [0]

    # 한 번 큰 폭으로 떨어지는 경우
    assert solution([5, 5, 1, 1]) == [2, 1, 1, 0]

    print("ok")
