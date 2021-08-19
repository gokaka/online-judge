"""
https://javabypatel.blogspot.com/2020/09/find-longest-length-bi-valued-slice-in-array-in-java.html

Find longest length bi-valued slice in an array in java
This is a popular interview question asked in Tier-1 companies.

You are given a sequence of n integers,
and the task is to find the maximum slice of the array which contains no more than two different numbers.

Example:
1. Input: [1, 2, 1, 2, 2, 3, 3, 2, 3]
Output: 6
Max slice is [2, 2, 3, 3, 2, 3] which contains only two numbers 2 and 3 and the length is 6 
2. Input: [1, 2, 3]
Output: 2
Max slice is either [1, 2] or [2, 3] which contains only two numbers and the length is 2

3. Input: [1, 4, 4, 1, 4]
Output: 5 
Max slice is whole array which contains only two numbers 1 and 4 and the length is 5

4. Input: [2]
Output: 1 
Max slice is whole array which contains only one number 2 and the length is 1
"""

def longest_bi_slice(A):
    max_len = 0
    bi_map = {}
    left = 0
    right = 0
    slice_len = 0
    slice = []
    for i in range(len(A)):
        right = i
        bi_map[A[right]] = right
        slice_len = right - left + 1
        if len(bi_map) > 2: # if unique number in slice more than 2, move left pointer to min_idx+1
            min_idx_list = [bi_map[k] for k in bi_map]
            min_idx = min(min_idx_list)
            del bi_map[A[min_idx]]
            left = min_idx+1
        elif slice_len > max_len: # keep first longest slice
            max_len = slice_len
            slice = A[left: right+1]
    
    print(slice)
    return max_len

print(longest_bi_slice([1, 2, 1, 2, 2, 3, 3, 2, 3]))
print(longest_bi_slice([1, 2, 3]))
print(longest_bi_slice([1, 4, 4, 1, 4]))
print(longest_bi_slice([2]))
print(longest_bi_slice([]))
