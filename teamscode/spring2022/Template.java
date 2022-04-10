import java.util.*;
import java.io.*;


public class Template {
    

    public static String solve( int tries, int[][] current, int[][] finals, boolean[] positions, String steps ){
        
        if( tries == 0 ) return "";
        boolean state = true;
        for( boolean i: positions ) if( !i ) state = false;
        if( state ) return steps;
        
    

    }


    public static void UP( int[][] current ){
        for( int[] cur : current ) if( cur!= )
    }

    public static void DOWN( int[][] current ){
        
    }

    public static void LEFT( int[][] current ){
        
    }

    public static void RIGHT( int[][] current ){
        
    }




    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );

        String[] inputs = br.readLine().split("\\s"); 
        final int ROWS = Integer.parseInt( inputs[0] );
        final int COLUMNS = Integer.parseInt( inputs[1] );
        final int CHIPS = Integer.parseInt( inputs[2] );

        int[][] current = new int[CHIPS][2];
        int[][] finals = new int[CHIPS][2];

        //get the inits
        for( int i = 0; i < CHIPS; i++){
            inputs = br.readLine().split("\\s");
            current[i][0] = Integer.parseInt( inputs[0] );
            current[i][1] = Integer.parseInt( inputs[1] );
        }
        //get the outits
        for( int i = 0; i < CHIPS; i++){
            inputs = br.readLine().split("\\s");
            finals[i][0] = Integer.parseInt( inputs[0] );
            finals[i][1] = Integer.parseInt( inputs[1] );
        }

        String answer = solve( 2*ROWS*COLUMNS, current, finals, new boolean[CHIPS], "" );

        if ( answer.isEmpty() ) System.out.println(-1);
        else System.out.println(answer);

    }

}
