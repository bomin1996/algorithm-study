// 백준 1753 - 최단경로 (Gold V)
// https://www.acmicpc.net/problem/1753
//
// 방향 가중 그래프에서 시작 정점으로부터 모든 정점까지의 최단 거리를 구한다.
// 가중치는 1 이상 10 이하의 양수이므로 다익스트라가 적합하다.
//
// 풀이 메모
// - V <= 20000, E <= 300000. 인접 리스트 + 이진 힙 다익스트라로 O(E log V).
// - 음수 간선이 없으므로 한 번 확정된(팝된) 정점은 다시 갱신하지 않는다.
// - 같은 정점이 거리만 다르게 힙에 여러 번 들어갈 수 있으므로,
//   팝한 거리가 이미 확정된 dist 보다 크면 흘러간 항목으로 보고 건너뛴다(lazy deletion).
// - 도달 불가능한 정점은 INF 로 두고 출력 시 "INF" 로 바꾼다.
// - 정점 번호가 1..V 이고 시작점이 거듭 주어질 수 있는 자기 루프/중복 간선도
//   그대로 두면 된다(최단거리에는 영향 없음).

const INF = Number.POSITIVE_INFINITY;

// (거리, 정점) 쌍을 거리 기준 최소 힙으로 관리한다.
// 숫자 두 개를 객체 대신 단일 배열에 [dist, node, dist, node, ...] 로 평탄화하면
// 객체 할당이 줄어 대량 간선에서도 부담이 적다.
class MinHeap {
    private dist: number[] = [];
    private node: number[] = [];

    get size(): number {
        return this.dist.length;
    }

    push(d: number, n: number): void {
        this.dist.push(d);
        this.node.push(n);
        let i = this.dist.length - 1;
        while (i > 0) {
            const parent = (i - 1) >> 1;
            if (this.dist[parent] <= this.dist[i]) break;
            this.swap(i, parent);
            i = parent;
        }
    }

    // 최소 거리 항목을 꺼내 [dist, node] 로 돌려준다.
    pop(): [number, number] {
        const topD = this.dist[0];
        const topN = this.node[0];
        const lastD = this.dist.pop()!;
        const lastN = this.node.pop()!;
        if (this.dist.length > 0) {
            this.dist[0] = lastD;
            this.node[0] = lastN;
            this.siftDown(0);
        }
        return [topD, topN];
    }

    private siftDown(i: number): void {
        const n = this.dist.length;
        while (true) {
            const left = i * 2 + 1;
            const right = left + 1;
            let smallest = i;
            if (left < n && this.dist[left] < this.dist[smallest]) smallest = left;
            if (right < n && this.dist[right] < this.dist[smallest]) smallest = right;
            if (smallest === i) break;
            this.swap(i, smallest);
            i = smallest;
        }
    }

    private swap(a: number, b: number): void {
        const td = this.dist[a];
        this.dist[a] = this.dist[b];
        this.dist[b] = td;
        const tn = this.node[a];
        this.node[a] = this.node[b];
        this.node[b] = tn;
    }
}

interface Edge {
    to: number;
    weight: number;
}

// 1..v 정점, 시작점 start 로부터의 최단 거리 배열(인덱스 1..v)을 반환한다.
// 도달 불가능한 정점은 INF.
function dijkstra(v: number, start: number, graph: Edge[][]): number[] {
    const dist = new Array<number>(v + 1).fill(INF);
    dist[start] = 0;

    const heap = new MinHeap();
    heap.push(0, start);

    while (heap.size > 0) {
        const [d, cur] = heap.pop();
        if (d > dist[cur]) continue; // 이미 더 짧은 경로로 확정된 흘러간 항목

        for (const { to, weight } of graph[cur]) {
            const nd = d + weight;
            if (nd < dist[to]) {
                dist[to] = nd;
                heap.push(nd, to);
            }
        }
    }

    return dist;
}

function main(): void {
    const data = require("fs").readFileSync(0, "utf8");
    // 공백/개행 단위로 정수 토큰을 순서대로 소비한다.
    const tokens = data.split(/\s+/);
    let p = 0;
    const next = (): number => Number(tokens[p++]);

    const v = next();
    const e = next();
    const start = next();

    const graph: Edge[][] = Array.from({ length: v + 1 }, () => []);
    for (let i = 0; i < e; i++) {
        const u = next();
        const w = next();
        const c = next();
        graph[u].push({ to: w, weight: c });
    }

    const dist = dijkstra(v, start, graph);

    const out: string[] = new Array(v);
    for (let i = 1; i <= v; i++) {
        out[i - 1] = dist[i] === INF ? "INF" : String(dist[i]);
    }
    process.stdout.write(out.join("\n") + "\n");
}

main();
