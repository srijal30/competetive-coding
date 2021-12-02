import java.util.*;
import java.io.*;

public class Question4 {
    
    public static String binary (int num){
        String result = "";
        while( num != 0){
            result = Integer.toString(num%2) + result;
            num /= 2;
        }

        return result;
    }

    public static int find(String num, String num2){
        num = binary( Integer.parseInt(num) );
        num2 = binary(Integer.parseInt(num2) );

        if( num.length() > num2.length()){
            int zeroes = num.length() - num2.length();
            for( int i = 0; i < zeroes; i++){
                num2 = "0" + num2;
            } 
        }
        else{
            int zeroes = num2.length() - num.length();
            for( int i = 0; i < zeroes; i++){
                num = "0" + num;
            }
        }

        int answer = 0;
        for(int i=0; i<num2.length(); i++){
            if( num.charAt(i) != num2.charAt(i) ) answer++;
        }

        return answer;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );
        StringTokenizer st = new StringTokenizer( br.readLine() );
        
        System.out.println( find(st.nextToken(), st.nextToken()) );

    }
    
}
