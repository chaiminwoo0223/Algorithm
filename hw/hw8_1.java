package hw;

import java.util.Scanner;

// 상호배타적 집합 구현
public class hw8_1 {

	public static void main(String[] args) {
		System.out.println("hw8_1:최민우");
		Scanner input = new Scanner(System.in); // Scanner 객체 생성

		// 사용자가 원하는 갯수의 원소를 갖는 상호배타적 집합 MySet 객체를 생성(set)
		int n = input.nextInt(); // 원소 개수(n) 입력
		MySet set = new MySet(n); // n개의 원소를 갖는 MySet 객체 생성

		// 사용자가 원하는 횟수의 union 연산을 수행
		int m = input.nextInt(); // union 연산의 수
		for(int i = 0; i < m; i++) {
			int x = input.nextInt(); // 첫 번째 원소
			int y = input.nextInt(); // 두 번째 원소
			set.union(x,y); // 두 원소를 합치는 union 연산 수행
		}

		// 트리 구현을 확인하기 위해, 모든 원소에 대해 각 원소의 부모를 출력
		set.printParent(); // 모든 원소의 부모를 출력

		// 모든 원소에 대해 findSet 연산을 수행
		for (int x = 0; x < n; x++) {
			set.findSet(x); // x의 대표원소 찾기
		}

		// 트리 구현을 확인하기 위해, 모든 원소에 대해 각 원소의 부모를 출력
		set.printParent(); // 모든 원소의 부모를 출력

		// Scanner 객체 닫기
		input.close();
	}
}

// 트리를 이용하여 상호배타적 집합을 구현하는 클래스
class MySet {
	private int[] parent; // 각 원소의 부모를 저장하는 배열

	// 생성자: 원소 수 n을 매개변수로 받아 집합 객체를 초기화
	public MySet(int n) {
		parent = new int[n];
		for (int i = 0; i < n; i++) {
			makeSet(i); // 각 원소에 대해 makeSet 연산 수행
		}
	}

	// makeSet 연산: x 하나로 이루어진 집합을 만듦
	public void makeSet(int x) {
		parent[x] = x; // 자기 자신을 부모로 설정
	}

	// findSet 연산: x의 대표 원소를 찾되 경로압축 사용
	public int findSet(int x) {
		if (x != parent[x]) {
			parent[x] = findSet(parent[x]); // 경로 압축 수행
		}
		return parent[x];
	}

	// union 연산: x와 y가 속한 집합을 합치되, x의 대표원소가 최종 대표원소가 되도록 함
	public void union(int x, int y) {
		int rootX = findSet(x); // x의 대표원소 찾기
		int rootY = findSet(y); // y의 대표원소 찾기
		if (rootX != rootY) {
			parent[rootY] = rootX; // y의 대표원소의 부모를 x의 대표원소로 설정
		}
	}

	// printParent: 모든 원소에 대해 각 노드의 부모를 출력하여 구조 확인
    public void printParent() {
        for (int i = 0; i < parent.length; i++) {
            if (i > 0) {
				System.out.print(" ");
			}
            System.out.print(parent[i]);
        }
        System.out.println(); // 줄바꿈 추가
    }
}