import java.io.*;
import java.util.*;

public class GameWithChips {










    public static void main(String[] args) throws IOException{
    
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
        StringTokenizer st = new StringTokenizer( br.readLine() );

        //Creation of Board
        int rows = Integer.parseInt( st.nextToken() );
        int columns = Integer.parseInt( st.nextToken() );
        int chipCount = Integer.parseInt( st.nextToken() ); //Store chip count

        int[][] board = new int[rows][columns];
        
        int maxActions = rows*columns*2; //Check if there is subquence that has less than this amount of moves
        

        //Option 1:
        //Loop for making board
        for( int i = 1; i <= chipCount; i++){
            //Take input
            st = new StringTokenizer( br.readLine() );
            
            //Find X and Y
            int xPos = Integer.parseInt( st.nextToken() ) - 1;
            int yPos = Integer.parseInt( st.nextToken() ) - 1;

            //Place on "board"
            board[xPos][yPos] = i;
        }

        
        
        //Loop for desired position
        



        // To Help Print the Board
        for( int[] array: board){
            System.out.println( Arrays.toString(array) );
        } 
    
    }

}
