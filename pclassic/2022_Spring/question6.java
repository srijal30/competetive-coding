import java.util.*;
import java.io.*;

public class question6 {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int times = sc.nextInt();
        
        for (int i = 0; i < times; i++) {
            Graph g = new Graph();
            int n = sc.nextInt();
            for (int j = 0; j < n; j++) {
                g.addNode(j);
            }
            boolean ok = true;
            HashSet<Integer> connected = new HashSet<>();
            int numPref = sc.nextInt();
            for (int j = 0; j < numPref; j++) {
                int temp1 = sc.nextInt();
                int temp2 = sc.nextInt();
                if (connected.contains(temp2)) {
                    ok = false;
                }
                g.addEdge(temp1, temp2);
                connected.add(temp2);
            }
            
            for (int j = 0; j < n; j++) {
                if (g.getEdge(j).size() != 2 || g.getEdge(j).size() != 0) {
                   ok = false;
                }
                for (int k : g.getEdge(j)) {
                    if (g.getEdge(k).contains(j)) {
                       ok = false;
                    }
                }
            }

            if (!ok) {
                System.out.println(-1);
            }

            if (ok) {
                for(int j = 0; j < n; j++) {
                    HashSet<Integer> visited = new HashSet<>();
                    ArrayList<Integer> path = new ArrayList<>();
                    g.dfs(0, visited, path);
                    if (visited.size() == n) {
                        for (int k : path) {
                            System.out.println(k);
                        }
                    }
                }
            }
        }
    }

    static class Graph{
      HashMap<Integer, ArrayList<Integer>> adj;

        public Graph() {
            adj = new HashMap<Integer, ArrayList<Integer>>();
        }

        public void addNode(int v) {
            adj.putIfAbsent(v, new ArrayList<>());
        }

        public void addEdge(int v1, int v2) {
            adj.get(v1).add(v2);
        }

        public List<Integer> getEdge(int v) {
            return adj.get(v);
        }
        public void dfs(int v, HashSet visited, ArrayList path) {
          if (visited.contains(v))
              return;
          path.add(v);
          visited.add(v);
          for (int i : adj.get(v)) {
              if (!visited.contains(i))
                  dfs(i, visited, path);
        }
    }
    }
}
