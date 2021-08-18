"""
https://brainly.in/question/22119265?tbs_match=3

A rectangular map consisting of N rows and M columns of square areas is given. 
Each area is painted with a certain color. 
Two areas on the map belong to the same country if the following conditions are met: 
The map can be described by a zero-indexed matrix A consisting of N rows and M columns of integers. 
The color of each area is described by the corresponding element of the matrix. 
Two areas have the same color if and only if their corresponding matrix elements have the same value. 

For example, consider the following matrix A consisting of seven rows and three columns: 
A =[
[5, 4, 4],
[4, 3, 4],
[3, 2, 4],
[2, 2, 2],
[3, 3, 4],
[1, 4, 4],
[4, 1, 1],
]

Matrix A describes a map that is colored with five colors. 
The areas on the map belong to eleven different countries (C1−C11), as shown in the following figure: 

Write a function that, given a zero-indexed matrix A consisting of N rows and M columns of integers, returns the number of different countries to which the areas of the map described by matrix A belong. 

For example, given matrix A consisting of seven rows and three columns corresponding to the example above, the function should return 11
"""
def find_countries(A):
    union = {}
    R = len(A)
    C = len(A[0])
    union[(0,0)] = (0,0)
    for c in range(1, C):
        r = 0

    for r in range(R):
        for c in range(C):
            if (r,c) == (0,0):
                union[(r,c)] = (0, 0)
            elif r == 0 and c > 0:
                if A[r][c] == A[r][c-1]:
                    union[(r,c)] = union[(r,c-1)]
                else:
                    union[(r,c)] = (r,c)
            elif r > 0 and c==0:
                if A[r][c] == A[r-1][c]:
                    union[(r,c)] = union[(r-1,c)]
                else:
                    union[(r,c)] = (r,c)
            else:
                if A[r][c] == A[r-1][c]:
                    union[(r,c)] = union[(r-1,c)]

                    """
                    set left equals top father
                    1 2    (0,0)   (0,1)
                                     |
                    2 2    (1,0) - (0,1)
                           update (1,0) to (0,1) when scan (r,c) at (1,1)
                    """
                    if A[r][c] == A[r][c-1]:
                        union[(r,c-1)] = union[(r-1,c)]
                    
                elif A[r][c] == A[r][c-1]:
                        union[(r,c)] = union[(r,c-1)]
                else:
                    union[(r,c)] = (r,c)
    country_set = set()

    # output union map
    for r in range(R):
        print([union[(r,c)] for c in range(C)])

    # find union countries
    for r in range(R):
        for c in range(C):    
            country_set.add(union[(r,c)])
    print(country_set)
    return len(country_set)

A =[
[5, 4, 4],
[4, 3, 4],
[3, 2, 4],
[2, 2, 2],
[3, 3, 4],
[1, 4, 4],
[4, 1, 1],
]

print(find_countries(A))
