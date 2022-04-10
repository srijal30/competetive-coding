import java.util.*;
import java.io.*;

public class question4b {
    public static void main(String[] args) throws IOException{
    
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );
        StringTokenizer st;

        //get amount of test cases
        int times = Integer.parseInt( br.readLine() );

        //loop through each test case
        for( int i = 0; i < times; i++){
            //legnth of trail
            int trail = Integer.parseInt( br.readLine() );
            //elevations list
            int[] elevations = new int[trail];
            //create the list of elevations
            st = new StringTokenizer( br.readLine() );
            int index = 0;
            while( st.hasMoreTokens() ){
                elevations[index] = Integer.parseInt( st.nextToken() );
                index++;
            }

            int bestDistance = 0;
            for( int current = 0; current < trail; current++){
                
                int currentDistance = 0;
                boolean decreasing = false;
                boolean hasDecreased = false;
                boolean hasIncreased = false;

                while( current + currentDistance + 1 < trail ){
                    //if increasing
                    if( !decreasing ){
                        //if next is higher, than increment by 1
                        if( elevations[current+currentDistance] < elevations[current+currentDistance + 1] ){
                            currentDistance++;
                            hasIncreased = true;
                        } 
                        //else start decreasing
                        else {
                            decreasing = true;
                        }
                    }
                    //if decreasing
                    else{
                        //if next is lower, than increment by 1
                        if( elevations[current+currentDistance] > elevations[current+currentDistance+1] ){
                            currentDistance++;
                            hasDecreased = true;
                        }
                        //if not, then 
                        else{
                            break;
                        }
                    }
                }
                //System.out.println(  hasDecreased );
                //System.out.println(  hasIncreased );
                //System.out.println( "for index: " + current + " the distance was " + currentDistance );
                //if hasnt decreased then dont bother
                if( !hasDecreased || !hasIncreased ){
                    continue;
                }
                //else change bestDistance
                if(currentDistance > bestDistance) bestDistance = currentDistance;
               
                //else bestDistance = bestDistance;
                //bestDistance = Math.max( currentDistance, bestDistance );
            }
             if(bestDistance > 0) {
                    bestDistance++;
            }
            System.out.println(bestDistance);
        }
    }

}