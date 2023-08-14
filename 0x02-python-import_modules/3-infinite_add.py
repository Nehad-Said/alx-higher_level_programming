#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    count = len(sys.argv) - 1
    sum = 0
    for i in range(count):
        argument = int(sys.argv[i + 1])
        sum += argument
        print("{:d}".format(sum))
