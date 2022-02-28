/*import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class DragRacing {

    public static int[][] findSmallestD( int[][] tracks){

        int[][] result = new int[tracks.length][2];


    }
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );

        int times = Integer.parseInt( br.readLine() );

        for( int i = 0; i < times; i++){

            int tracksCount = Integer.parseInt( br.readLine() );
            int[][] tracks = new int[tracksCount][2];
            

            //Loop through adding on to tracks list and finding largest x and y
            int maxXDir = Integer.parseInt( st.nextToken() );
            int maxYDir = Integer.parseInt( st.nextToken() );

            int minXDir = maxXDir;
            int minYdir = maxYDir;

            tracks[0][0] = maxXDir;
            tracks[0][1] = maxYDir;

            for( int x = 1; x < tracksCount; x++){

                StringTokenizer st = new StringTokenizer( br.readLine() );

                int xDir = Integer.parseInt( st.nextToken() );
                int yDir = Integer.parseInt( st.nextToken() );

                maxXDir = Math.max( maxXDir, xDir);
                maxYDir = Math.max( maxYDir, yDir);
                
                minXDir = Math.min

                tracks[x][0] = xDir ;
                tracks[x][1] = yDir;

            }

            //Creation of the Plane
            int[][] plane = new int[][]

            System.out.println( Arrays.deepToString( tracks) );


        }

    }
}
*/