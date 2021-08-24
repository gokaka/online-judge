"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

class Solution {
    public int solution(int[] A) {
        long maxEnding = Integer.MIN_VALUE; // use long to avoid overflow
        long maxSlice = Integer.MIN_VALUE;

        for(int i=0; i<A.length; i++) {
            maxEnding = Math.max(maxEnding+A[i], A[i]);
            maxSlice = Math.max(maxEnding, maxSlice);
        }
        return (int)maxSlice;
    }
}

// passed
// https://app.codility.com/demo/results/trainingF8ST9H-NCV/


class Solution {
    public int solution(int[] A) {
        long maxEnding = A[0]; // use long to avoid overflow
        long maxSlice = A[0];

        for(int i=1; i<A.length; i++) {
            maxEnding = Math.max(maxEnding+A[i], A[i]);
            maxSlice = Math.max(maxEnding, maxSlice);
        }
        return (int)maxSlice;
    }
}
// passed
// https://app.codility.com/demo/results/trainingJ58R85-F3X/


/* 
wrong answers
https://app.codility.com/demo/results/training2C749U-EM9/

The following issues have been detected: wrong answers.

For example, for the input [-10] the solution returned a wrong answer (got 0 expected -10).


▶one_element✘WRONG ANSWER
got 0 expected -10
1.0.004 sWRONG ANSWER, got 0 expected -10
2.0.004 sOK
3.0.008 sOK
▶two_elements✘WRONG ANSWER
got 0 expected -2
1.0.004 sWRONG ANSWER, got 0 expected -2
2.0.008 sOK
3.0.004 sOK
4.0.004 sOK
5.0.004 sOK
6.0.004 sOK
7.0.004 sOK
8.0.008 sOK
9.0.004 sOK
▶three_elements✘WRONG ANSWER
got 0 expected -2
1.0.004 sWRONG ANSWER, got 0 expected -2
2.0.004 sOK
3.0.004 sOK
4.0.004 sOK
5.0.008 sOK
6.0.004 sOK
7.0.004 sOK
8.0.004 sOK
9.0.008 sOK
10.0.004 sOK
11.0.004 sOK
12.0.004 sOK
13.0.004 sOK
14.0.004 sOK
15.0.004 sOK
16.0.004 sOK
17.0.004 sOK
18.0.008 sOK
19.0.004 sOK
20.0.004 sOK
21.0.004 sOK
22.0.004 sOK
23.0.004 sOK
24.0.004 sOK
25.0.004 sOK
26.0.004 sOK
27.0.004 s
*/