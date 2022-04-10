import java.util.*;
import java.io.*;
public class question7 {

    public static void main(String[] args) throws IOException{
    
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );

        //get amount of test cases
        int times = Integer.parseInt( br.readLine() );

        //loop through each test case
        for( int i = 0; i < times; i++){
            int events = Integer.parseInt(br.readLine());
            int[][] itinerary = new int[events][];
            for (int j = 0; j < events; j++){
                StringTokenizer str = new StringTokenizer(br.readLine());
                itinerary[j] = new int[]{Integer.parseInt(str.nextToken()), Integer.parseInt(str.nextToken())};
            }

            //debug print out itinerary
            String result = "itinerary is [";
            for(int j = 0; j < itinerary.length; j ++){
                result += Arrays.toString(itinerary[j]);
                if(j < itinerary.length - 1){
                    result += ", ";
                }
            }
            result += "]";
            System.out.println("itinerary is " + result);
            System.out.println(maximizeFun(itinerary));
        }
        
       

        
    }
    public static int maximizeFun(int[][] itinerary){
        System.out.println("itinierary under const.");
        return maximizeFunH(itinerary, 0, 0);
    }
    public static int maximizeFunH(int[][]itinerary, int counter, int highest){
        highest += itinerary[counter][0];
        if(counter == itinerary.length){
            return highest;
        }else{
            int s = maximizeFun(itinerary, counter += 1 + itinerary[counter][1], highest);
            int i = counter + 2 + itinerary[counter][1];
            while(i < itinerary.length){
                maximizeFun(itinerary, counter + i, highest);
                i++;
            }

        }
        return highest;
    }

}