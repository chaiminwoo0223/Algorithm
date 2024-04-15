package hw;

import java.util.Scanner;

// merge sort
public class hw4_2 {

	public static void main(String[] args) {
		System.out.println("hw4_2:최민우");

		// 사용자로부터 원소 개수(n)와 n개의 실수값을 입력받아 배열에 저장
		Scanner scanner = new Scanner(System.in); // Scanner 객체 생성
		int n = scanner.nextInt(); // 원소 개수(n) 입력
		double[] array = new double[n]; // 실수값을 저장할 배열 선언
		for (int i = 0; i < n; i++) { // n개의 실수값을 입력
			array[i] = scanner.nextDouble();
		}

		// 배열 원소들을 병합 정렬 알고리즘을 이용하여 정수부 기준으로 오름차순 정렬
		mergeSort(array, 0, n - 1); // 병합 정렬

		// 정렬된 배열 원소들을 출력
		for (int i = 0; i < n; i++) {
			System.out.print(array[i] + " ");
		}
		scanner.close(); // Scanner 객체 닫기
	}

	// 배열 array[p...r]을 정렬
	private static void mergeSort(double[] array, int p, int r) {
		if (p < r) {
			int q = (p + r) / 2; // p, r 중간 지점 계산
			mergeSort(array, p, q); // 전반부 정렬
			mergeSort(array, q + 1, r); // 후반부 정렬
			merge(array, p, q, r); // 병합
		}
	}

	// 배열의 두 부분을 정수부 기준으로 병합
	private static void merge(double[] array, int p, int q, int r) {
     double[] temp = new double[r - p + 1]; // 병합 결과를 임시 저장할 temp 배열
     int i = p; int j = q + 1; int t = 0;

     // 전반부와 후반부를 비교하며 정수부 기준으로 병합
     while (i <= q && j <= r) {
         if ((int)array[i] <= (int)array[j]) {
             temp[t++] = array[i++]; // 전반부
         } else {
             temp[t++] = array[j++]; // 후반부
         }
     }

     // 왼쪽 부분 배열이 남은 경우
     while (i <= q) {
         temp[t++] = array[i++];
     }

     // 오른쪽 부분 배열이 남은 경우
     while (j <= r) {
         temp[t++] = array[j++];
     }

     // temp 배열의 내용을 array[p...r]로 복사
     for (t = 0, i = p; i <= r; t++, i++) {
         array[i] = temp[t];
     }
 }
}