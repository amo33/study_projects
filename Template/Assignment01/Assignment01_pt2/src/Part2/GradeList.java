package Part2;

public class GradeList { // GradeNode ��ü�� ���Ḯ��Ʈ�� ������ Ŭ����

	GradeNode head; // ���Ḯ��Ʈ�� ù ���

	public GradeList() // �⺻ �����ڴ� head ��带 null�� �ʱ�ȭ
	{
		head = new GradeNode();
	}

	public GradeList(GradeList gradeList) // ���ڷ� ���� gradeList ���Ḯ��Ʈ�� �����ϴ� Copy Constructor ������
	{

		if (gradeList == null) // ���ڷ� ���� ���Ḯ��Ʈ�� �������� ���� ���
		{
			System.out.println("Nothing to copy");
			return;
		}

		/* ���� GradeList�� head ��ü�� ���� ��� head�� ���ڷ� ���� gradeList�� head�� ���� */
		if(this.head == null){

		}
		/* ���ڷ� ���� gradeList ���Ḯ��Ʈ�� ���� (�� ����� �������� ���� ����, ���� ���� X) */


	}

	public void addNode(Assignment assignment, Answer answer, String score) // ���ڷ� ���� ���� �� ��ü��� ������ ��带 ���Ḯ��Ʈ�� �߰��ϴ� �޼ҵ�
	{

		/* ���� GradeList�� head ��ü�� ���� ��� ���ڷ� ���� ���� �� ��ü��� ��� ���� */
		GradeNode tempNode = new GradeNode(assignment, answer, score);
		GradeNode tempsearch = this.head;
		if(this.head == null){
			this.head.nextNode = tempNode;
			return;
		}
		/* ���� ����� ���� ��尡 null�� �ƴ� ������ ���� ��带 �ű� �� ������ ����� ���� ��忡 ��� ���� �� ��ü ���� */
		while(tempsearch.nextNode != null){
			tempsearch = tempsearch.nextNode;
		}
		tempsearch.nextNode = tempNode;
		tempNode.nextNode = null;
	}

	public void printList() // ���Ḯ��Ʈ ��� �޼ҵ�
	{

		/* ����Ʈ�� ù ������ toString �޼ҵ带 ȣ���Ͽ� ��� */
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