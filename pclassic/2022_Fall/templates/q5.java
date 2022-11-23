import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import static java.lang.Integer.*;

public class Main {
    public static int[] evacuate(int n, int k, String[] order, int[] duration, List<String[]> sfx) {
        return new int[0];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(reader.readLine());
            int k = Integer.parseInt(reader.readLine());
            String[] order = reader.readLine().split(" ");
            String[] temp = reader.readLine().split(" ");
            int[] duration = new int[n];
            for (int j = 0; j < n; j++) {
                duration[j] = parseInt(temp[j]);
            }
            List<String[]> sfx = new ArrayList<>();
            for (int x = 0; x < k; x++) {
                sfx.add(reader.readLine().split(" "));
            }
            int[] output = evacuate(n, k, order, duration, sfx);
            for (int outputStr : output) {
                System.out.println(outputStr);
            }
        }
    }
}