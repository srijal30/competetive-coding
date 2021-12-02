import java.util.*;
import java.io.*;

public class Question1 {

    public static String reverse(String s, int num){
        String result = s.substring(0, s.length() - num);
        for(int i = s.length()-1; i > s.length()-num-1; i--){
            result += s.charAt(i);
        }
        return result;
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for( int i = 0; i < times; i++){
            StringTokenizer st = new StringTokenizer( br.readLine() );    
            System.out.println( reverse( st.nextToken(), Integer.parseInt(st.nextToken()) ) );
        }
    }

    
}
