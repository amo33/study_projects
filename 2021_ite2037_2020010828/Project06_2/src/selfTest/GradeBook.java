package selfTest;

import java.util.Scanner;

public class GradeBook {
	private int numberOfStudents;
	private int numberOfQuizzes;
	
	private int [][] grade;
	
	private double[] studentAverage;
	private double[] quizAverage;

	public GradeBook()
	{
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Enter the number of Students:");
		numberOfStudents = keyboard.nextInt();
		
		System.out.println("Enter the number of Quizzes:");
		numberOfQuizzes = keyboard.nextInt();
		
		int score = 0;
		
		this.grade = new int[this.numberOfStudents][this.numberOfQuizzes];
		
		for(int i=0; i<numberOfStudents; i++) {
			for(int j=0; j< numberOfQuizzes; j++) {
				System.out.printf("Enter the score for student %d on quiz %d\n", i+1, j+1);
				score = keyboard.nextInt();
				grade[i][j] = score;
			}
		}
		
		fillStudentAverage();
		fillQuizAverage();
		
	}
	

	
	private void fillStudentAverage()
	{	
		this.studentAverage = new double[this.numberOfStudents];
		double sum = 0;
		for(int i=0; i<this.numberOfStudents; i++) {
			sum = 0;
			for(int j=0; j< this.numberOfQuizzes; j++) {
				
				sum += grade[i][j];
				
			}
			this.studentAverage[i] = sum / this.numberOfQuizzes;
		}
	}
	
	private void fillQuizAverage()
	{
		this.quizAverage = new double[this.numberOfQuizzes];
		double sum = 0;
		for(int i=0; i<this.numberOfQuizzes; i++) {
			sum = 0;
			for(int j=0; j< this.numberOfStudents; j++) {
				
				sum += grade[j][i];
				
			}
			
			this.quizAverage[i] = sum / this.numberOfStudents;
		}
	}
	
	
	public void display()
	{
		for(int studentNumber =1; studentNumber <= numberOfStudents; studentNumber++)
		{
			System.out.print("Student " + studentNumber + " Quizzes: ");
			for(int quizNumber = 1;quizNumber <= numberOfQuizzes; quizNumber++)
				System.out.print(grade[studentNumber-1][quizNumber-1] + " ");
			System.out.println("Ave = " + studentAverage[studentNumber-1]);
		}
		
		System.out.println("Quiz average : ");
		
		for(int quizNumber = 1; quizNumber <= numberOfQuizzes;quizNumber++)
			System.out.print("Quiz "+quizNumber + " Ave = "+ quizAverage[quizNumber - 1] + " ");
		System.out.println();
	}
	
	
}