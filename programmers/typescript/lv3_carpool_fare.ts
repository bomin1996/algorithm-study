// https://school.programmers.co.kr/learn/courses/30/lessons/72413
// 합승 택시 요금 - Lv.3 (2021 KAKAO BLIND RECRUITMENT)
//
// 풀이 메모
// - S에서 출발해 어느 지점 X까지 함께 타고, 거기서 A/B가 각자 이동하는 최소 합 요금.
// - X = S 인 경우(처음부터 따로) 포함해 dist[S][X] + dist[X][A] + dist[X][B] 의 최솟값.
// - n <= 200, fares <= 10000 이므로 플로이드-워셜 O(n^3) = 8e6 으로 충분.
// - 양방향 간선이고 자기 자신은 0. 초기값은 INF.

const INF = Number.POSITIVE_INFINITY;

function solution(n: number, s: number, a: number, b: number, fares: number[][]): number {
    const dist: number[][] = Array.from({ length: n + 1 }, () =>
        new Array<number>(n + 1).fill(INF),
    );
    for (let i = 1; i <= n; i++) dist[i][i] = 0;

    for (const [c, d, f] of fares) {
        if (f < dist[c][d]) {
            dist[c][d] = f;
            dist[d][c] = f;
        }
    }

    for (let k = 1; k <= n; k++) {
        for (let i = 1; i <= n; i++) {
            if (dist[i][k] === INF) continue;
            for (let j = 1; j <= n; j++) {
                const via = dist[i][k] + dist[k][j];
                if (via < dist[i][j]) dist[i][j] = via;
            }
        }
    }

    let best = dist[s][a] + dist[s][b];
    for (let x = 1; x <= n; x++) {
        const cur = dist[s][x] + dist[x][a] + dist[x][b];
        if (cur < best) best = cur;
    }
    return best;
}

// --- 로컬 검증 ---
const tests: {
    n: number;
    s: number;
    a: number;
    b: number;
    fares: number[][];
    expected: number;
}[] = [
    {
        n: 6,
        s: 4,
        a: 6,
        b: 2,
        fares: [
            [4, 1, 10],
            [3, 5, 24],
            [5, 6, 2],
            [3, 1, 41],
            [5, 1, 24],
            [4, 6, 50],
            [2, 4, 66],
            [2, 3, 22],
            [1, 6, 25],
        ],
        expected: 82,
    },
    {
        n: 7,
        s: 3,
        a: 4,
        b: 1,
        fares: [
            [5, 7, 9],
            [4, 6, 4],
            [3, 6, 1],
            [3, 2, 3],
            [2, 1, 6],
        ],
        expected: 14,
    },
    {
        n: 6,
        s: 4,
        a: 5,
        b: 6,
        fares: [
            [2, 6, 6],
            [6, 3, 7],
            [4, 6, 7],
            [6, 5, 11],
            [2, 5, 12],
            [5, 3, 20],
            [2, 4, 8],
            [4, 3, 9],
        ],
        expected: 18,
    },
];

let pass = 0;
for (const { n, s, a, b, fares, expected } of tests) {
    const got = solution(n, s, a, b, fares);
    const ok = got === expected;
    if (ok) pass++;
    console.log(`n=${n} s=${s} a=${a} b=${b}`);
    console.log(`  got=${got}  exp=${expected}  ${ok ? "PASS" : "FAIL"}`);
}
console.log(`\n${pass}/${tests.length} passed`);
