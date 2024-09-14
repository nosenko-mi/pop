import sys
import math


def f(x):
    e = math.exp(2*x)
    return (e-8)/(x+3)


def main(args):
    if len(args) < 4:
        print("Not all arguments provided. Expected input: main.py <min_x> <max_> <delta_x>")
        return -1
    
    min_x = float(args[1])
    max_x = float(args[2])
    delta_x = float(args[3])

    i = min_x
    res = []
    while i <= max_x:
        tmp = f(i)
        res.append(tmp)

        print(f"x={i:.2f}; y={tmp:.2f}")

        i += delta_x

    return res

    
main(sys.argv)