import java.io.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.regex.Pattern;
import java.util.stream.*;


class Result {

    /*
     * Complete the 'countingValleys' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER steps
     *  2. STRING path
     */

    public static int countingValleys(int steps, String path) {
        // Write your code here

        AtomicInteger hills = new AtomicInteger();
        AtomicInteger position = new AtomicInteger();

        // String to Stream.
        Stream<String>  stream = Pattern.compile("").splitAsStream(path);

        stream.forEach( step -> {
            position.addAndGet((step.equals("U") ? 1 : -1));

            if ( position.get() == 0 && step.equals("U") ) hills.getAndIncrement();
        });
        return hills.get();
    }

}

class Solution {
    public static void main(String[] args) throws IOException {
//        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int steps = Integer.parseInt("8".trim());

        String path = "UDDDUDUU";
        int result = Result.countingValleys(steps, path);

        System.out.println(result);
    }
}
