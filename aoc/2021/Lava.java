import java.io.*;
import java.util.*;

public class Lava{

    // precondition: current coord is not already apart of basin
    // function: returns size of basin for current
    // postconditin: all coords apart of basin will become 9 to not allow other things

    public static int basinSize( int[][] map, int row, int col){

        if( row < 0 || row > 99){
            return 0;
        }
        if( col < 0 || col > 99){
            return 0;
        }
        if( map[row][col] == 9 ){
            return 0;
        }
        
        map[row][col] = 9;

        return 1 + basinSize(map, row+1, col) + basinSize(map, row, col+1) + basinSize(map, row-1, col) + basinSize(map, row, col-1) ;
    }


    public static void main(String[] args) throws IOException {

        File file = new File("day9test.txt");
        Scanner sc = new Scanner( file );

        int[][] map = new int[100][100];

        //create the map
        for( int row=0; row<100; row++){
            int col = 0;
            String nums = sc.nextLine();
            for( int i = 0; i < nums.length(); i++ ){
                if( nums.charAt(i) == '\n' ) continue;
                map[row][col++] =  Character.getNumericValue( nums.charAt(i) );
            }
        }


        ArrayList<Integer> basins = new ArrayList<Integer>();

        for( int row = 0; row < 100; row++){

            for( int col = 0; col < 100; col++){

                if (map[row][col] == 9) continue;
                basins.add( basinSize(map, row, col) ) ;

            }

        }

        Collections.sort( basins );
        System.out.println( basins );





        sc.close();
    }

}