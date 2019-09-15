def merge(I1, I2):  
    """
    takes two iterable objects and merges them alternately
    required runtime: O(len(I1) + len(I2)).

    :param I1: Iterable -- the first iterable object. Can be a string, tuple, etc
    :param I2: Iterable -- the second iterable object. Can be a string, tuple, etc

    :return: List -- alternately merged I1, I2 elements in a list.
    """
    res = []
    index = 0      
    while index < min(len(I1), len(I2)):
        res.append(I1[index])
        res.append(I2[index])
        index += 1
    if len(I1) > len(I2):
        for i in range(index, len(I1)):
            res.append(I1[i])
    elif len(I2) > len(I1):
        for i in range(index, len(I2)):
            res.append(I2[i])
    return res

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print([i for i in merge("what",range(100,105))])
    print([i for i in merge(range(5),range(100,101))])
    print([i for i in merge(range(1),range(100,105))])

if __name__ == '__main__':
    main()