import sys
from helpers import *
from handle_files import *
from func_dec import *
from last_line_empty import *

file = readfile("test.c")

def print_errors(errors, filename):
    if len(errors):
        print("Error!")
        for line in errors: print(line)
        exit()
    print(filename, ":OK")

def iterate_file(file):
    errors = []
    for i, line in enumerate(file):
        if not tab_function_name(line): errors.append(f'line: {i}: space before function name')
    print_errors(errors, "test.c")

iterate_file(file)

#if __name__ == "__main__": iterate_file(file):