package selfTest;

public class DateFirstTryDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		DateFirstTry date1 = new DateFirstTry();
		DateFirstTry date2 = new DateFirstTry();
		
		date1.month = "March";
		date1.day = 25;
		date2.month = "November";
		date2.day = 17;
		
		date2.makeItNewYears();
		
		System.out.println("date1: " + date1.yellIfNewYear());
		System.out.println("date2: " + date2.yellIfNewYear());
		
	}

}
