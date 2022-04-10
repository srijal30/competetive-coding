import java.util.*;
import java.io.*;

/*
Exception in thread "main" java.util.InputMismatchException
	at java.util.Scanner.throwFor(Scanner.java:864)
	at java.util.Scanner.next(Scanner.java:1485)
	at java.util.Scanner.nextInt(Scanner.java:2117)
	at java.util.Scanner.nextInt(Scanner.java:2076)
	at Main.main(Main.java:11)
*/

public class question2 {

    public static void main(String[] args) throws IOException{
    
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );

        //get amount of test cases
        int times = Integer.parseInt( br.readLine() );
        //loop through each test case
        for( int i = 0; i < times; i++){
            String next = br.readLine();
            String[] array = next.split(" ");

            HashMap<String, String> map = new HashMap<String, String>();

            

            // System.out.println(Arrays.toString(array));
            int mappingCount = Integer.parseInt(br.readLine());

            for(int x = 0; x < mappingCount; x++){
                String[] pair = br.readLine().split(" ");
                if (pair.length == 2){
                    map.put( pair[0], pair[1] );
                }
            }
            
            int index = 0;

            for( String current: array ){
                if( map.containsKey(current)  ){
                    System.out.print( map.get(current) );
                }
                else{
                    System.out.print( current );
                }
                if( ! (index>= array.length-1) ){
                    System.out.print(" ");
                }
            }
        
    }
}
}