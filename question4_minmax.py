def minmax(list1):
    """
    find both the minimum and maximum within list1.
    # You can assume list1 size is even.
    required number of comparisons: 3n/2  (This is not big O, you should limit your "<", ">" comparisons)

	:param list1: List -- list of integers
    :return: a tuple of two integers. The first integer is the minimum, the second integer is the maximum.
    """
    cmax = []
    cmin = []
    for i in range(0, len(list1), 2):
        if list1[i] > list1[i + 1]:
            cmax.append(list1[i])
            cmin.append(list1[i + 1])
        else:
            cmax.append(list1[i + 1])
            cmin.append(list1[i])
    maxi = max(cmax)
    mini = min(cmin)
    return (mini, maxi)


'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.


def main():
    print(minmax([150, 24, 79, 50, 98, 88, 345, 3]))    # (3, 345)
    print(minmax([678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561, 100]))  # (37, 982)

if __name__ == '__main__':
    main()
'''