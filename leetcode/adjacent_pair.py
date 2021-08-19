"""
Integer V lies strictly between integers U and W if U < V < W or if U > V > W.
A non-empty zero-indexed array A consisting of N integers is given.
A pair of indices (P, Q), where 0 ≤ P < Q < N, is said to have adjacent values if no value
in the array lies strictly between values A[P] and A[Q].
For example, in array A such that:
A[0] = 0
A[1] = 3
A[2] = 3
A[3] = 7
A[4] = 5
A[5] = 3
A[6] = 11
A[7] = 1
the following pairs of indices have adjacent values:
(0, 7), (1, 2), (1, 4),
(1, 5), (1, 7), (2, 4),
(2, 5), (2, 7), (3, 4),
(3, 6), (4, 5), (5, 7).
For example, indices 4 and 5 have adjacent values because there is no value in array A that lies
strictly between A[4] = 5 and A[5] = 3; the only such value could be the number 4,
and it is not present in the array.
Write a function that returns number of adjacent values
"""
def comb(arr, r, start, end, index, data, ans):
    if index == r:
        ans.append(tuple(data))
        return
    i = start
    while i <= end and end-i+1 >= r-index:
        data[index] = arr[i]
        comb(arr, r, i+1, end, index+1, data, ans)
        i += 1

def pair(arr):
    ans = []
    r = 2
    data = [0,0]
    comb(arr, r, 0, len(arr)-1, 0, data, ans)
    return ans

# print(pair([1,2,5]))

def adjacent_pair(A):
    map_list = {}
    for i in range(len(A)):
        if A[i] not in map_list:
            map_list[A[i]] = []
        map_list[A[i]].append(i)
    print(map_list)
    keys = list(map_list)
    keys.sort()
    ans = []
    for i in range(1, len(keys)):
        k = keys[i]
        print(k, map_list[k])
        prev_k = keys[i-1]
        prev_id_list = map_list[prev_k]
        id_list = map_list[k]
        for id in id_list:
            for prev_id in prev_id_list:
                ans.append((prev_id, id))
        pairs = pair(id_list)
        for p in pairs:
            ans.append(p)
    
    ans.sort()
    print(ans)
    return len(ans)

print(adjacent_pair([0, 3, 3, 7, 5, 3, 11, 1]))