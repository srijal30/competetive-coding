import java.io.*;
import java.util.*;



public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );

        String[] ints = br.readLine().split("\\s+");

        System.out.println(  Integer.parseInt(ints[0]) + Integer.parseInt(ints[1]) );      

    }
}