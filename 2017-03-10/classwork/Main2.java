import java.util.Arrays;
import java.util.Scanner;


public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] array = new int[n];
        for (int i = 0; i < n; i += 1) {
            array[i] = sc.nextInt();
        }
        int s = 0;
        /*
        for (int i = 0; i < n; i += 1) {
            s += array[i];
        }
        */
        for (int x : array) { // для любого х
            s += x;
        }
        System.out.println(s);

    }
}
