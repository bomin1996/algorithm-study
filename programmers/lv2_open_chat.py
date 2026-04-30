# 프로그래머스 - 오픈채팅방 (Lv.2, 2019 KAKAO BLIND RECRUITMENT)
# https://school.programmers.co.kr/learn/courses/30/lessons/42888
#
# 핵심 관찰: 출력 시점의 닉네임은 "그 유저가 마지막에 설정한 닉네임" 하나뿐이다.
# 따라서 두 단계로 나누면 깔끔하다.
#
#   1) 첫 패스: 모든 record 를 훑으며 uid -> 최종 nickname 맵을 만든다.
#      (Enter / Change 가 닉네임을 갱신, Leave 는 무시)
#   2) 두 번째 패스: Enter / Leave 만 추려 출력 문자열을 만들고,
#      uid 의 최종 닉네임으로 치환한다.
#
# 한 번에 처리하려고 들면 Change 가 과거 출력을 소급 변경하는 모양이라 꼬인다.
# 상태(닉네임 맵)와 이벤트 로그(들어옴/나감)를 분리해서 처리하는 게 정석이다.
#
# 시간복잡도: O(N), N = len(record)

def solution(record):
    nickname = {}
    events = []

    for line in record:
        parts = line.split()
        action = parts[0]

        if action == "Enter":
            uid, name = parts[1], parts[2]
            nickname[uid] = name
            events.append(("Enter", uid))
        elif action == "Leave":
            uid = parts[1]
            events.append(("Leave", uid))
        elif action == "Change":
            uid, name = parts[1], parts[2]
            nickname[uid] = name

    answer = []
    for action, uid in events:
        name = nickname[uid]
        if action == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        else:
            answer.append(f"{name}님이 나갔습니다.")

    return answer


if __name__ == "__main__":
    # 공식 예시
    record = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
    expected = [
        "Prodo님이 들어왔습니다.",
        "Ryan님이 들어왔습니다.",
        "Prodo님이 나갔습니다.",
        "Prodo님이 들어왔습니다.",
    ]
    assert solution(record) == expected

    # Change 만 있고 Enter/Leave 가 없으면 events 비어있음
    assert solution(["Enter uid1 A", "Change uid1 B", "Change uid1 C"]) == [
        "C님이 들어왔습니다."
    ]

    # 같은 uid 가 들락날락 + 마지막에 Change
    record2 = [
        "Enter uid1 A",
        "Leave uid1",
        "Enter uid1 B",
        "Leave uid1",
        "Change uid1 C",
    ]
    assert solution(record2) == [
        "C님이 들어왔습니다.",
        "C님이 나갔습니다.",
        "C님이 들어왔습니다.",
        "C님이 나갔습니다.",
    ]
    print("ok")
