def getalnum(strval):
    ##################################################
    # make your code
    ##################################################
    # yield statement


def main():
    strval = 'Python Programming'
    ret = getalnum(strval)
    print(ret)  # print generator information
    retstr = ''.join(ret)

    # retstr = list(ret)
    print(retstr)


if __name__ == '__main__':
    main()
