// 백준 2206 - 벽 부수고 이동하기 (Gold III)
// https://www.acmicpc.net/problem/2206
//
// N x M 0/1 격자에서 (1,1) -> (N,M) 최단 경로의 칸 수를 구한다.
// 0 은 이동 가능, 1 은 벽. 단, 이동 중 벽을 "최대 한 번" 부수고 지나갈 수 있다.
// 도달 불가능하면 -1.
//
// 풀이 메모
// - 단순 격자 BFS 라면 visited[r][c] 면 충분하지만, "벽을 한 번 부쉈는지"라는
//   상태가 경로마다 다르므로 차원을 하나 더 붙인다: visited[r][c][broken], broken in {0,1}.
//   같은 칸이라도 벽을 안 부수고 온 경우와 부수고 온 경우는 이후 선택지가 다르기 때문에
//   별개의 상태로 취급해야 한다.
// - 가중치가 모두 1(한 칸 이동)이므로 BFS 로 최단 칸 수를 보장한다.
// - 다음 칸이 벽(1)이면: 아직 벽을 안 부쉈을 때(broken===0)만 부수고 진입(broken->1).
//   다음 칸이 길(0)이면: 현재 broken 상태 그대로 진입.
// - 칸 수는 시작 칸을 1 로 세고 이동할 때마다 +1. 도착 칸에서의 dist 가 정답.
// - N,M <= 1000 이라 상태 수는 최대 2 * 10^6. 큐는 고정 크기 배열로 운용해 부담을 줄인다.

const DR = [-1, 1, 0, 0];
const DC = [0, 0, -1, 1];

// 격자(각 행은 '0'/'1' 문자열)에서 (0,0) -> (n-1,m-1) 최단 칸 수.
// 벽을 최대 한 번 부술 수 있고, 불가능하면 -1 을 반환한다.
function breakWallBfs(grid: string[], n: number, m: number): number {
    // visited[broken][r][c] — broken 은 지금까지 벽을 부순 횟수(0 또는 1).
    const visited = [
        Array.from({ length: n }, () => new Uint8Array(m)),
        Array.from({ length: n }, () => new Uint8Array(m)),
    ];

    // 큐를 [r, c, broken] 평탄화 배열로. 최대 노드 수 = 2*n*m.
    const cap = 2 * n * m;
    const qr = new Int32Array(cap);
    const qc = new Int32Array(cap);
    const qb = new Uint8Array(cap);
    let head = 0;
    let tail = 0;

    qr[tail] = 0;
    qc[tail] = 0;
    qb[tail] = 0;
    tail++;
    visited[0][0][0] = 1;

    let dist = 1; // 시작 칸 포함
    while (head < tail) {
        const levelEnd = tail; // 현재 거리(dist)에 해당하는 노드들의 끝 경계
        while (head < levelEnd) {
            const r = qr[head];
            const c = qc[head];
            const b = qb[head];
            head++;

            if (r === n - 1 && c === m - 1) return dist;

            for (let d = 0; d < 4; d++) {
                const nr = r + DR[d];
                const nc = c + DC[d];
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;

                if (grid[nr][nc] === "1") {
                    // 벽: 아직 한 번도 안 부쉈을 때만 부수고 진입.
                    if (b === 0 && visited[1][nr][nc] === 0) {
                        visited[1][nr][nc] = 1;
                        qr[tail] = nr;
                        qc[tail] = nc;
                        qb[tail] = 1;
                        tail++;
                    }
                } else {
                    // 길: 현재 broken 상태 그대로 진입.
                    if (visited[b][nr][nc] === 0) {
                        visited[b][nr][nc] = 1;
                        qr[tail] = nr;
                        qc[tail] = nc;
                        qb[tail] = b;
                        tail++;
                    }
                }
            }
        }
        dist++;
    }

    return -1;
}

function main(): void {
    const data = require("fs").readFileSync(0, "utf8");
    const lines = data.split("\n");

    const [n, m] = lines[0].split(" ").map(Number);
    const grid: string[] = [];
    for (let i = 1; i <= n; i++) grid.push(lines[i].trim());

    process.stdout.write(String(breakWallBfs(grid, n, m)) + "\n");
}

main();
