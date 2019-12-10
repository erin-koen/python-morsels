def add(*args):
    # args is an iterable that contains lists that contain lists.
    # each outer list is an iterable that contains two lists
    # each inner list is an iterable that contains a certain number of integers
    # want to get to a point where we have
    # [[[1,2], [-2, -1]], [[-3, 0], [4, -1]]]
    # ^^ need the same index from same inner array in all outer arrays
    # then can sum each array so it's
    # [[3, -3], [-3, -3]]
    # TODO
    # use generators to... generate matched_by_index
    # handle assumption that all lists passed are the same length
    
    matched_by_index = []
    
    for j in range(len(args[0])):
        by_inner_index = []
        for k in range(len(args[0][0])):
            by_outer_index = []
            for i in range(len(args)):
                by_outer_index.append(args[i][j][k])
            by_inner_index.append(by_outer_index)
        matched_by_index.append(by_inner_index)

    summed = [
        [
            sum(item)
            for item in inner
        ]
        for inner in matched_by_index
    ]

    return summed


'''
loop | argument  | outer index  | inner index  | expected
  1         0            0               0          1
  2         1            0               0          2
  3         0            1               0          -2
  4         1            1               1          -1
  5         0            0               1          




'''

# 0,0,0
# 1,0,0

# 0,0,0
# 0,0,0

# 0


m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[-1, -2, -3], [-4, -5, -6]]
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add(m1, m2))

'''
return [
        [
            item + list2[k][i]
            for i, item in enumerate(inner_list)
        ]
        for k, inner_list in enumerate(list1)

    ]
    '''
