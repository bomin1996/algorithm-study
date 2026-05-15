// https://school.programmers.co.kr/learn/courses/30/lessons/42746
// 가장 큰 수 - Lv.2
//
// 풀이 메모
// - 두 수 a, b를 이어붙일 때 어느 쪽을 앞에 둘지는 a+b vs b+a 문자열 비교로 결정.
//   두 문자열 길이가 같으므로 사전순 비교 = 숫자 대소 비교.
// - 원소 최대 1000이라 직접 수치로 a*10^len(b)+b를 만들면 전체 이어붙일 때 자릿수가
//   최대 300,000자리까지 갈 수 있다. 문자열 비교가 안전하고 단순.
// - 모두 0인 입력은 결과가 "000..."이 되므로 첫 글자만 보고 "0"으로 정규화.
// - 비교 문자열 길이는 최대 8자(1000+1000) 라 사실상 상수. 전체 O(n log n).

function solution(numbers: number[]): string {
    const strs = numbers.map(String);
    strs.sort((a, b) => (b + a).localeCompare(a + b));
    const joined = strs.join("");
    return joined[0] === "0" ? "0" : joined;
}

// --- 로컬 검증 ---
const tests: { input: number[]; expected: string }[] = [
    { input: [6, 10, 2], expected: "6210" },
    { input: [3, 30, 34, 5, 9], expected: "9534330" },
    { input: [0, 0, 0], expected: "0" },                       // 모두 0 정규화
    { input: [1000, 100, 10, 1], expected: "1101001000" },     // 같은 prefix, 짧은 쪽이 앞
    { input: [12, 121], expected: "12121" },                   // 12+121 vs 121+12
    { input: [21, 212], expected: "21221" },                   // 위와 반대 케이스
    { input: [0], expected: "0" },                             // 단일 0
];

let pass = 0;
for (const { input, expected } of tests) {
    const got = solution(input);
    const ok = got === expected;
    if (ok) pass++;
    console.log(`input=[${input.join(",")}]`);
    console.log(`  got="${got}"`);
    console.log(`  exp="${expected}"  ${ok ? "PASS" : "FAIL"}`);
}
console.log(`\n${pass}/${tests.length} passed`);
