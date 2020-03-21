# import neccessary packages
import argparse

# construct the argument parser
parser = argparse.ArgumentParser()
# parser.add_argument('echo',help="echo the string you use here")
parser.add_argument('square',help='display the square of a number',type=int)
# parser.add_argument('-v','--verbosity',help='Increase output verbosity',action='store_true') # as flag
# parser.add_argument("-v", "--verbosity", type=int, choices = [0,1,2], help="increase output verbosity") # as integer
# parser.add_argument("-v", "--verbosity", action="count",help="increase output verbosity") 
parser.add_argument("-v", "--verbosity", action="count", default=0,help="increase output verbosity")

args = parser.parse_args()
number = args.square
squared = number**2
# if args.verbosity == 2:
if args.verbosity >= 2:
    print("the square of {} equals {}".format(number, squared))
elif args.verbosity == 1:
    print("{}^2 == {}".format(number, squared))
else:
    print(squared)