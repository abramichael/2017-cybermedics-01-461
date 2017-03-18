/**
 * Created by ma on 22.02.2017.
 */
public class Task2 {
    public static double exp(double x) {
        double a = 1.0;
        double s = a;
        double eps = 0.000000001;
        int n = 1;
        while (Math.abs(a) > eps) {
            a = x * a / n;
            s += a;
            n += 1;
        }
        return s;
    }

    public static double ln(double x) {
        double a = x;
        double s = a;
        double eps = 0.000000001;
        int k = -1;
        double d = x;
        int n = 2;
        while (Math.abs(a) > eps) {
            a = k * d / n;
            s += a;
            n += 1;
            k *= -1;
            d *= x;
        }
        return s;
    }
    public static double pow(double x, double y) {
        return exp(y * ln(x));
    }

    public static void main(String[] args) {
        double  x = 0.5;
        long l1 = System.nanoTime();
        double y = x;
        long l2 = System.nanoTime();
        double y2 = pow(x, 2);
        long l3 = System.nanoTime();
        System.out.println(l2 - l1);
        System.out.println(l3 - l2);
    }
}
