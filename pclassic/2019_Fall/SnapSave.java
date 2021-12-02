public class SnapSave{

    public static void main(String[] args) {
        System.out.println( findPeak( new int[] {20, 10, 35}));
        System.out.println( findPeak( new int[] {13, 52, 75, -8, 27}));
    }

    public static int findPeak( int[] peaks){
        int distance = 0;
        int currentHighest = peaks[ distance ];
        while( currentHighest < peaks[distance + 1]){
            distance++;
            currentHighest = peaks[distance];
        }
        return distance;
    }
}