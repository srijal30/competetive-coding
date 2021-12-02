import java.util.*;
import java.io.*;


public class Question4{

    public static int subMin(int length, int ones){

        int zeroes = length - ones;
        int maxSubstrings = ones+1;

        int minGroup = zeroes/maxSubstrings;

        int oddGroups = zeroes%maxSubstrings;
        int groups = maxSubstrings - oddGroups;

        int groupSum = (minGroup+1)*minGroup/2;
        int oddGroupSum = groupSum+minGroup+1;

        return oddGroupSum*oddGroups + groupSum*groups;


    }


    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for( int i = 0; i < times; i++){
            StringTokenizer st = new StringTokenizer( br.readLine() );
            int length = Integer.parseInt( st.nextToken() );
            int ones = Integer.parseInt( st.nextToken() );

            System.out.println( subMin(length, ones) );
            
        }




    }


}