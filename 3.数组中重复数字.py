def get_dup(lst):
    """
    时间复杂度 O(n)
    
    """
    from collections import Counter
    c = Counter(lst)

    ret = []

    for k, v in c.items():
        if v > 1:
            ret.append(k)
    return ret


if __name__ == '__main__':
    example = [2, 3, 1, 0, 2, 5, 3]
    print(get_dup(example))
