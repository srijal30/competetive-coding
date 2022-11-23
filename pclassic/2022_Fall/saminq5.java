import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import static java.lang.Integer.*;

public class Main {
    public static int[] evacuate(int n, int k, String[] order, int[] duration, List<String[]> sfx){
      ArrayList<String> letters = new ArrayList<String>();
      for (int i = 0; i < order.length; i++){
        for (int j = 0; j < duration[i]; j++){
          letters.add(order[i]);
        }
      }

      int elapsed_times[] = new int[k];
      
      boolean entered = false;

      for (int i = 0; i < k; i++){
        String start = sfx.get(i)[0];
        String end = sfx.get(i)[1];
        int start_time = Integer.parseInt(sfx.get(i)[2]);

        if (start_time >= letters.size()){
          elapsed_times[i] = -1;
          entered = true;
          break;
        } else if (letters.get(start_time).compareTo(start) == 0 || bool(letters.get(start_time), start)){
          for (int j = start_time; j < letters.size(); j++){
            boolean temp = false;
            if (j == 0) temp = true;
            if (letters.get(j).compareTo(end) == 0 && (temp || bool(letters.get(j-1), letters.get(j))) ){
              elapsed_times[i] = j-start_time;
              entered = true;
              break;
            }
          }
        }
        if (entered == false) elapsed_times[i] = -1;
      }
      return elapsed_times;
    }

    public static boolean bool(String n1, String n2){
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

    public static void main(String[] args) throws Exception {
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
            for (int outputStr : output) {
                System.out.println(outputStr);
            }
        }
    }
}