package Part1;

public class Professor { 
	
	private enum SCORE { AA, A, A0, B, B0, C, C0, D, D0, F}
	// 과제 점수

	public Assignment makeAssignment(String subject, String question) // subject, question의 값을 인자로 받아서 Assignment 클래스의 객체를 리턴하는 메소드 
	{
		return new Assignment(subject, question);
	}
	
	public String grading(Assignment assignment, Answer answer) // 0과 10사이의 난수를 통해 받아온 랜덤 SCORE 변수 값을 리턴하는 메소드 (인자로 Assignment 객체와 Answer 객체를 받지만 사용은 하지 않음)
	{ 

		double temp = (10 * Math.random());
		SCORE [] Stemp = SCORE.values();
		int temp2 = (int)Math.floor(temp);
		return Stemp[temp2].toString();
	}
	
}
