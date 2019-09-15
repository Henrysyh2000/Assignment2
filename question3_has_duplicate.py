def has_duplicate(list1):
# the Complexity of this fuction is O(n^2)
    """
    remember to mention your runtime as comment!

    :param l: List -- list of integers
    :return: True if list1 has duplicate, return False otherwise.
    """
    while len(list1) != 0:
        new = list1[1:]
        if list1[0] in new:
            return True
        else:
            list1.pop(0)
    return False
        
        

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(has_duplicate([0,6,2,4,9]))   # False

    print(has_duplicate([0,6,2,4,9,1,2]))   # True

#if __name__ == '__main__':
    #main()