// https://school.programmers.co.kr/learn/courses/30/lessons/42883
// 큰 수 만들기 - Lv.2
//
// 풀이 메모
// - 단조 감소 스택. 자릿수를 하나씩 보면서, 스택 top이 현재 숫자보다 작으면 k가 남아있는 한 pop.
//   더 큰 자릿수가 앞쪽에 오도록 양보.
// - 다 훑고도 k가 남으면 뒤에서부터 잘라낸다 (이 시점 스택은 단조 감소이므로 뒤가 가장 작음).
// - number 길이 최대 1,000,000. 각 문자가 push/pop 최대 1회씩이라 O(n).
// - 문자열 비교는 단일 자릿수라 사전순 = 숫자순. 변환 비용 없음.

function solution(number: string, k: number): string {
    const stack: string[] = [];
    let removed = 0;
    for (const ch of number) {
        while (removed < k && stack.length > 0 && stack[stack.length - 1] < ch) {
            stack.pop();
            removed++;
        }
        stack.push(ch);
    }
    while (removed < k) {
        stack.pop();
        removed++;
    }
    return stack.join("");
}

// --- 로컬 검증 ---
const tests: { number: string; k: number; expected: string }[] = [
    { number: "1924", k: 2, expected: "94" },
    { number: "1231234", k: 3, expected: "3234" },
    { number: "4177252841", k: 4, expected: "775841" },
    { number: "9999", k: 2, expected: "99" },     // 단조 감소 - 뒤에서 잘라내는 분기
    { number: "10000", k: 4, expected: "1" },     // 0 다수 케이스
    { number: "12345", k: 3, expected: "45" },    // 단조 증가
    { number: "54321", k: 2, expected: "543" },   // 단조 감소 + 뒤 잘라내기
];

let pass = 0;
for (const { number, k, expected } of tests) {
    const got = solution(number, k);
    const ok = got === expected;
    if (ok) pass++;
    console.log(`number="${number}", k=${k}`);
    console.log(`  got="${got}"`);
    console.log(`  exp="${expected}"  ${ok ? "PASS" : "FAIL"}`);
}
console.log(`\n${pass}/${tests.length} passed`);
