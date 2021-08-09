/*
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
*/

// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        if(A.length < 3) return 0;

        for(int i=2; i<A.length; i++){
            int P = A[i-2];
            int Q = A[i-1];
            int R = A[i];
            if (P+Q > R && Q+R > P && R+P > Q){
                return 1;
            }
        }
        return 0;
    }
}

// extreme_arith_overflow
// overflow test, 3 MAXINTs
// https://app.codility.com/demo/results/training7Z65YH-QD9/

// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        if(A.length < 3) return 0;

        for(int i=2; i<A.length; i++){
            int P = A[i-2];
            int Q = A[i-1];
            int R = A[i];
            if (P > R-Q && Q > P-R && R > Q-P){  // fix int overflow
                return 1;
            }
        }
        return 0;
    }
}

// https://app.codility.com/demo/results/training2YH5K4-EZU/
