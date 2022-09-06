import java.io.*;
import java.util.*;


interface SortAlgorithm {
    int[] sort(int[] arr);
}

class MinimumSteps implements SortAlgorithm {
    @Override
    public int[] sort(int[] arr) {
        int count = 0;
        int i = 0;

        while (i < arr.length) {
            int index = arr[i] - 1;
            if (arr[i] != arr[index]) {
                int temp = arr[i];

                arr[i] = arr[index];
                arr[index] = temp;
                count += 1;
//                Arrays.stream(arr).forEach(System.out::print);
//                System.out.println("");
            } else {
                i += 1;
            }
        }
        return new int[]{count};
    }
}

class InsertionSort implements SortAlgorithm {
    @Override
    public int[] sort(int[] arr) {
        int steps = 0;

        for (int i = 1; i < arr.length; i++) {
            int currentValue = arr[i];
            while (i > 0 && arr[i - 1] > currentValue) {
                arr[i] = arr[i - 1];
                i -= 1;
                steps += 1;
            }
            arr[i] = currentValue;
        }

        arr[0] = steps;
        return arr;
    }
}

class MergeSort implements SortAlgorithm {

    @Override
    public int[] sort(int[] arr) {
        int index = arr.length / 2;
        int steps = 0;
        while (index > 0) {
            for (int i = index; i < arr.length; i++) {
                int currentValue = arr[i];
                int currentIndex = i;

                while (currentIndex >= index && arr[currentIndex - index] > arr[currentIndex]) {
                    steps += currentIndex - (currentIndex - index);
                    arr[currentIndex] = arr[currentIndex - index];
                    currentIndex -= index;
                    arr[currentIndex] = currentValue;
                }
            }
            index /= 2;
        }
        return arr;
    }
}

public class Result {

    public static int sort(int[] arr) {
        SortAlgorithm algorithm = new MinimumSteps();
        return algorithm.sort(arr)[0];
    }

    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        return sort(arr);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int n = 4;
        int[] arr = new int[n];

        String[] arrItems = "4 3 1 2".split(" ");
        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }
        int res = minimumSwaps(arr);
        System.out.println(res);
    }
}


