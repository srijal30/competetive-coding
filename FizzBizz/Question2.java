import java.util.*;
import java.io.*;


public class Question2{

    public static boolean canReach( int x, int y, int k){

        return x%k==0  && y%k==0;
    }
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for( int i = 0; i < times; i++){

            StringTokenizer st = new StringTokenizer( br.readLine() );

            int x = Integer.parseInt( st.nextToken() );
            int y = Integer.parseInt( st.nextToken() );
            int k = Integer.parseInt( st.nextToken() );

            boolean result = canReach(x, y, k);

            if(result) System.out.println("yes");
            else System.out.println("no");

            
        }




    }


}