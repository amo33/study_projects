package selfTest;
import java.util.Scanner;
public class TestScores {
	public static final int MAX_NUMBER_SCORES = 10;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		double[] scores = new double[MAX_NUMBER_SCORES];
		int counting = 0;
		
		System.out.println("This program reads test scores and shows");
		System.out.println("how much each differs from the average.");
		System.out.println("Enter test scores:");
		
		counting = fillArray(scores);
		showDifference(scores, counting);
		
	}

	public static int fillArray(double [] grades)
	{
		System.out.println("Mark the end of the list with a negative number.");	
		int cnt = 0;
		Scanner keyboard = new Scanner(System.in);
		double score = 0;
		score = keyboard.nextDouble();
		while(score > 0 && cnt <= MAX_NUMBER_SCORES) {
			grades[cnt] = score;
			cnt ++;
			score = keyboard.nextDouble();
		
		}
			
		
		return cnt;
	}
	
	public static void showDifference(double [] grades, int cnt)
	{
		double average = computeAverage(grades, cnt);
		
		System.out.println("Average of the scores = " + average);
		System.out.println("The scores are: ");
		
		for(int i = 0; i<cnt; i++) {
			System.out.printf("%.1f differs from average by %.2f\n", grades[i], grades[i] - average);
		}
		
	}
	
	public static double computeAverage(double[] grades, int count)
	{	
		double Average = 0;
		for(int i = 0; i< count; i++) {
			Average +=grades[i];
		}
		if(count >0) {
			return Average /= count;
		}
		else {
			return 0;
		}
		
	}
}
