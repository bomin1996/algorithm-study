// https://school.programmers.co.kr/learn/courses/30/lessons/43105
// 정수 삼각형 - Lv.3
//
// 풀이 메모
// - 맨 위 칸에서 시작해 아래로 내려가며, 현재 칸과 대각선으로 인접한
//   (바로 아래 같은 열 또는 그 다음 열) 칸으로만 이동할 수 있다.
//   거쳐 간 숫자의 합이 최대가 되는 경로의 합을 구한다.
// - DP: dp[r][c] = (r,c)까지 내려오는 동안의 최대 합.
//   위에서 (r,c)로 올 수 있는 칸은 (r-1, c-1) 과 (r-1, c) 둘뿐이다.
//   dp[r][c] = triangle[r][c] + max(dp[r-1][c-1], dp[r-1][c]).
//   단 c == 0 이면 (r-1, c-1) 이 없고, c == r 이면 (r-1, c) 가 없다.
// - 답은 마지막 행 dp 값들의 최댓값.
// - 행 수 n <= 500, 칸 값 0~9999. O(n^2) 으로 충분.

import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;
        int[][] dp = new int[n][];
        dp[0] = new int[] { triangle[0][0] };

        for (int r = 1; r < n; r++) {
            dp[r] = new int[r + 1];
            for (int c = 0; c <= r; c++) {
                int best;
                if (c == 0) {
                    best = dp[r - 1][c];          // 왼쪽 끝: 바로 위 칸만 가능
                } else if (c == r) {
                    best = dp[r - 1][c - 1];       // 오른쪽 끝: 왼쪽 위 칸만 가능
                } else {
                    best = Math.max(dp[r - 1][c - 1], dp[r - 1][c]);
                }
                dp[r][c] = triangle[r][c] + best;
            }
        }

        int answer = 0;
        for (int v : dp[n - 1]) {
            answer = Math.max(answer, v);
        }
        return answer;
    }
}

public class lv3_integer_triangle {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][][] inputs = {
            {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}}, // 예제: 답 30
            {{1}},                                                    // 단일 칸: 답 1
            {{0}, {0, 0}, {0, 0, 0}},                                 // 전부 0: 답 0
            {{1}, {2, 1}, {1, 2, 1}, {2, 1, 2, 1}},                   // 항상 왼쪽 큰 값: 1+2+2+2=7
            {{5}, {9, 1}},                                            // 두 행: 5+9=14
        };
        int[] expected = {30, 1, 0, 7, 14};

        int pass = 0;
        for (int i = 0; i < inputs.length; i++) {
            int got = sol.solution(inputs[i]);
            boolean ok = got == expected[i];
            if (ok) pass++;
            System.out.println("triangle=" + Arrays.deepToString(inputs[i]));
            System.out.println("  got=" + got + "  exp=" + expected[i] + "  " + (ok ? "PASS" : "FAIL"));
        }
        System.out.println("\n" + pass + "/" + inputs.length + " passed");
    }
}
