//q1)wap to check whether a person is eligible for vote or not
import java.util.Scanner;

class VoteCheck {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        if (age >= 18) {
            System.out.println("Eligible to vote");
        } else {
            System.out.println("Not eligible");
        }
    }
}
//q2)CHECK WHETHER A NUMBER IS DIVISIBLE BY 7 OR NOT
import java.util.scanner;

class DivisibleCheck {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        if (num % 7 == 0) {
            System.out.println("Divisible by 7");
        } else {
            System.out.println("Not divisible by 7");
        }
    }
}
