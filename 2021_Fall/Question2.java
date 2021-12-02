import java.util.*;
import java.io.*;

public class Question2 {

    public static String decodes(String str, int k){
        String result = "";
        k = k% 26;
        
        for( int i = 0; i < str.length(); i++){

            int ascii = (int) str.charAt(i);

            if(ascii > 122 || ascii < 97){
                result += str.charAt(i);
                continue;
            }

            else if(ascii-k > 122){
                ascii = ascii - k - 26;
            }
            else if(ascii - k < 97) {
                ascii = ascii - k + 26;
            }
            else {
                ascii = ascii - k;
            }

            result += (char)ascii;
        }

        return result;
    }



    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for( int i = 0; i < times; i++){

            String message = br.readLine();
            int k = Integer.parseInt( br.readLine() );
            
            System.out.println( decodes( message, k) );
            
        }
    }

    
}
