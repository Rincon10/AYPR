import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {
    public static int backTracking(List<Integer> list, int index, int steps, int length) {
        if (index >= length - 1) return 0;

        int delta = 1;
        if (index + 2 < length && list.get(index + 2) == 0) delta = 2;

        return Math.min(steps, 1 + backTracking(list, index + delta, steps + index, length));
    }

    /*
     * Complete the 'jumpingOnClouds' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY c as parameter.
     */
    public static int jumpingOnClouds(List<Integer> c) {
        // Write your code here

        return backTracking(c, 0, 100, c.size());
    }

}

class Solution {
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt("7");

        List<Integer> c = Stream.of("0 0 1 0 0 1 0".split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = Result.jumpingOnClouds(c);

        System.out.println(result);
    }
}
