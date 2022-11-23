import java.io.*;
import java.util.*;
import java.util.Queue;

public class Q6 {
    static boolean pathExists(int w, int h, int[][] arr) {
        
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine()); //number of test cases

        for (int i = 0; i < t; i++) {

            String s1 = reader.readLine(); // read array
            String[] str1 = s1.split(" ");
            int w = Integer.parseInt(str1[0]);
            int h = Integer.parseInt(str1[1]);

            String s2 = reader.readLine(); // read array
            int n = Integer.parseInt(s2);

            int[][] arr = new int[n][3];
            for (int a = 0; a < n; a++) {
                String input = reader.readLine(); // read array
                String[] str = input.split(" ");
                arr[a][0] = Integer.parseInt(str[0]);
                arr[a][1] = Integer.parseInt(str[1]);
                arr[a][2] = Integer.parseInt(str[2]);
            }
            System.out.println(pathExists(w, h, arr));
        }
    }
}