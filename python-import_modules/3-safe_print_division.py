#!/usr/bin/env python3
def safe_print_division(a, b):
    try:
        answer = a/b
    except ZeroDivisionError:
        result = "None"
    finally:
        print("Inside result: {}", format(answer))
        return answer
