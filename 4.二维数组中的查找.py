def idx(lst, k):
    if not k:
        return False
    m = len(lst)
    n = len(lst[1])
    for i in range(m):
        for j in range(n-1, -1, -1):
            if lst[i][j] == k:
                return True
            elif lst[i][j] > k:
                n -= 1
            elif lst[i][j] < k:
                break
    return False


if __name__ == '__main__':
    example = [
        [1,  2,  8,  9],
        [2,  4,  9, 12],
        [4,  7, 10, 13],
        [6,  8, 11, 15]
    ]

    keys = [
        1, 15, 10,
        0, 16, 5,
        None
    ]

    for k in keys:
        print(k, idx(example, k))
