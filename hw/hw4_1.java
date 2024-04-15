package hw;

import java.util.Scanner;

// quick sort
public class hw4_1 {

	public static void main(String[] args) {
		System.out.println("hw4_1:최민우");

		// 사용자로부터 원소 개수(n)와 n개의 실수값을 입력받아 배열에 저장
		Scanner scanner = new Scanner(System.in); // Scanner 객체 생성
		int n = scanner.nextInt(); // 원소 개수(n) 입력
		double[] array = new double[n]; // 실수값을 저장할 배열 선언
		for (int i = 0; i < n; i++) { // n개의 실수값을 입력
			array[i] = scanner.nextDouble();
		}

		// 배열 원소들을 퀵 정렬 알고리즘을 이용하여 정수부 기준으로 오름차순 정렬
		quickSort(array, 0, n - 1); // 퀵 정렬

		// 정렬된 배열 원소들을 출력
		for (int i = 0; i < n; i++) {
			System.out.print(array[i] + " ");
		}
		scanner.close(); // Scanner 객체 닫기
	}

	// 배열 array[p...r]을 정렬
	private static void quickSort(double[] array, int p, int r) {
		if (p < r) {
			int q = partition(array, p, r); // 분할
			quickSort(array, p, q - 1); // 왼쪽 배열 정렬
			quickSort(array, q + 1, r); // 오른쪽 배열 정렬
		}
	}

	// array[p...r]을 분할하여 기준원소 인덱스를 리턴
	private static int partition(double[] array, int p, int r) {
	    double x = array[r]; // 기준 원소
	    int i = p - 1; // i는 1구역의 끝 지점
	    for (int j = p; j < r; j++) { // j는 3구역의 시작 지점
	    	 if ((int)array[j] < (int)x) {
	            swap(array, ++i, j); // i값 증가 후, array[i]와 array[j] 교환
	        }
	    }
	    swap(array, i + 1, r); // 기준 원소를 올바른 위치로 이동
	    return i + 1; // 기준 원소의 새 위치 반환
	}

	// 배열의 두 원소의 위치를 교환
	private static void swap(double[] array, int i, int j) {
	    double temp = array[i];
	    array[i] = array[j];
	    array[j] = temp;
	}
}