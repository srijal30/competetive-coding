import java.util.*;
import java.io.*;

public class Question4 {

    public static boolean love(String front, String back){
        String[] alpha = new String[26];

        for(int i = 0; i < front.length(); i ++){
            int position =( (int)front.charAt(i) ) - 97;
            
            if( alpha[position] == null ){

                alpha[position] = "" + back.charAt(i);
            }
            else{
                if( !alpha[position].equals("" + back.charAt(i)) ){
                    return false;
                }
            }

        }

        return true;
    }



    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader( new InputStreamReader( System.in) );

        int times = Integer.parseInt( br.readLine() );

        for(int i = 0; i < times; i++){
            String front = br.readLine();
            String back = br.readLine();
            
            if( love(front, back) && love(back, front) ){
                System.out.println("yes");
            }
            else{
                System.out.println("no");
            }
        }
    }

    
}
