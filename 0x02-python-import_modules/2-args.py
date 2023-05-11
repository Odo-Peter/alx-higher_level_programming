#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    i = len(argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} arguments.".format(i))
    else:
        print("{} arguments.".format(i))

    if len(argv) >= 1:
        for index, args in enumerate(argv):
            if index != 0:
                print("{}: {}.".format(index, args))
