#!/usr/bin/env python3
from divison import safe_print_division
a = 12
b = 2


def main():
    result = safe_print_division(a, b)
    print("Inside result: {:d} / {:d} = {:d}".format(a, b, result))

    if __name__ == '__main__':
        main()
