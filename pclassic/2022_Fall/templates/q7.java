import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class q7 {
    
    public static long timeLasted(int n, long ladders, int robberInit, int copInit, int[][] edges) {
        return -1;
    }
    
    public static void main(String args[]) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(reader.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.valueOf(reader.readLine());
            long ladders = Long.valueOf(reader.readLine());
            int robbersInit = Integer.valueOf(reader.readLine());
            int copsInit = Integer.valueOf(reader.readLine());
            int[][] edges = new int[n - 1][2];
            for (int j = 0; j < n - 1; j++) {
                String[] edge = reader.readLine().split(" ");
                edges[j][0] = Integer.valueOf(edge[0]);
                edges[j][1] = Integer.valueOf(edge[1]);
            }
            long output = timeLasted(n, ladders, robbersInit, copsInit, edges);
            System.out.println(output);
        }
    }
}