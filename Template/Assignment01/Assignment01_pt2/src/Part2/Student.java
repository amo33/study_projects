package Part2;


public class Student {
	
	private String studentName; // �л� �̸�
	private int studentId; // �й�


	public Student(){}

	public Student(String studentName, int studentId) // ��� ������ ���ڷ� ���� ������ �ʱ�ȭ�ϴ� ������
	{
		this.studentId = studentId;
		this.studentName = studentName;
	}

	public String getStudentName()
	{
		return this.studentName;
	}

	public void setStudentName(String studentName)
	{
		this.studentName = studentName;
	}

	public int getStudentId()
	{
		return this.studentId;
	}


	public void setStudentId(int studentId)
	{
		this.studentId = studentId;
	}

	public Answer makeAnswer(Assignment assignment, String solution) // ���ڷ� ���� Assignment ��ü�� solution�� �� �� solution�� ���� ����Ͽ� ������ Answer ��ü�� �����ϴ� �޼ҵ�
	{
		return new Answer(solution);
	}

	public String toString() //  studentName, studentId�� ���� ����ϴ� toString() �޼ҵ带 �������̵�
	{
		return ("StudentName: "+ this.studentName + ", StudentId: " + this.studentId);
	}

}
