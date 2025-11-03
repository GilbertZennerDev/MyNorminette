from helpers import *

def mightbefunctiondec(line):
    ctypes = ['int', 'float', 'double', 'bool', 'void']
    splitted = line.split()
    return len(splitted) and splitted[0] in ctypes and allinline(splitted[1], *'()')

def tab_function_name(line):
    if not mightbefunctiondec(line): return True
    needed = '()\t'
    forbidden = ' '
    return allinline(line, *needed) and notinline(*forbidden)