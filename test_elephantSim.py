# Bruce Maxwell
# Fall 2015
# CS 151 Project 6
#
# Test function for elephantSim.
#
#
import sys
import elephant

def main(argv):

    for i in range(5):
        probDarting = 0.405 + i * 0.01
        diff = elephant.elephantSim( probDarting )
        print("probDarting %.3f  diff %d" % (probDarting, diff))

    return

if __name__ == "__main__":
    main(sys.argv)