import java.util.*;
import java.io.*;

public class Question3 {

    public static int[] hitDetection( int[] pts, int index, int temp){
        pts[index] += temp;
        return pts;
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for(int i = 0; i < times; i++){
            StringTokenizer st = new StringTokenizer( br.readLine() );
            int[] pts = new int[ Integer.parseInt(st.nextToken()) ];
            int k = Integer.parseInt( st.nextToken() );

            for(int x = 0; x < k; x++){
                StringTokenizer sts = new StringTokenizer( br.readLine() );
                sts.nextToken();

                int index = Integer.parseInt( sts.nextToken() );
                int temp = Integer.parseInt( sts.nextToken() );

                pts = hitDetection(pts, index, temp);
            }

            int count = 0;
            for(int num: pts){
                if(num==0){
                    count++;
                }
            }
            System.out.println(count);
        }

    }

    
}
