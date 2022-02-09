import java.util.ArrayList;
import java.util.Scanner;
public class Bank {
    private int cost;
    private String Name;
    String Receiver;
    String Word;
    boolean Account;
    Bank(String name, int cost){
        this.Name =name;
        this.cost = cost;
    }
    public static void main(String[] args){
        int flag = 1;
        String name;
        int Money;
        ArrayList<Bank> members = new ArrayList<Bank>();
        // Switch case 문으로 해보기 // 밑에 if문은 계좌생성하는 코드들임
        switch(flag) {
            case 1:
                Scanner scan = new Scanner(System.in);
                System.out.print("What's your name?:");
                name = scan.next();
                System.out.print("How much are you going to save?:");
                Money = scan.nextInt();
                Bank Person1 = new Bank(name, Money);
                if(members.contains(Person1.Name) == true){
                    System.out.println("You already have your account.");
                    return;
                }
                members.add(Person1);
                Person1.ReturnString();
            case 2:
                Scanner scan2 = new Scanner(System.in);
                System.out.print("How much are you going to save more?");
                Money = scan2.nextInt();
                System.out.print("What's your name?:");
                name = scan2.next();
                // 이름의 소유자인 통장을 불러와야해야하는 코드 구현!


        }


    }
    public void AddMoney(int amount){
        this.cost += amount;
    }
    public void ReturnString(){
        System.out.println(this.Name + " has amount of "+ this.cost);
    }
    public void Menu(){
        System.out.println("Choose an option");
        System.out.println("===================================");
        System.out.println("1. Make Account");
        System.out.println("2. Input the money");
        System.out.println("3. WithDrawal");
        System.out.println("4. Send Money");
        System.out.println("===================================");
    }

  /*  public void CheckAccount(String FindName, Arraylist<Bank> set ){
        while (set)
    }
    */
}
