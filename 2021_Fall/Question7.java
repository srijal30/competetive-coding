import java.util.*;
import java.io.*;

public class Question7 {

    public static boolean possible(int hoses, int initial, int finale){
        return false;
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for(int i = 0; i < times; i++){

            String input1 = br.readLine();
            String input2 = br.readLine();

            int hoses = Integer.parseInt(input1);
            int finale = Integer.parseInt(input2);

            int initial = hoses;

            for(int x = 0; x < input2.length()-input1.length(); x++){
                initial  *= 10;
            }
            
            System.out.println( finale - initial);
            
            //possible(hoses, initial, finale);
        }
    }

    
}
