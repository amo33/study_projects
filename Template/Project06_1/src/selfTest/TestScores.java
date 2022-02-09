package selfTest;

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

	public static int fillArray(/* your code */)
	{
		System.out.println("Mark the end of the list with a negative number.");	
		/* your code */
	}
	
	public static void showDifference(/* your code */)
	{
		double average = computeAverage(/* your code */);
		
		System.out.println("Average of the scores = " + average);
		System.out.println("The scores are: ");
		
		/* your code */
	}
	
	public static double computeAverage(/* your code */)
	{	
		/* your code */
	}
}
