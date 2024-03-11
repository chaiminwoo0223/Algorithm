package Class1;

import java.util.Scanner;

// 재귀 알고리즘
public class lab0_2 {

	public static void main(String[] args) {
		System.out.println("lab0_2:최민우");
		Scanner scanner = new Scanner(System.in); // Scanner 객체 생성
		int n = scanner.nextInt(); // 사용자로부터 정수 n 입력받기
		System.out.println(total(n)); // 합계
		show(n); // 정수 리스트
		scanner.close(); // Scanner 객체 닫기
	}

	// 1부터 n까지의 합을 구하여 리턴하는 메소드
	private static int total(int n) {
		if (n == 1) {
			return 1;
		}
		return n + total(n - 1);
	}

	// 1부터 n까지의 정수를 출력하는 메소드
	private static void show(int n) {
		if (n > 0) {
			show(n - 1);
			System.out.print(n + " ");
		}
	}
}