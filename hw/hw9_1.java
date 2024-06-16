package hw;

import java.util.Scanner;

// 계단오르기
public class hw9_1 {

	public static void main(String[] args) {
		System.out.println("hw9_1:최민우");
		Scanner input = new Scanner(System.in); // Scanner 객체 생성
		int n = input.nextInt(); // 계단 개수 입력

		// 계단별 점수 입력
		int[] scores = new int[n];
		for (int i = 0; i < n; i++) {
			scores[i] = input.nextInt(); // 각 계단의 점수를 입력받음
		}

		// 동적 프로그래밍을 위한 배열 선언
		int[] dp = new int[n]; // 각 계단까지의 최대 점수를 저장하는 배열
		int[] path = new int[n]; // 최대 점수를 얻기 위해 밟은 계단의 경로를 저장하는 배열

		// 초기값 설정
		dp[0] = scores[0]; // 첫 번째 계단의 점수는 자기 자신의 점수
		if (n > 1) {
			dp[1] = scores[0] + scores[1]; // 두 번째 계단의 점수는 첫 번째 계단과 두 번째 계단의 점수 합
		}
		if (n > 2) {
			dp[2] = Math.max(scores[0] + scores[2], scores[1] + scores[2]); // 세 번째 계단의 점수는 첫 번째 계단을 밟고 오는 경우와 두 번째 계단을 밟고 오는 경우 중 큰 값
			path[2] = (scores[0] + scores[2] > scores[1] + scores[2]) ? 0 : 1; // 어느 경로를 선택했는지 기록 (첫 번째 계단을 밟은 경우 0, 두 번째 계단을 밟은 경우 1)
		}

		// 동적 프로그래밍을 통한 최대 점수 계산
		for (int i = 3; i < n; i++) {
			if (dp[i - 2] + scores[i] > dp[i - 3] + scores[i - 1] + scores[i]) {
				dp[i] = dp[i - 2] + scores[i];
				path[i] = i - 2; // 두 칸 아래에서 오는 경로 기록
			} else {
				dp[i] = dp[i - 3] + scores[i - 1] + scores[i];
				path[i] = i - 1; // 한 칸을 건너뛰고 오는 경로 기록
			}
		}

		// 최대 점수 출력
		System.out.println(dp[n - 1]);

		// 최대 점수를 얻기 위해 밟은 계단의 점수 출력 메소드 호출
		printPath(n, scores, path);

		// Scanner 객체 닫기
		input.close();
	}

	// 최대 점수를 얻기 위해 밟은 계단의 점수를 추적 및 출력하는 메소드
	private static void printPath(int n, int[] scores, int[] path) {
		int idx = n - 1; // 마지막 계단부터 역추적
		int[] result = new int[n]; // 결과를 저장할 배열
		int count = 0; // 결과 배열의 인덱스를 위한 변수

		while (idx >= 0) {
			result[count++] = scores[idx]; // 현재 계단의 점수를 결과 배열에 저장
			if (path[idx] == idx - 2) {
				idx -= 2; // 두 칸 아래에서 온 경우 두 칸 아래로 이동
			} else if (path[idx] == idx - 1) {
				result[count++] = scores[idx - 1]; // 한 칸을 건너뛰고 온 경우 건너뛴 계단의 점수를 결과 배열에 저장
				idx -= 3; // 세 칸 아래로 이동
			}
		}

		// 결과 배열을 역순으로 출력하여 정렬된 형태로 출력
		for (int i = count - 1; i >= 0; i--) {
			System.out.print(result[i] + " ");
		}
	}
}
