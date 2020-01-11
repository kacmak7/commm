import argparse

parser = argparse.ArgumentParser(description='connects you with a world')
parser.add_argument('--yo', required=False, dest='yo_var', type=str)

subparsers = parser.add_subparsers()
init = subparsers.add_parser('init', help='initialize smth idk')
init.add_argument('-y', help='YES')

args = parser.parse_args()

if args.yo_var:
    res = args.yo_var 
else:
    res = args.
print(res)
