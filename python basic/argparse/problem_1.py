# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument('physics', type=int,  help='physics marks')
# parser.add_argument('chemistry', type=int,  help='chemistry marks')
# parser.add_argument('maths', type=int,  help='maths marks')
# args = parser.parse_args()
# print(args.physics)
# print(args.chemistry)
# print(args.maths)
# print("result",(args.physics+args.chemistry+args.maths)/3)



import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--physics', type=int, required=True, help='physics marks')
parser.add_argument('--chemistry', type=int, required=True, help='chemistry marks')
parser.add_argument('--maths', type=int, required=True, help='maths marks')

args = parser.parse_args()

print(args.physics)
print(args.chemistry)
print(args.maths)
print("result", (args.physics + args.chemistry + args.maths) / 3)
