import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'hourglassSum' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */

    public static int hourglassSum(List<List<Integer>> arr) {
        // Write your code here
        Integer[][] positions = {{1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, -1}, {-1, 1}, {0, 0}};

        int length = arr.size();
        double max = Double.NEGATIVE_INFINITY;
        for (int i = 1; i < length - 1; i++) {
            for (int j = 1; j < length - 1; j++) {
                int temp = 0;
                for (Integer[] position : positions) {
                    if (i + position[0] < 0 || i + position[0] >= length) break;
                    if (j + position[1] < 0 || j + position[1] >= length) break;
                    temp += arr.get(i + position[0]).get(j + position[1]);
                }
                max = Math.max(temp, max);
            }
        }
        return (int)max;
    }
}

class Solution {
    public static void main(String[] args) throws IOException {
        List<List<Integer>> arr = new ArrayList<>();

        String[] list = "0 -4 -6 0 -7 -6,-1 -2 -6 -8 -3 -1,-8 -4 -2 -8 -8 -6,-3 -1 -2 -5 -7 -4,-3 -5 -3 -6 -6 -6,-3 -6 0 -8 -6 -7".split(",");
        IntStream.range(0, 6).forEach(i -> {
            arr.add(
                    Stream.of(list[i].replaceAll("\\s+$", "").split(" "))
                            .map(Integer::parseInt)
                            .collect(toList())
            );
        });

        int result = Result.hourglassSum(arr);

        System.out.println(result);
    }
}
