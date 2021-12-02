import java.util.*;
import java.io.*;


public class Question1{

    public static int canYouEatIt( int length, int k){

        if( length%k == 0 ){
            return length/k;
        }
        else{
            return -1; 
        }
    }





    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for( int i = 0; i < times; i++){

            StringTokenizer st = new StringTokenizer( br.readLine() );
            
            int length = Integer.parseInt( st.nextToken() );
            int k = Integer.parseInt( st.nextToken() );

            System.out.println( canYouEatIt(length, k) );
        }




    }


}