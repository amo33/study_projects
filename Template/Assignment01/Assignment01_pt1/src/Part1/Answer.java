package Part1;

public class Answer {
	
	private String solution; // ������ ���� ��
	
	public Answer() // ��� ������ ��None������ �ʱ�ȭ�ϴ� �⺻ ������
	{ 
		this.solution = "None";
	}
	
	public Answer(String solution) // ��� ������ ���ڷ� ���� ������ �����ϴ� ������
	{ 
		this.solution = solution;
	}

	public String getSolution() 
	{
		return this.solution;
	}

	public void setSolution(String solution) 
	{
		this.solution = solution;
	}
	
	public boolean equals(Answer answer) // ���ڷ� ���� ��ü�� �������� ������ Ȯ���ϴ� �޼ҵ�
	{
		return this.solution.equals(answer.solution);
	}
	
	public String toString() // solution�� ���� ����ϴ� toString() �޼ҵ带 �������̵�
	{ 
		return ("Solution: " + this.solution);
	}
	
}
