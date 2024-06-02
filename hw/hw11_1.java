package hw;

import java.util.Arrays;
import java.util.Scanner;

// 동전 바꾸기
public class hw11_1 {

	public static void main(String[] args) {
		System.out.println("hw11_1:최민우");
		Scanner input = new Scanner(System.in); // 입력을 위한 Scanner 객체 생성

		int n = input.nextInt(); // 동전 액면 갯수 입력받음
		int[] coins = new int[n]; // 동전 액면을 저장할 배열

		// 동전 액면 입력받기
		for (int i = 0; i < n; i++) {
			coins[i] = input.nextInt();
		}

		Arrays.sort(coins); // 동전 액면을 오름차순으로 정렬

		// 동전 액면이 모두 바로 아래 액면의 배수인지 검사
		boolean valid = true;
		for (int i = 1; i < n; i++) {
			if (coins[i] % coins[i - 1] != 0) {
				valid = false;
				break;
			}
		}

		if (!valid) {
			System.out.println("그리디 알고리즘은 최적해를 보장하지 않습니다.");
		} else {
			int amount = input.nextInt(); // 거스름돈 액수 입력받음
			int[] result = new int[n]; // 결과를 저장할 배열

			// 그리디 알고리즘을 이용하여 거스름돈 액수에 대한 최적해를 구함
			for (int i = n - 1; i >= 0; i--) {
				if (amount >= coins[i]) {
					result[i] = amount / coins[i];
					amount %= coins[i];
				}
			}

			// 최적해를 구하는 과정에서 거스름돈 액수를 맞출 수 없으면 실패
			if (amount != 0) {
				System.out.println("원하는 거스름돈 액수를 맞출 수 없습니다.");
			} else {
				// 최적해 출력
				for (int i = n - 1; i >= 0; i--) {
					if (result[i] > 0) {
						System.out.println(coins[i] + " x " + result[i]);
					}
				}
			}
		}
		input.close(); // Scanner 객체 닫기
	}
}