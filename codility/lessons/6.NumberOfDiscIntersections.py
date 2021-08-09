"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    def searchIndex(val, arr, from_id):
        low = from_id
        high = len(arr) - 1

        if val < arr[low]: return -1
        if val >= arr[high]: return high

        while low <= high:
            mid = (low + high) // 2
            # print('search', low, high, mid, arr[mid])
            if arr[mid] < val:
                low = mid + 1
            elif val < arr[mid]:
                high = mid - 1
            else:
                # search: 3
                # [1,2,3,3,3,4,5]
                #          ^4
                idx = mid
                while idx < len(arr) and arr[idx] <= val:
                    idx += 1
                break
        return high

    interval_list = []
    for i in range(len(A)):
        start = i - A[i]
        end = i + A[i]
        interval_list.append((start, end))
    interval_list.sort()
    start_list = [start for (start,end) in interval_list]
    # print(start_list)
    
    result = 0
    for i in range(len(interval_list)-1):
        start,end = interval_list[i]
        matchId = searchIndex(end, start_list, i)
        # print(end, matchId, i)
        if matchId != -1:
            intersect_count = matchId - i
            # print(intersect_count)
            result += intersect_count

    return result

# Wrong answer
# https://app.codility.com/demo/results/trainingDVG2P5-8AG/
"""
Analysis summary
The following issues have been detected: wrong answers.

For example, for the input [1, 0, 1, 0, 1] the solution returned a wrong answer (got 10 expected 6).
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    def searchIndex(val, arr, from_id):
        low = from_id
        high = len(arr) - 1

        if val < arr[low]: return -1
        if val >= arr[high]: return high

        while low <= high:
            mid = (low + high) // 2
            # print('search', low, high, mid, arr[mid])
            if arr[mid] < val:
                low = mid + 1
            elif val < arr[mid]:
                high = mid - 1
            else:
                # search: 3
                # [1,2,3,3,3,4,5]
                #          ^4
                idx = mid
                while idx < len(arr) and arr[idx] <= val:
                    idx += 1
                return idx-1
        
        return high

    interval_list = []
    for i in range(len(A)):
        start = i - A[i]
        end = i + A[i]
        interval_list.append((start, end))
    interval_list.sort()
    start_list = [start for (start,end) in interval_list]
    # print(start_list)
    
    result = 0
    for i in range(len(interval_list)-1):
        start,end = interval_list[i]
        matchId = searchIndex(end, start_list, i+1)
        # print(end, matchId, i)
        if matchId != -1:
            intersect_count = matchId - i
            # print(intersect_count)
            result += intersect_count
            if result > 10000000:
                return -1

    return result

# AC
# https://app.codility.com/demo/results/training7FG3MU-26Y/