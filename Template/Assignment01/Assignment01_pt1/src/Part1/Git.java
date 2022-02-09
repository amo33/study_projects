package Part1;

// repository 2차원 배열과 연결리스트를 생성하는 메인 메서드를 포함하는 클래스
public class Git { 
	
	private static int assignmentNum = 3; // 과제 수
	private static int studentNum = 4; // 학생 수
	private static GradeNode repository[][]; // GradeNode 객체를 담는 2차원 배열
	
	public Git() // 선언된 repository 배열 원소에 GradeNode 객체를 생성하는 생성자 
	{
		repository = new GradeNode[3][4];
		for(int i=0; i< repository.length; i++){
			for(int j=0; j< repository[i].length; j++){
				repository[i][j] = new GradeNode();
			}
		}
	}
	
	public GradeNode pushGradeNode(Assignment assignment, Answer answer, String score) // 인자로 받은 클래스와 변수로 GradeNode 객체를 생성해서 리턴하는 메소드
	{
		return new GradeNode(assignment, answer, score);
	}
	
	public static void main(String[] args) {

		Git git = new Git();
		Professor professor = new Professor();
		Student student[] = new Student[studentNum];
		Assignment assignment[] = new Assignment[assignmentNum];
		Answer answer[][] = new Answer[assignmentNum][studentNum];
		String score[][] = new String[assignmentNum][studentNum];

		String question[] = {"1 + 1 = ?", "What is Velocity?", "What is this?"};
		String subject[] = {"Mathematics", "Physics", "Philosophy"};
		String solution[][] = {{"1", "Speed", "Computer"}, {"2", "m/s", "Apple"}, {"3", "I have no idea", "Iphone"}, {"4", "Running", "Nothing"}};

		student[0] = new Student("Kevin", 2021104233);
		student[1] = new Student("Judy", 2002548215);
		student[2] = new Student("Charlie", 1997487865);
		student[3] = new Student("Puth", 15048655);

		for (int i = 0; i < repository.length; i++) {
			for (int j = 0; j < repository[i].length; j++) {
				/* makeAssignment 메소드 호출로 생성한 Assignment 객체를 assignment 배열에 삽입 */

				/* makeAnswer 메소드 호출로 생성한 Answer 객체를 answer 배열에 삽입 */

				/* grading 메소드 호출로 저장한 solution 문자열을 score 배열에 삽입 */

				/* pushGradeNode 메소드 호출로 생성한 GradeNode 객체를 repository 2차원 배열에 삽입 */

				assignment[i] = professor.makeAssignment(subject[i], question[i]);
				answer[i][j] = student[j].makeAnswer(assignment[i], solution[j][i]);
				score[i][j] = professor.grading(assignment[i], answer[i][j]);
				repository[i][j] = git.pushGradeNode(assignment[i], answer[i][j], score[i][j]);

			}
		}

		System.out.println(git.showRepository()); // repository 2차원 배열 출력
	}
	public String showRepository() { // repository 2차원 배열 출력 메소드
		String string = "\n";
		for (int i = 0; i < repository.length; i++) {
			string += "Solution: ";
			for (int j = 0; j < repository[i].length; j ++)
				string += String.format("%20s", repository[i][j].answer.getSolution());
			string += "\nScore:    ";
			for (int j = 0; j < repository[i].length; j++)
				string += String.format("%20s", repository[i][j].getScore());
			string += "\n\n";
		}
		return string;
	}
}
