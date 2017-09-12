public class Wow { 
	public static void main(String [] args) { 
		int n = 10;
		int i = 1;
		while (i <= n) {// for (int i = 1; i <= n; i++)
			int j = 1;
			while (j <= n - i) {
				System.out.print(" ");
				j++;
			}
			j = 1;
			while (j <= n) {
				System.out.print("*");
				j++;
			}
			System.out.println();
			i++;
		}
	}
}