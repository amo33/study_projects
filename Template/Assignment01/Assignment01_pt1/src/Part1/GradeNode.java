package Part1;

public class GradeNode { 
	
	Assignment assignment; // ����
	Answer answer; // ������ ���� ��
	private String score; // ����
	
	public GradeNode() // ��� ������ null�� �ʱ�ȭ�ϴ� �⺻ ������
	{ 
		this.answer = null;
		this.assignment = null;
		this.score = null;
	}
	
	public GradeNode(Assignment assignment, Answer answer, String score) // nextNode�� ������ ��� ������ ���ڷ� ���� ������ �����ϴ� ������ (��, ���ڷ� ��ü�� ������ �� ��ü�� ��� ������ ����)
	{ 
		this.answer = new Answer(answer.getSolution());
		this.assignment = new Assignment(assignment.getSubject(), assignment.getQuestion());
		this.score = score;
	}
	
	public void setScore(String score)
	{ 
		this.score = score;
	}
	
	public String getScore() 
	{
		return this.score;
	}

	public boolean equals(GradeNode gradeNode) // ���ڷ� ���� ��ü�� �������� ������ Ȯ���ϴ� �޼ҵ�
	{
		return (this.score.equals(gradeNode.score)&& (this.answer.equals(gradeNode.answer)) && (this.assignment.equals(gradeNode.assignment)));
	}
	
	public String toString() // nextNode�� ������ ��� ������ ���� ����ϴ� toString() �޼ҵ带 �������̵� (������ ��ü�� ��� �ش� ��ü�� toString() �޼ҵ� ȣ��)
	{
		return ("Score: " + this.score + "," + this.assignment.toString() +", "+ this.answer.toString());
	}
}
