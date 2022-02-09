package Part2;

public class GradeList { // GradeNode 객체로 연결리스트를 생성할 클래스

	GradeNode head; // 연결리스트의 첫 노드

	public GradeList() // 기본 생성자는 head 노드를 null로 초기화
	{
		head = new GradeNode();
	}

	public GradeList(GradeList gradeList) // 인자로 받은 gradeList 연결리스트를 복사하는 Copy Constructor 생성자
	{

		if (gradeList == null) // 인자로 받은 연결리스트가 존재하지 않을 경우
		{
			System.out.println("Nothing to copy");
			return;
		}

		/* 현재 GradeList의 head 객체가 없을 경우 head에 인자로 받은 gradeList의 head를 복사 */
		if(this.head == null){

		}
		/* 인자로 받은 gradeList 연결리스트를 복사 (각 노드의 변수들을 전부 복사, 참조 복사 X) */


	}

	public void addNode(Assignment assignment, Answer answer, String score) // 인자로 받은 변수 및 객체들로 생성한 노드를 연결리스트에 추가하는 메소드
	{

		/* 현재 GradeList의 head 객체가 없을 경우 인자로 받은 변수 및 객체들로 노드 생성 */
		GradeNode tempNode = new GradeNode(assignment, answer, score);
		GradeNode tempsearch = this.head;
		if(this.head == null){
			this.head.nextNode = tempNode;
			return;
		}
		/* 현재 노드의 다음 노드가 null이 아닐 때까지 현재 노드를 옮긴 후 마지막 노드의 다음 노드에 노드 삽입 및 객체 생성 */
		while(tempsearch.nextNode != null){
			tempsearch = tempsearch.nextNode;
		}
		tempsearch.nextNode = tempNode;
		tempNode.nextNode = null;
	}

	public void printList() // 연결리스트 출력 메소드
	{

		/* 리스트의 첫 노드부터 toString 메소드를 호출하여 출력 */
		if(this.head== null){
			System.out.println("No input");
			return;
		}
		GradeNode tempNode = this.head.nextNode;
		while(tempNode != null){
			System.out.println(tempNode.assignment);
			System.out.println(tempNode.answer);
			System.out.println(tempNode.getScore());
			tempNode = tempNode.nextNode;
		}

	}

}