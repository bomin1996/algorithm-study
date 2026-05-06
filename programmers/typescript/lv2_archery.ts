// https://school.programmers.co.kr/learn/courses/30/lessons/92342
// 양궁대회 - Lv.2 (2022 KAKAO BLIND RECRUITMENT)
//
// 풀이 메모
// - 점수판 11칸(10점~0점)에 대해 라이언이 "이긴다(어피치+1발)" / "포기(0발)" 두 분기 백트래킹.
// - 끝에 다다르면 남은 화살은 0점에 몰아넣고 점수 차 계산.
// - 동률이면 낮은 점수(인덱스 큰 쪽)에서 더 많이 맞힌 배치를 우선.
// - 이긴 케이스가 한 번도 없으면 [-1] 반환.
// - 분기 수 최대 2^11 = 2048, n <= 10 이라 상수 시간 수준.

function solution(n: number, info: number[]): number[] {
    const ryan: number[] = new Array(11).fill(0);
    let bestDiff = 0;
    let bestRyan: number[] = [-1];

    const score = (arr: number[]): [number, number] => {
        let r = 0;
        let a = 0;
        for (let i = 0; i < 11; i++) {
            if (info[i] === 0 && arr[i] === 0) continue;
            const point = 10 - i;
            if (arr[i] > info[i]) r += point;
            else a += point;
        }
        return [r, a];
    };

    // 낮은 점수에서 더 많이 맞힌 쪽이 cur이면 true
    const preferCur = (cur: number[], best: number[]): boolean => {
        for (let i = 10; i >= 0; i--) {
            if (cur[i] !== best[i]) return cur[i] > best[i];
        }
        return false;
    };

    const dfs = (idx: number, left: number): void => {
        if (idx === 11) {
            ryan[10] += left;
            const [r, a] = score(ryan);
            const diff = r - a;
            if (diff > 0) {
                if (diff > bestDiff || (diff === bestDiff && preferCur(ryan, bestRyan))) {
                    bestDiff = diff;
                    bestRyan = [...ryan];
                }
            }
            ryan[10] -= left;
            return;
        }

        const need = info[idx] + 1;
        if (left >= need) {
            ryan[idx] = need;
            dfs(idx + 1, left - need);
            ryan[idx] = 0;
        }

        dfs(idx + 1, left);
    };

    dfs(0, n);
    return bestRyan;
}

// --- 로컬 검증 ---
const tests: { n: number; info: number[]; expected: number[] }[] = [
    { n: 5, info: [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], expected: [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0] },
    { n: 1, info: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], expected: [-1] },
    { n: 9, info: [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1], expected: [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0] },
    { n: 10, info: [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3], expected: [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2] },
];

let pass = 0;
for (const { n, info, expected } of tests) {
    const got = solution(n, info);
    const ok = JSON.stringify(got) === JSON.stringify(expected);
    if (ok) pass++;
    console.log(`n=${n}`);
    console.log(`  got=[${got}]`);
    console.log(`  exp=[${expected}]  ${ok ? "PASS" : "FAIL"}`);
}
console.log(`\n${pass}/${tests.length} passed`);
