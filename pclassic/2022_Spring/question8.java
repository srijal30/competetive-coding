import java.util.*;
import java.io.*;
/*
Meggie and Vatsin are enjoying their summer in the beautiful country of Vanuatu. Vanuatu is composed of mn islands, 
but a sudden earthquake caused the islands to shift their positions such that they miraculously ended up in an mn grid of islands! 
The island that Meggie and Vatsin were chilling at somehow ended up in the bottom left hand corner of the grid. 
The earthquake also made the bellies of Meggie and Vatsin quake, so they need to get some food for themselves quickly! 
The only place to get food in the country is located at the island at the top right corner of the grid of islands. 
The islands are connected by tubes such that each island is connected to the island above, below, to the left, and to the right of it 
(if such an island exists). Vatsin and Meggie are only allowed to go to the island directly north of them or directly east of them.

Furthermore, some of the islands have tickets which they can trade in for a meal at the top right island. 
If Vatsin and Meggie encounter a ticket along their path, they must collect it. 
Because Vatsin and Meggie want to both eat the same amount of meals, they want to collect an even number of tickets along the way.

As the concierge at Vanuatu island, you want to guarantee that no matter what path Vatsin and Meggie take, they end up with an even number of tickets. 
Moreover, you know that there are q plans where the ith plan involves adding di tickets to islands such that each island can have at most one ticket. 
For each of the q plans, determine whether it is possible to place the di additional tickets such that no matter what path they take from the bottom left to the top right, 
Vatsin and Meggie will collect an even number of tickets.

Implementation Details

Implement the following function. It will be called by the grader once for each test case.

tubeAdventures(n, m, q, islands, queries)

n:number of rows of islands
m: number of columns of islands
q: number of queries
islands: an array of strings where each string represents a row of islands and a character is a “.” if there is no ticket and an “x” if there is a ticket.
queries an array of integers where each element represents the number of tickets to place
Your function should return a list containing YES if it is possible to place the additional tickets, and NO if it is not possible for each query.

Input Format
The first line contains n m q The next n lines contain a string representing a row of islands The next q lines contain an int representing the number of tickets we want to place

Output Format
Output YES if there exists a valid ticket placement, and NO otherwise per query.

Constraints
0≤m∗n≤5∗104
1≤q≤105
Sample Input 1 
2 3 3
...
...
1
2
3
Sample Output 1 
NO
YES
YES
Explanation
There’s no way to place only one ticket so that Vatsin is always in front of Meggie.

For two tickets we could place them as follows:

..x

x..

For three tickets:

.x.

x.x

Sample Input 2 
3 3 5
...
..x
..x
1
2
3
4
5
Sample Output 2 
NO
NO
YES
NO
YES
Explanation
There’s no way to place only one, two, or four tickets so that Vatsin is always in front of Meggie.

For three tickets we could place them as follows:

xx.

.xx

..x

For five tickets:

xxx

.xx

x.x

Sample Input 3 
3 6 3
.x....
.x.x.x
.....x
8
9
10
Sample Output 3 
NO
NO
YES
Explanation
There’s no way to place only eight or nine tickets so that Vatsin is always in front of Meggie.

For ten tickets we could place them as follows:

xxxxx.

.xxxxx

x.xxxx
*/

public class question8 {

    public static void main(String[] args) throws IOException{
    
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );

        //get amount of test cases
        int times = Integer.parseInt( br.readLine() );

        //loop through each test case
        for( int i = 0; i < times; i++){
            
            

        }


        
    }

}
