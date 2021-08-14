/*
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
*/

// null pointer error
// The following issues have been detected: runtime errors.
// For example, for the input [1, 2] the solution terminated unexpectedly.
// https://app.codility.com/demo/results/trainingQUESJV-EV9/


import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        Integer leader = null;
        Integer leaderCount = 0;
        Map<Integer, Integer> leaderCountMap = new HashMap<>();
        for(int a : A){
            int count = leaderCountMap.getOrDefault(a, 0);
            count += 1;
            leaderCountMap.put(a, count);
            if (count >= A.length / 2){
                leaderCount = count;
                leader = a;
            }
        }
        if (leader == null) return 0; // no leader case
        // System.out.println("leader: " + leader);
        // System.out.println("leaderCount: " + leaderCount);
        int result = 0;
        int leftLeaderCount = 0;
        for(int i=0; i<A.length; i++){
            if(A[i] == leader){
                leftLeaderCount += 1;
            }
            int rightLeaderCount = leaderCount - leftLeaderCount;
            int leftSeqLen = i + 1;
            int rightSeqLen = A.length - i - 1;
            if (leftLeaderCount > leftSeqLen / 2 && rightLeaderCount > rightSeqLen/2){
                // System.out.println("split: " + i);
                result += 1;
            }
        }
        // System.out.println(result);
        return result;
    }
}

// https://app.codility.com/demo/results/training9FTJCT-BPU/
