import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true',help='perform operation silently')
group.add_argument('-v','--verbose',action='store_true',help='increase verbosity')
parser.add_argument('x',type=float,help='the base')
parser.add_argument('y',type=float,help='the power')
args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print('answer')
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))

