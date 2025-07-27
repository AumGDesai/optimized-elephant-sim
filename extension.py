"""
Aum Desai
Fall 2022
CS152B Project 06 Extension

This program is for Project 06 Extension. 
You run it by putting python3 and the file name in the terminal. python3 extension.py
This file optimizes the elephant.py file which is a simulation of an elephant population.
This file finds the optimal darting probability for different situations of elephant populations.
This extension automatically plots the results into a graph plot. 

"""

import sys
import elephant
import random as rand
import matplotlib.pyplot as plt


def optimize(min, max, optfunc, parameters = None, tolerance = 0.001, maxIterations = 20, verbose = False):

    '''
    This function takes in 7 arguments and returns 1 value.
    It uses the concept of binary search to optimize a variable
    in a simulation.
    '''

    done = False

    while not done:

        testValue = (max + min) / 2

        if verbose == True:

            print(testValue)

        result = optfunc(testValue, parameters)

        if verbose == True:

            print(result)

        if result > 0:

            max = testValue

        elif result < 0:

            min = testValue

        else:

            done = True

        sub = max - min

        if sub < tolerance:

            done = True

        maxIterations -= 1

        if maxIterations <= 0:

            done = True
        
    return testValue


#def testEsim():

    '''
    This function simple gives the optimize function all
    the values to optimize the Prob Dart paramater. 
    '''

    res = optimize(0.0, 0.5, elephant.elephantSim, tolerance = 0.01, verbose = True)
    print(res)

#if __name__ == "__main__":
    testEsim()


# # a function that returns x - target
# def target(x, pars):
#     return x - 0.73542618

# # Tests the binary search using a simple target function.
# # Try changing the tolerance to see how that affects the search.
# def testTarget():
#     res = optimize( 0.0, 1.0, target, tolerance = 0.000000001, verbose=True)
#     print(res)

# if __name__ == "__main__":
#     testTarget()

# Evaluates the effects of the selected parameter on the dart percentage
# whichParameter: the index of the parameter to test
# testmin: the minimum value to test
# testmax: the maximum value to test
# teststep: the step between parameter values to test
# defaults: default parameters to use (default value of None)
def evalParameterEffect( whichParameter, testmin, testmax, teststep, defaults=None, verbose=False ):

    '''
    This function takes in 6 arguments and evaluates a list of tuples
    that show how a changing paramater effects another result of the elephant
    simulation.
    '''

    # if defaults is None, assign to simParameters the result of calling elephant.defaultParameters.
    if defaults == None:

        simParameters = elephant.defaultParameters()

    # else, assign to simParameters a copy of defaults (e.g. simParameters = defaults[:]
    else:

        simParameters = defaults[:]

    # create an empty list (e.g. results) to hold the results
    results = []

    if verbose:

        print("Evaluating parameter %d from %.3f to %.3f with step %.3f" % (whichParameter, testmin, testmax, teststep))

    # assign to t the value testmin
    t = testmin
    # while t is less than testmax
    while t < testmax:

        # assign to the whichParameter element of simParameters (e.g.simParameters[whichParameter]) the value t
        simParameters[whichParameter] = t

        # assign to percDart the result of calling optimize with the appropriate arguments, including simParameters
        percDart = optimize(0,1,elephant.elephantSim,simParameters)
        # append to results the tuple (t, percDart)
        results.append((t,percDart))

        if verbose:

            print("%8.3f \t%8.3f" % (t, percDart))

        # increment t by the value teststep
        t += teststep

    if verbose:
        print("Terminating")
    # return the list of results
    return results

# Test your evalParameterEffects function by modifying your top level
# code at the bottom of your file to be the following.
#if __name__ == "__main__":

    evalParameterEffect(elephant.IDXProb_Adult_Survival, 0.98, 1.0, 0.001, verbose=True)

res = evalParameterEffect(elephant.IDXMaximum_Age, 56, 66, 2, verbose=True)


plt.scatter(*zip(*res))
plt.title("Effect of Changing parameters of Elephant Population on Optimal Percent Darted")
plt.xlabel("Max Age")
plt.ylabel("Optimal Percent Darted")
plt.show()