package Part1;

public class Professor { 
	
	private enum SCORE { AA, A, A0, B, B0, C, C0, D, D0, F}
	// ���� ����

	public Assignment makeAssignment(String subject, String question) // subject, question�� ���� ���ڷ� �޾Ƽ� Assignment Ŭ������ ��ü�� �����ϴ� �޼ҵ� 
	{
		return new Assignment(subject, question);
	}
	
	public String grading(Assignment assignment, Answer answer) // 0�� 10������ ������ ���� �޾ƿ� ���� SCORE ���� ���� �����ϴ� �޼ҵ� (���ڷ� Assignment ��ü�� Answer ��ü�� ������ ����� ���� ����)
	{ 

		double temp = (10 * Math.random());
		SCORE [] Stemp = SCORE.values();
		int temp2 = (int)Math.floor(temp);
		return Stemp[temp2].toString();
	}
	
}
