import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import static java.lang.Integer.*;

public class Main {
    public static boolean isAdjacent(char start, char dest){
        String n1 = "" + start;
        String n2 = "" + dest;
        if (n1.compareTo("A") == 0){
            if (n2.compareTo("B") == 0 || n2.compareTo("D") == 0) return true;
          } else if (n1.compareTo("B") == 0){
            if (n2.compareTo("A") == 0 || n2.compareTo("C") == 0) return true;
          } else if (n1.compareTo("C") == 0){
            if (n2.compareTo("B") == 0 || n2.compareTo("D") == 0) return true;
          } else if (n1.compareTo("D") == 0){
            if (n2.compareTo("A") == 0 || n2.compareTo("C") == 0) return true;
          }
          return false;
    }

    public static int time(int n, int k, String[] order, int[] duration, char start, char dest, int curPortal, int timeNext){
        //REMEMBER TO DO START TIME FACTORING
        if(curPortal >= n) return -1;
        timeNext = duration[curPortal] - timeNext;
        int travelTime = 0;
        boolean isAdj = isAdjacent(start, dest);
        //if we are at destination
        if(isAdj && order[curPortal].charAt(0) == dest){
            return 0;
        }
        if(isAdj){
            while(curPortal < n  && order[curPortal].charAt(0) != dest){
                curPortal++;
                if(curPortal >= n) return -1;
                travelTime += timeNext;
                timeNext = duration[curPortal];
            }
        }
        else{
            boolean adjFound = false; 
            while(curPortal < n && !adjFound || order[curPortal].charAt(0) != dest){
                curPortal++;
                if(curPortal >= n) return -1;
                travelTime += timeNext;
                timeNext = duration[curPortal];
            }
        }
        return travelTime;
    }

    public static int[] evacuate(int n, int k, String[] order, int[] duration, List<String[]> sfx){
        int[] result = new int[sfx.size()];
        int ctr = 0;
        //for every person
        for(String[] person: sfx){
            //prelim
            char start = person[0].charAt(0);
            char dest = person[1].charAt(0);
            //get the time right
            int startTime = Integer.parseInt(person[2]);
            int curPortal = 0;
            //get to the current open portal for person
            while(curPortal < n && startTime - duration[curPortal] >= 0){
                startTime -= duration[curPortal];
                curPortal++;
            }
            //add to array
            result[ctr++] = time(n, k, order, duration, start, dest, curPortal, startTime);
            //debug
            //System.out.println(start + " " + dest + " " + curPortal + " " + startTime);
        }
        return result;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(reader.readLine());
            int k = Integer.parseInt(reader.readLine());
            String[] order = reader.readLine().split(" ");
            String[] temp = reader.readLine().split(" ");
            int[] duration = new int[n];
            for (int j = 0; j < n; j++) {
                duration[j] = parseInt(temp[j]);
            }
            List<String[]> sfx = new ArrayList<>();
            for (int x = 0; x < k; x++) {
                sfx.add(reader.readLine().split(" "));
            }
            int[] output = evacuate(n, k, order, duration, sfx);
            System.out.println(Arrays.toString(output));
        }
    }
}