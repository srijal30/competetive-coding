import java.io.*;
import java.util.*;

public class Two {

    static int query = 0;

    public static void cat( ArrayList<Integer> distances, int action, int parameter ){

        //last distance
        int prevD = distances.get( distances.size() - 1 );
        
        //ellis moves closer
        prevD--;
            
        if( action == 0 ){
            query = prevD;
        }
        else if ( action == 1){
            prevD -= parameter;
        }
        else if ( action == 2 ){
            prevD += parameter;
        }
        else if ( action == 3 ){
            prevD = distances[ current - parameter];
        }
        else if ( action == 4 ){

        }
        else{
            System.out.println("ERROR");
        }


    }

    public static void main(String[] args) throws IOException {
    
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in ) );
        
        String[] nums = br.readLine().split(" ");

        int times = Integer.parseInt( nums[0] );
        int distance = Integer.parseInt( nums[1] );

        ArrayList<Integer> frames = new ArrayList<Integer>();

        for( int i = 0; i < times; i++){

            //get x and y
            nums = br.readLine().split(" ");
            int x = Integer.parseInt( nums[0] );
            int y = Integer.parseInt( nums[1] );

            //decrypt
            x = x ^ query;
            y = y ^ query;



        }

    }
    
}
