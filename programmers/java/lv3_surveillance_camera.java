// https://school.programmers.co.kr/learn/courses/30/lessons/42884
// 단속카메라 - Lv.3
//
// 풀이 메모
// - 고속도로에 진입(진출) 지점이 주어진 차량들이 있고, 한 지점에 카메라를 두면
//   진입 <= 카메라위치 <= 진출 인 모든 차량을 동시에 단속할 수 있다.
//   모든 차량이 최소 한 번은 단속되도록 하는 카메라 최소 개수를 구한다.
// - 그리디: 진출 지점(out) 기준 오름차순 정렬.
//   가장 먼저 빠져나가는 차량의 진출 지점에 카메라를 두는 것이 항상 최적이다.
//   (그 차량을 잡으려면 카메라는 진출 지점 이하에 있어야 하고, 가능한 오른쪽=진출 지점에
//    둘수록 뒤따르는 차량과 겹칠 여지가 가장 크다.)
// - 정렬 후 순회하며 현재 차량의 진입(in)이 마지막 카메라 위치보다 크면
//   아직 못 잡은 차량이므로 그 차량의 진출 지점에 새 카메라를 설치.
// - routes 최대 10,000개. 정렬 O(n log n), 순회 O(n).
// - 좌표 범위 -30,000 ~ 30,000 이므로 카메라 초기값은 그보다 작은 값으로 둔다.

import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        // 진출 지점 오름차순 정렬
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));

        int cameras = 0;
        int lastCamera = Integer.MIN_VALUE; // 마지막으로 설치한 카메라 위치

        for (int[] route : routes) {
            int in = route[0];
            int out = route[1];
            // 이 차량의 진입 지점이 마지막 카메라보다 뒤라면 아직 단속되지 않은 차량
            if (in > lastCamera) {
                cameras++;
                lastCamera = out; // 진출 지점에 새 카메라 설치
            }
        }
        return cameras;
    }
}

public class lv3_surveillance_camera {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][][] inputs = {
            {{-20, -15}, {-14, -5}, {-18, -13}, {-5, -3}}, // 예제: 답 2
            {{0, 0}},                                       // 단일 차량: 답 1
            {{-30000, 30000}, {-30000, 30000}},            // 전 구간 겹침: 카메라 1개
            {{0, 1}, {2, 3}, {4, 5}},                       // 서로 안 겹침: 답 3
            {{-10, -8}, {-8, -6}, {-6, -4}},                // 경계 공유(진출==진입): 답 2
        };
        int[] expected = {2, 1, 1, 3, 2};

        int pass = 0;
        for (int i = 0; i < inputs.length; i++) {
            // 정렬이 입력 배열을 변형하므로 출력용 사본을 따로 만든다
            int[][] original = deepCopy(inputs[i]);
            int got = sol.solution(inputs[i]);
            boolean ok = got == expected[i];
            if (ok) pass++;
            System.out.println("routes=" + Arrays.deepToString(original));
            System.out.println("  got=" + got + "  exp=" + expected[i] + "  " + (ok ? "PASS" : "FAIL"));
        }
        System.out.println("\n" + pass + "/" + inputs.length + " passed");
    }

    private static int[][] deepCopy(int[][] src) {
        int[][] copy = new int[src.length][];
        for (int i = 0; i < src.length; i++) {
            copy[i] = src[i].clone();
        }
        return copy;
    }
}
