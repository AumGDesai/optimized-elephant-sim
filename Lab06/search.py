"""
Aum Desai
Fall 2022
CS152B Lab 06

This program is for Lab 06.
It goes over the basics of binary search.
You run it by putting python3 and the file name in the terminal. python3 search.py

"""

import random as rand

def searchSortedList( mylist, value ):

    '''
    This function takes in 2 arguments and then sorts a list and then runs
    a binary search on it. 
    '''
    # assign to the variable done, the value False
    done = False
    # assign to the variable found, the value False
    found = False
    # assign to the variable count, the value 0
    count = 0
    # assign to the variable maxIdx, the one less than the length of mylist
    maxIdx = len(mylist) - 1
    # assign to the variable minIdx, the value 0
    minIdx = 0
    # start a while loop that executes while done is not True
    while not done:
        # increment count (which keeps track of how many times the loop executes
        count += 1
        # assign to testIndex the average of maxIdx and minIdx(use integer math)
        testIndex =  (maxIdx + minIdx) // 2
        # if the myList value at testIndex is less than value
        if mylist[testIndex] < value:
            # assign to minIdx the value testIndex + 1
            minIdx = testIndex + 1
        # elif the myList value at testIndex is greater than value
        elif mylist[testIndex] > value:
            # assign to maxIdx the value testIndex - 1
            maxIdx =  testIndex - 1
        # else
        else:
            # set done to True
            done = True
            # set found to True
            found = True
            #if maxIdx is less than minIdx
            if maxIdx < minIdx:
                # set done to True
                done = True
                # set found to False
                found = False
    return(found, count)

def test():

    '''
    This a test function that tests the previous function to see if it executes binary search. 
    '''
    a = []
    N = 10**6
    for i in range (N):
        a.append(rand.randint(0,N) )
    a.append(42)
    a.sort()
    print(searchSortedList( a, 42 ))


if __name__ == "__main__":
    test()