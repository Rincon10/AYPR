import java.io.*;

import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;
import java.util.stream.*;

class Result {
    /*
     * Complete the 'repeatedString' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. LONG_INTEGER n
     */


    public static long repeatedString(String s, long n) {
        // Write your code here

        if (s.equals("a")) return n;
        if (!s.contains("a")) return 0;

        long length = s.length();
        long times = (n % length);
        long size =  (n / length);
        AtomicInteger additional = new AtomicInteger();

        int cont = 0;
        for (String _char : s.split("")) {
            if (cont == times) break;
            if (_char.equals("a")) additional.getAndIncrement();
            cont++;
        }

        Map<String, Long> answ = Stream.of(s.split("")).collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        return answ.get("a") * size + additional.get() ;
    }

}

class Solution {
    public static void main(String[] args) throws IOException {


        String s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm";

        long n = Long.parseLong("736778906400");

        long result = Result.repeatedString(s, n);
        System.out.println(result);

    }
}
