import java.util.*;
import java.io.*;

public class Question5 {

    public static int unbeatable(int[] vibrant, int[] confidence){
        int maxV = vibrant[0];
        int cutoffC = confidence[0];
        int maxC = confidence[0];
        int cutoffV = vibrant[0];

        for(int i = 1; i < vibrant.length; i++){
            if( vibrant[i] > maxV){
                maxV = vibrant[i];
            }
            else if( vibrant[i] == maxV){
                cutoffC = Math.max( cutoffC, confidence[i] );
            }
            if( confidence[i] > maxC){
                maxC = confidence[i];
            }
            else if( confidence[i] == maxC){
                cutoffV = Math.max( cutoffV, vibrant[i] );
            }
        }

        int count = 0;
        for( int i = 0; i < vibrant.length; i++){
            int currentV = vibrant[i];
            int currentC = confidence[i];

            if( currentV == cutoffV && currentC == maxC){
                count ++;

            }
            else if( currentC == cutoffC && currentV == maxV){
                count ++;
        }

    }
    return count;
}


    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for(int i = 0; i < times; i++){
            

            ArrayList<Integer> vibrance = new ArrayList<Integer>();
            ArrayList<Integer> confidence = new ArrayList<Integer>();

            String line = br.readLine();
            while( !line.equals("") ){
                StringTokenizer st = new StringTokenizer( line );

                vibrance.add( Integer.parseInt(st.nextToken()) );
                confidence.add( Integer.parseInt(st.nextToken()) );

                line = br.readLine();
            } 

            int[] vib = new int[vibrance.size()];
            int[] con = new int[confidence.size()];

            for(int x = 0; x < vib.length; x++){
                vib[x] = vibrance.get(x);
                con[x] = confidence.get(x); 
            }
            System.out.println( unbeatable(vib, con) );

        }
        
    }

    
}
