import java.io.*;

// Problem 5
public class Magic {
    
    static int findTriples(int[] levels){
        int cnt = 0;
        for(int i = 0; i < levels.length; i++){
            for(int j = 0; j < levels.length; j++)
                if(levels[j] > levels[i])
                    for(int n = 0; n < levels.length; n++)
                        if(levels[n] > levels[j]) cnt++;
        }
        return cnt % 1000000007;
    }
    
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int times = Integer.parseInt(br.readLine());

        for(int i = 0; i < times; i++){
            //get input
            int amount = Integer.parseInt(br.readLine());
            int[] levels = new int[amount];
            for(int j = 0; j < amount; j++) levels[j] = Integer.parseInt(br.readLine());
            //do problem
            int ans = findTriples(levels);
            //print output
            System.out.println(ans);
        }
    }
}