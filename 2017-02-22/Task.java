import java.util.Scanner;

public class Task {
    public static double pow(double x, int n) {
        double p = 1;
        int i = 0;
        while (i < n) {
            p *= x;
            i++;
        }
        return p;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x = scanner.nextDouble();
        long c1 = System.nanoTime();
        //double y = 2 * x * x * x * x - 3 * x * x * x + 4 * x * x -
        //        5 * x + 6;
        double y = (((2 * x - 3) * x + 4) * x - 5) * x + 6;
        long c2 = System.nanoTime();
        System.out.println(c2 - c1);
        System.out.println(y);
    }
}
