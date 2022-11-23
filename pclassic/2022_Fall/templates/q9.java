import java.io.*;

public class Q9 {
    static long passcode(int[] arr, int k) {
        return 0;
    }

    public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.valueOf(reader.readLine()); //number of test cases
		
		for (int i = 0; i < t; i++) {
            
            String s1 = reader.readLine(); // read array
            String[] str1 = s1.split(" ");
            int length = Integer.valueOf(str1[0]);
            int k = Integer.valueOf(str1[1]);

            int[] arr = new int[length];
            String input = reader.readLine(); // read array
            String[] str = input.split(" ");
            for (int a = 0; a < length; a++) {
                arr[a] = Integer.valueOf(str[a]);
            }
            System.out.println(passcode(arr, k));
		}
	}
}
