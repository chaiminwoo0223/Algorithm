package hw;

// 이진검색트리2
public class hw6_1 {

	public static void main(String[] args) {
		System.out.println("hw6_1:최민우");

		// (1) 연산에 사용할 키값 배열 초기화
		int[] addList = {13, 6, 2, 10, 1, 5, 7, 11, 4, 3, 8, 9, 3, 6, 10, 13};
		int[] searchList = {12, 3, 6, 10, 13};
		int[] removeList = {12, 3, 6, 10, 13, 2, 1, 5, 4, 7, 8, 9, 11};

		// (2) 정수 키값을 저장할 공백 이진검색트리 tree를 생성
		MyBinarySearchTree tree = new MyBinarySearchTree();

		// (3) addList에 저장된 키값들을 차례대로 트리에 삽입
		for(int i = 0; i < addList.length; i++) {
			tree.add((addList[i]));
		}

		// (4) tree를 중순위 순회하여 키값을 출력
		tree.inorder();

		// (5) searchList에 저장된 키값들을 차례대로 트리에서 검색하여 결과 출력
		for(int i = 0; i < searchList.length; i++) {
			System.out.print(tree.contains(searchList[i]) + " ");
		}
		System.out.println();

		// (6) tree의 키값 합을 구하여 출력
		System.out.println(tree.sum());

		// (7) removeList에 저장된 키값들을 차례대로 트리에서 삭제
		for(int i = 0; i < removeList.length; i++) {
			tree.remove((removeList[i]));
		}

		// (8) tree를 중순위 순회하여 키값을 출력
		tree.inorder();

		// (9) tree의 키값 합을 구하여 출력
		System.out.println(tree.sum());
	}
}

// 정수 키값을 갖는 이진검색트리를 구현하는 클래스
class MyBinarySearchTree {
	private Node root = null; // 루트 노드를 가리키는 인스턴스 변수

	// 노드의 구조를 정의하는 클래스
	private class Node {
		int key;
		Node left;
		Node right;
	}

	// 트리를 중순위 순회하는 public 메소드 - 구현 세부사항을 알지 못해도 호출할 수 있음
	public void inorder() {
		System.out.print("( ");
		inorder(root);
		System.out.println(")");
	}

	// t를 루트로 하는 트리를 중순위 순회하여 키값 출력 - 매개변수(루트노드 t)로 인해 구현 세부사항을 알아야 호출할 수 있으므로 private 메소드로 따로 두었음
	private void inorder(Node t) {
		if(t != null) {
			inorder(t.left);
			System.out.print(t.key + " ");
			inorder(t.right);
		}
	}

	// 매개변수로 받은 키값을 트리에 삽입 - 구현 세부사항을 알지 못해도 호출할 수 있음
	public void add(int key) {
		root = treeInsert(root, key);
	}

	// t를 루트로 하는 트리에 key를 삽입하고 삽입 후 루트 노드를 리턴 - 매개변수(루트노드 t)로 인해 구현 세부사항을 알아야 호출할 수 있으므로 private 메소드로 따로 두었음
	private Node treeInsert(Node t, int key) {
		if(t == null) {
			Node r = new Node();
			r.key = key;
			return r;
		}
		else if(key < t.key) {
			t.left = treeInsert(t.left, key);
			return t;
		}
		else if(key > t.key) {
			t.right = treeInsert(t.right, key);
			return t;
		}
		else {
			return t;  // 이미 존재하는 키값인 경우
		}
	}

	// 키값을 매개변수로 받아 그 키값 존재 여부를 리턴
	public boolean contains(int key) {
		Node r = root; // 트리를 root부터 시작하여, 주어진 키값과 노드의 키값을 비교
		while (r != null) {
			if (key < r.key) { // 주어진 키값이 현재 노드의 키값보다 작다면, 왼쪽 자식 노드로 이동
				r = r.left;
			} else if (key > r.key) { // 주어진 키값이 현재 노드의 키값보다 크면, 오른쪽 자식 노드로 이동
				r = r.right;
			} else {
				return true; // 키를 찾음
			}
		}
		return false; // 키를 찾지 못함
	}

	// 트리의 키값 합을 구하여 리턴
	public int sum() {
		return sum(root); // 트리의 루트에서 시작하여, 전체 트리의 키값 합을 계산하는 "진입점"
	}

	// t를 루트로 하는 트리의 키값 합을 구하여 리턴
	private int sum(Node t) {
		if (t == null) { // 현재 노드가 null이면, 0을 반환
			return 0;
		} else {
			return t.key + sum(t.left) + sum(t.right); // 현재 노드의 키값 + 왼쪽 서브 트리의 키값 합 + 오른쪽 서브 트리의 키값 합(재귀적 호출)
		}
	}

	// 매개변수로 받은 키값을 트리에서 삭제. 키값이 없으면 삭제하지 않으면 됨
	public void remove(int key) {
		Node p = null; // 삭제할 노드의 부모 노드
		Node r = root; // 현재 탐색 중인 노드
		// 삭제할 노드 탐색
		while (r != null && r.key != key) {
			p = r;
			if (key < r.key) {
				r = r.left; // // 주어진 키값이 현재 노드의 키값보다 작다면, 왼쪽 자식 노드로 이동
			} else {
				r = r.right; // 주어진 키값이 현재 노드의 키값보다 크면, 오른쪽 자식 노드로 이동
			}
		}
		// 삭제할 노드가 존재하는 경우
		if (r != null) {
			treeDelete(r, p);
		}
	}

	// 부모 노드가 p인 노드 r을 트리에서 삭제
	private void treeDelete(Node r, Node p) {
		Node replacement = deleteNode(r); // 삭제할 노드를 대체할 노드
		if (p == null) { // r이 루트 노드인 경우
			root = replacement;
		} else if (r == p.left) { // r이 왼쪽 자식 노드인 경우
			p.left = replacement;
		} else { // r이 오른쪽 자식 노드인 경우
			p.right = replacement;
		}
	}

	// 노드 r을 삭제하고 r을 대신할 노드를 리턴
	private Node deleteNode(Node r) {
		// 노드가 자식이 없는 경우
		if (r.left == null && r.right == null) {
			return null;
		} else if (r.left == null) { // 오직 오른쪽 자식 노드만 있는 경우
			return r.right;
		} else if (r.right == null) { // 오직 왼쪽 자식 노드만 있는 경우
			return r.left;
		} else { // 두 자식이 모두 있는 경우
			Node parent = r;
			Node successor = r.right; // 후계 노드
			// 후계 노드 찾기
			while (successor.left != null) {
				parent = successor;
				successor = successor.left;
			}
			// 후계 노드가 r의 바로 오른쪽 자식 노드가 아닌 경우
			if (parent != r) {
				parent.left = successor.right;
				successor.right = r.right;
			}
			successor.left = r.left; // 왼쪽 자식 노드 연결
			return successor; // 대체 노드 리턴
		}
	}
}