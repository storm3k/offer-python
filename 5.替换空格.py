def replace_black(string):
    ret = ['%20' if x == ' ' else x for x in string]
    return ''.join(ret)


if __name__ == '__main__':
    print(replace_black('We are happy.'))
