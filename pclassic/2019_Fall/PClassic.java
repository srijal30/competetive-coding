import java.util.*;
import java.io.*;

public class PClassic {

    public static String reverse(String str){

        String result = "";
        for(int i = str.length()-1 ; i >= 0; i--){
            result += str.charAt(i);


        }

        return result;
    
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );
        StringTokenizer st = new StringTokenizer( br.readLine() );

        String result = "";
        while( st.hasMoreTokens() ){
            result += reverse(st.nextToken()) + " ";
        }
        result = result.substring(0, result.length()-1);
        System.out.println(result);


        
    }




}
