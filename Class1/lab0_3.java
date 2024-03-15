package Class1;

import java.util.Scanner;

// 배열 검색
public class lab0_3 {

	public static void main(String[] args) {
		System.out.println("lab0_3:최민우");

		// 정렬되지 않은 정수 배열 array, 정렬된 정수 배열 sortedArray
		int array[] = {120, 990, 130, 150, 20, 300, 400, 990, 40, 100, 110, 150, 60, 80, 190, 200};
		int sortedArray[] = {20, 40, 60, 80, 100, 110, 120, 130, 150, 150, 190, 200, 300, 400, 990, 990};

		// 검색할 정수를 입력받음
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();

		// 출력
		System.out.println(sequentialSearch(array, n)); // 순차검색 결과(인덱스)
		System.out.println(binarySearch(sortedArray, n)); // 이진검색 결과(인덱스)
		scanner.close(); // Scanner 객체 닫기
	}

	// 원소를 맨 앞부터 찾는 순차검색 메소드
	private static int sequentialSearch(int[] array, int n) {
		for (int i = 0; i < array.length; i++) {
			if (array[i] == n) {
				return i; // 검색 성공
			}
		}
		return -1; // 검색 실패
	}

	// 중간값을 이용한 이진검색 메소드
	private static int binarySearch(int[] sortedArray, int n) {
		int left = 0;
		int right = sortedArray.length - 1;

		while(left <= right) {
			int middle = left + ((right - left) / 2); // 정수 연산 -> 정수 반환
			if (sortedArray[middle] == n) {
				return middle; // 검색 성공
			}
			else if (sortedArray[middle] < n) {
				left = middle + 1; // 검색할 정수가 중간값보다 큰 경우
			}
			else {
				right = middle - 1; // 검색할 정수가 중간값보다 작은 경우
			}
		}
		return -1; // 검색 실패
	}
}