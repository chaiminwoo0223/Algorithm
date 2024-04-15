package lab;

import java.util.Scanner;

// 숫자 세기
public class lab0_1 {

	public static void main(String[] args) {
		System.out.println("lab0_1:최민우");
		Scanner scanner = new Scanner(System.in); // Scanner 객체 생성

		// 사용자로부터 배열의 크기 입력받기
		int n = scanner.nextInt();

		// 사용자로부터 정수 입력받아 배열에 저장
		int[] nums = new int[n];
		for (int i = 0; i < n; i++) {
			nums[i] = scanner.nextInt();
		}

		// 평균 계산
		double mean = calculateAverage(nums);

		// 평균값보다 큰 원소의 수 계산
		int count = 0;
		for (int num : nums) {
			if (num > mean) {
				count += 1; // 평균값보다 큰 경우, 카운트 증가
			}
		}

		// 출력
		System.out.println(mean);
		System.out.println(count);
		scanner.close(); // Scanner 객체 닫기
	}

	// 평균을 계산하는 메소드
	private static double calculateAverage(int[] nums) {
		double sum = 0;
		for (int num : nums) {
			sum += num; // 배열의 각 원소를 합계에 더함
		}
		return sum / nums.length; // 합계를 배열의 길이로 나누어 평균을 계산
	}
}