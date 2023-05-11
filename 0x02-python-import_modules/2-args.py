#!/usr/bin/python3

if __name__ == "__main_":
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) > 1:
        for i, args in enumerate(argv):
            if(i != 0):
                print(f"{i}: {argv[i]}")
