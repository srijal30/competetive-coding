import java.util.*;
import java.io.*;


public class question1 {
    public static void main(String[] args) throws IOException{
    
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );

        //get amount of test cases
        int times = Integer.parseInt( br.readLine() );

        //loop through each test case
        for( int i = 0; i < times; i++){
            //input handling
            String s = br.readLine();
            
            int n = Integer.parseInt( br.readLine() );

            int[] shifts = new int[n];

            StringTokenizer st = new StringTokenizer( br.readLine() );

            int index = 0;
            while( st.hasMoreTokens() ){
                shifts[index]  = Integer.parseInt( st.nextToken() );
                index++;
            }
            String output = "";
            for(int j = 0; j < shifts.length; j++) {
            int part1;

            part1 = s.length() - shifts[j];
            // System.out.println("j is " + j);
            // System.out.println("n is " +n);
            // System.out.println("shifts[n-1] is " + shifts[n-1]);
            // System.out.println("shifts[j] is " + shifts[j]);
            // System.out.println("array s is " + Arrays.toString(shifts));
            // System.out.println("string is " + s);
            if(shifts[j] > s.length()) {
                part1 = shifts[j] % s.length();
                part1 = Math.abs(s.length() - part1);
            }

            
            //  System.out.println("part 1 is " + part1);

            String parts1 = s.substring(0,part1);
            String parts2 = s.substring(part1);
            output = parts2 + parts1;
            s = output;
            }
            System.out.println(output);
            


        }
    
      
    }

}