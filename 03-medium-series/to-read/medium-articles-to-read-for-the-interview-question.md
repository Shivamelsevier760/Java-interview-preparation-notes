# medium articles to read for the interview questions from now onwards

https://medium.com/javarevisited/top-java-developer-interview-questions-ace-your-job-interview-series-21-springboot-microservice-decccb2ef402

https://medium.com/javarevisited/senior-java-developer-interview-questions-series-15-ff50ed01a8d8

# **Technical Round preparation steps:**

Typically interview starts with your intro and the interviewer may ask you about the project that you have been working on.

***Step-1. Know the project that you have working on, of the current job in and out. We should be able to talk about the below things.***

a. Projects Functionality including what it does, and what problem it solves for customers, Basically you should know your project functional overview.

b. Know your project Architecture and Technical stack. Also, you can dig deeper to know about flow end to end.

c. Technical Stack wise talk about what has been used in the project. As which front-end is used(angular, react), which backend is used(like Java, Python), and which Database([Postgres](https://medium.com/javarevisited/7-best-free-postgresql-courses-for-beginners-to-learn-in-2021-3bf369d73794), [DynamoDB](https://medium.com/javarevisited/7-best-aws-s3-and-dynamodb-courses-for-beginners-in-2021-a8a44b6066da)).

d. What kind of CI-CD model is used here, like the deployment part that developers are mostly unaware of?

The above project-related stuff should be thoroughly studied by you so that you can drive the interview on your side, This is important, remember your answers generally drive the interview.

***Step 2. As a Java Developer, you should know the below topics which will increase your chance of getting selected.***

1. [**Object Oriented programming](https://www.educative.io/blog/object-oriented-programming) topics including SOLID principles. (prepare for inheritance puzzles)**
2. [**Multithreading and Concurrency](https://www.educative.io/blog/multithreading-and-concurrency-fundamentals)(prepare for Executor framework and concurrency API**
3. **Collection framework (Prepare for the internal working of each collection data structure like HashMap, Concurrent hashmap, HashSet)**
4. **Serialization (How it works)**
5. **Design Patterns (prepare at least 4–5 design patterns like creational, behavioral, and structural patterns)**
6. **Garbage Collections**
7. **Java Generics**
8. **Java 8 (Stream and Functional Programming-prepare for Java 8 coding programs on streams)**
9. **SQL Queries (prepare to write queries on JOINS and employee table like highest salary and all)**
10. **Coding practice (prepare Array and String problems as much as you can)**
11. **Memory Management (Know about Java 8 and above version memory management changes)**

The above area is a must to clear the interview. Generally, ***a candidate gets selected based on his practical knowledge, and if he is good at writing programs and SQL queries using Java he can clear interviews easily.***

**Top 15 DS Algo Interview Questions for Java Developers(Commonly Asked)**

1. **Print all substrings of a string (List every possible substring)**

```jsx
public class SubstringPrinter {

    public static void main(String[] args) {
        String str = "example";
        printAllSubstrings(str);
    }

    public static void printAllSubstrings(String str) {
        int n = str.length();
        // Loop through all possible starting points of substrings
        for (int i = 0; i < n; i++) {
            // Loop through all possible ending points of substrings
            for (int j = i + 1; j <= n; j++) {
                // Print the substring from index i to j
                System.out.println(str.substring(i, j));
            }
        }
    }
}
```

Explanation:

1. **Outer Loop (`i`)**: Iterates through each character in the string as the starting point of the substring.
2. **Inner Loop (`j`)**: Iterates from the current starting point (`i`) to the end of the string, defining the ending point of the substring.
3. **`str.substring(i, j)`**: Extracts and prints the substring from index `i` to `j`.

**2. Return all subsequences of a string(Generate all possible subsequences, not necessarily contiguous).**

```jsx
import java.util.ArrayList;
import java.util.List;

public class SubsequenceGenerator {

    public static void main(String[] args) {
        String str = "abc";
        List<String> subsequences = generateAllSubsequences(str);
        System.out.println(subsequences);
    }

    public static List<String> generateAllSubsequences(String str) {
        List<String> subsequences = new ArrayList<>();
        generateSubsequencesHelper(str, "", 0, subsequences);
        return subsequences;
    }

    private static void generateSubsequencesHelper(String str, String current, int index, List<String> subsequences) {
        if (index == str.length()) {
            subsequences.add(current);
            return;
        }

        // Include the current character
        generateSubsequencesHelper(str, current + str.charAt(index), index + 1, subsequences);

        // Exclude the current character
        generateSubsequencesHelper(str, current, index + 1, subsequences);
    }
}
```

Explanation:

1. **`generateAllSubsequences` Method**: Initializes the list to store subsequences and calls the helper method.
2. **`generateSubsequencesHelper` Method**: Recursively generates subsequences.
- **Base Case**: When the index reaches the length of the string, add the current subsequence to the list.
- **Recursive Case**:
- Include the current character and move to the next index.
- Exclude the current character and move to the next index.

This method ensures that all possible subsequences (including the empty subsequence) are generated and returned.

**3. Rotate an array to the right by k steps— Shift elements right by k positions.**

```jsx
import java.util.Arrays;

public class ArrayRotator {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;
        rotateRight(arr, k);
        System.out.println(Arrays.toString(arr));
    }

    public static void rotateRight(int[] arr, int k) {
        int n = arr.length;
        k = k % n; // In case k is greater than the length of the array
        reverse(arr, 0, n - 1);
        reverse(arr, 0, k - 1);
        reverse(arr, k, n - 1);
    }

    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
```

Explanation:

1. **`rotateRight` Method**:
- **Step 1**: Calculate the effective rotation steps `k` by taking `k % n` (where `n` is the length of the array) to handle cases where `k` is greater than the array length.
- **Step 2**: Reverse the entire array.
- **Step 3**: Reverse the first `k` elements.
- **Step 4**: Reverse the remaining `n - k` elements.

**`reverse` Method**: Reverses the elements in the array between the specified `start` and `end` indices.

**4. Rotate an array to the left by d steps— Shift elements left by d positions**

```jsx
import java.util.Arrays;

public class ArrayRotator {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int d = 3;
        rotateLeft(arr, d);
        System.out.println(Arrays.toString(arr));
    }

    public static void rotateLeft(int[] arr, int d) {
        int n = arr.length;
        d = d % n; // In case d is greater than the length of the array
        reverse(arr, 0, d - 1);
        reverse(arr, d, n - 1);
        reverse(arr, 0, n - 1);
    }

    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
```

Explanation:

1. **`rotateLeft` Method**:
- **Step 1**: Calculate the effective rotation steps `d` by taking `d % n` (where `n` is the length of the array) to handle cases where `d` is greater than the array length.
- **Step 2**: Reverse the first `d` elements.
- **Step 3**: Reverse the remaining `n - d` elements.
- **Step 4**: Reverse the entire array.

**`reverse` Method**: Reverses the elements in the array between the specified `start` and `end` indices.

This approach ensures that the array is rotated to the left by `d` steps efficiently with a time complexity of O(n).

**5. String compression— Compress repeated characters into counts.**