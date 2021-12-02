import java.util.*;
import java.io.*;

public class Question8 {

    public static int maxGame( String polly, String paul, int pol, int pau){
        //check if game over
        if( pol == polly.length() || pau == polly.length() ){
            return (Math.max(pol, pau)-Math.min(pol, pau))*-2;
        }

        //see if match
        int match;
        if( polly.charAt(pol) == paul.charAt(pau) ){
            match = 1;
        }
        else{
            match = -1;
        }
        
        //Reductions
        int noSkip = maxGame(polly, paul, pol+1, pau+1) + match;
        int skipPolly = maxGame(polly, paul, pol, pau+1) - 2;
        int skipPaul = maxGame(polly, paul, pol+1, pau) - 2;

        return Math.max( noSkip, Math.max(skipPolly, skipPaul) );
    }


    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for(int i = 0; i < times; i++){

            String polly = br.readLine();
            String paul = br.readLine();

            System.out.println( maxGame(polly, paul, 0, 0) );
        }
    }

    
}
