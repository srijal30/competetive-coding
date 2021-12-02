import java.util.*;

import javax.security.auth.login.CredentialException;

import java.io.*;


public class Question3{

    public static String desiredB;
    public static String desiredW;

    public static int largestSubstring( String str) {

        int maxLen = 1;
        int maxLenIndex = 0;

        int currentLen = 1;
        int currentLenIndex = 0;

        for( int i =1; i < str.length(); i++){

            if( str.charAt(i) == str.charAt(i-1) ){
                currentLen++;
            }
            else{
                if( currentLen > maxLen ){
                    maxLen = currentLen;
                    maxLenIndex = currentLenIndex;
                }
                
                currentLen = 1;
                currentLenIndex = i;
            }
        }

        return maxLenIndex;
    }


    public static int magicPlank( String planks ){

        if( planks.equals(desiredB) || planks.equals(desiredW) ){
            return 0;
        }

        int index = largestSubstring( planks );
        char currentchar = planks.charAt(index);
        char turnedchar;

        if( currentchar == 'B'){
            turnedchar = 'W';
        }
        else{
            turnedchar = 'B';
        }

        String reduction = planks.substring(0, index);

        while( planks.charAt(index) == currentchar ){
            reduction += turnedchar;
            index++;
        }

        reduction += planks.substring(index);
        System.out.println(reduction);
        return magicPlank( reduction ) + 1;

    }



    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for( int i = 0; i < times; i++){
            
            int length = Integer.parseInt( br.readLine() );
            String planks = br.readLine();

            desiredB = "B";
            desiredW = "W";

            for( int x = 0; x < length-1; x++){
                desiredB += "B";
                desiredW += "W";
            }

            System.out.println( magicPlank( planks ) );
        }




    }


}