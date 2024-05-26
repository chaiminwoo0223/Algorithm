package hw;

import java.util.Scanner;

// 최소 신장 트리
public class hw10_1 {

	public static void main(String[] args) {
		System.out.println("hw10_1 : 최민우");
		Scanner input = new Scanner(System.in); // 입력을 위한 Scanner 객체 생성

		int n = input.nextInt(); // 정점 수 입력받음
		int e = input.nextInt(); // 간선 수 입력받음
		int[][] edges = new int[e][3]; // 간선 목록을 저장할 배열

		// 간선 입력받기
		for (int i = 0; i < e; i++) {
			edges[i][0] = input.nextInt(); // 간선의 첫 번째 정점
			edges[i][1] = input.nextInt(); // 간선의 두 번째 정점
			edges[i][2] = input.nextInt(); // 간선의 가중치
		}

		// 크루스칼 알고리즘을 이용하여 최소신장트리 간선 목록을 구함
		int[][] mst = kruskal(n, edges, e);

		// 최소신장트리 간선 목록을 출력
		System.out.print("[");
		for (int i = 0; i < mst.length; i++) {
			if (mst[i][0] != -1) {
				System.out.print("(" + mst[i][0] + "," + mst[i][1] + "," + mst[i][2] + ")");
				if (i < mst.length - 1 && mst[i + 1][0] != -1) {
					System.out.print(", ");
				}
			}
		}
		System.out.println("]");

		input.close(); // Scanner 객체 닫기
	}

	// 크루스칼 알고리즘을 이용한 최소신장트리 구하는 메소드
	public static int[][] kruskal(int n, int[][] edges, int e) {
		sortEdgesByWeight(edges, e); // 간선 가중치 오름차순으로 정렬
		MySet disjointSet = new MySet(n); // 상호배타적 집합 생성

		int[][] mst = new int[n - 1][3]; // 최소신장트리 간선 목록
		for (int i = 0; i < n - 1; i++) {
			mst[i][0] = -1; // 초기화
		}

		int edgeCount = 0; // 최소신장트리에 포함된 간선 수
		for (int i = 0; i < e && edgeCount < n - 1; i++) {
			int v1 = edges[i][0]; // 현재 간선의 첫 번째 정점
			int v2 = edges[i][1]; // 현재 간선의 두 번째 정점
			int weight = edges[i][2]; // 현재 간선의 가중치
			int root1 = disjointSet.findSet(v1); // 첫 번째 정점의 대표 원소 찾기
			int root2 = disjointSet.findSet(v2); // 두 번째 정점의 대표 원소 찾기

			if (root1 != root2) { // 두 정점이 다른 집합에 속하면, 최소신장트리 간선 목록에 추가
				mst[edgeCount][0] = v1;
				mst[edgeCount][1] = v2;
				mst[edgeCount][2] = weight;
				edgeCount++;
				disjointSet.union(root1, root2); // 두 집합을 합침
			}
		}

		return mst; // 최소신장트리 간선 목록 반환
	}

	// 간선을 가중치 오름차순으로 정렬하는 메소드
	public static void sortEdgesByWeight(int[][] edges, int e) {
		for (int i = 0; i < e - 1; i++) {
			for (int j = 0; j < e - 1 - i; j++) {
				if (edges[j][2] > edges[j + 1][2]) { // 앞의 간선 가중치가 더 크면, 간선 교환
					int[] temp = edges[j];
					edges[j] = edges[j + 1];
					edges[j + 1] = temp;
				}
			}
		}
	}

	// 상호배타적 집합을 구현하는 클래스
	public static class MySet {
		private int[] parent; // 각 원소의 부모를 저장하는 배열
		private int[] rank; // 각 원소의 랭크를 저장하는 배열

		// 생성자: 원소 수 n을 매개변수로 받아 집합 객체를 초기화
		public MySet(int n) {
			parent = new int[n];
			rank = new int[n];
			for (int i = 0; i < n; i++) {
				makeSet(i); // 각 원소에 대해 makeSet 연산 수행
			}
		}

		// makeSet 연산: x 하나로 이루어진 집합을 만듦
		public void makeSet(int x) {
			parent[x] = x; // 각 원소의 부모를 자기 자신으로 설정
			rank[x] = 0; // 초기 랭크를 0으로 설정
		}

		// findSet 연산: x의 대표 원소를 찾되 경로압축 사용
		public int findSet(int x) {
			if (x != parent[x]) {
				parent[x] = findSet(parent[x]); // 경로 압축을 통해 x의 부모를 최상위 대표로 설정
			}
			return parent[x];
		}

		// union 연산: x와 y가 속한 집합을 합치되, 랭크를 고려하여 합침
		public void union(int x, int y) {
			int rootX = findSet(x); // x의 대표 원소 찾기
			int rootY = findSet(y); // y의 대표 원소 찾기

			if (rootX != rootY) { // 두 대표 원소가 다를 때만 합침
				if (rank[rootX] > rank[rootY]) { // x의 랭크가 더 크면
					parent[rootY] = rootX; // y의 대표를 x의 대표로 설정
				} else if (rank[rootX] < rank[rootY]) { // y의 랭크가 더 크면
					parent[rootX] = rootY; // x의 대표를 y의 대표로 설정
				} else { // 랭크가 같으면
					parent[rootY] = rootX; // y의 대표를 x의 대표로 설정
					rank[rootX]++; // x의 랭크 증가
				}
			}
		}
	}
}