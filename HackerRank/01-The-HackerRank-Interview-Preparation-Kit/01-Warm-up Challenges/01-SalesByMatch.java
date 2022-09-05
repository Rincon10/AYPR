import java.io.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.*;


import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'sockMerchant' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY ar
     */

    public static int sockMerchant(int n, List<Integer> ar) {
        // Write your code here

        // Function.identity() === ( element -> element )

        Map<Integer, Long> list = ar.stream().collect(Collectors.groupingBy(number -> number, Collectors.counting()));
        System.out.println(list);

        AtomicInteger answer = new AtomicInteger(0);
        list.forEach( (key, value ) -> {
            int delta = (int) (value/2);
            answer.getAndAdd(delta);
        });

        return answer.get();
    }

}

class Solution {
    public static void main(String[] args) throws IOException {
//        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt("9");

        List<Integer> ar = Stream.of("10 20 20 10 10 30 50 10 20".replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = Result.sockMerchant(n, ar);
        System.out.println(result);

    }
}
