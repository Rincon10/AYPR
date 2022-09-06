import java.io.*;
import java.util.*;
import java.util.stream.*;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'rotLeft' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY a
     *  2. INTEGER d
     */

    public static List<Integer> rotLeft(List<Integer> a, int d) {
        // Write your code here
        int length = a.size();
        List<Integer> newList = new ArrayList<>();

        for (int i = 0; i < length; i++) {
            newList.add(a.get(d % length));
            d++;
        }
        return newList;
    }
}

class Solution {
    public static void main(String[] args) throws IOException {

        String[] firstMultipleInput = "5 4".split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int d = Integer.parseInt(firstMultipleInput[1]);

        List<Integer> a = Stream.of("1 2 3 4 5".split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> result = Result.rotLeft(a, d);

        System.out.println(result.stream().map(Object::toString).collect(joining(" ")));
    }
}
