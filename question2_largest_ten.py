def largest_ten(list1):
    """
    find the largest ten elements in list1. Assume list size greater than 10.
    required runtime: O(len(list1))

    :param list1: List -- list of integers
    
    :return: List -- largest ten elements in list list1, as a new size 10 list. (Order doesn't matter.)
    """
    ten = list1[:10]
    ten.sort()
    print(ten)
    for i in list1[10:]:
        if i > ten[0]:
            ten[0] = i
            ten.sort()
    return ten
'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.


def main():
    print(largest_ten([9,8,6,4,22,68,96,212,52,12,6,8,99]))

    print(largest_ten([42,10,90,75,79,98,11,90,92,11,21,8,47,72,25,94,99,54,69,60]))

if __name__ == '__main__':
    main()
'''    
