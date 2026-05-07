// https://school.programmers.co.kr/learn/courses/30/lessons/60058
// 괄호 변환 - Lv.2 (2020 KAKAO BLIND RECRUITMENT)
//
// 풀이 메모
// - 문제 정의 자체가 재귀 절차라 그대로 옮기면 끝.
// - "균형잡힌": '(' 수 == ')' 수. "올바른": 스택 매칭 시 깊이가 음수로 떨어지지 않음.
// - split(w): 더 이상 쪼갤 수 없는 균형 prefix u, 나머지 v 로 분리 (open == close 가 처음 만나는 지점).
// - u 가 올바르면 u + f(v).
// - 그렇지 않으면 "(" + f(v) + ")" + reverse(u[1..n-1]).
// - 입력 길이 <= 1000, 재귀 깊이도 그 절반 수준이라 무난.

function solution(p: string): string {
    const isCorrect = (s: string): boolean => {
        let depth = 0;
        for (const ch of s) {
            depth += ch === "(" ? 1 : -1;
            if (depth < 0) return false;
        }
        return depth === 0;
    };

    const split = (s: string): [string, string] => {
        let open = 0;
        let close = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] === "(") open++;
            else close++;
            if (open === close) return [s.slice(0, i + 1), s.slice(i + 1)];
        }
        return [s, ""];
    };

    const flip = (s: string): string => {
        let out = "";
        for (const ch of s) out += ch === "(" ? ")" : "(";
        return out;
    };

    const convert = (w: string): string => {
        if (w.length === 0) return "";
        const [u, v] = split(w);
        if (isCorrect(u)) return u + convert(v);
        return "(" + convert(v) + ")" + flip(u.slice(1, -1));
    };

    return convert(p);
}

// --- 로컬 검증 ---
const tests: { p: string; expected: string }[] = [
    { p: "(()())()", expected: "(()())()" },
    { p: ")(", expected: "()" },
    { p: "()))((()", expected: "()(())()" },
    { p: "", expected: "" },
    { p: "()", expected: "()" },
    { p: "(((())))", expected: "(((())))" },
];

let pass = 0;
for (const { p, expected } of tests) {
    const got = solution(p);
    const ok = got === expected;
    if (ok) pass++;
    console.log(`p="${p}"`);
    console.log(`  got="${got}"`);
    console.log(`  exp="${expected}"  ${ok ? "PASS" : "FAIL"}`);
}
console.log(`\n${pass}/${tests.length} passed`);
