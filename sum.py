import sys


if __name__ == '__main__':
    args = map(lambda x: float(x), sys.argv[1:])
    print(sum(args))