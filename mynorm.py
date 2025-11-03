import sys

def readfile(filename):
    try: return open(filename, 'r').read().splitlines()
    except Exception as e:
        print(e); exit()

file = readfile("test.c")

def last_line_empty(file):
    return (file[-1] == '}')

def oneinline(line, *stuff):
    for el in stuff:
        if el in line: return True
    return False

def allinline(line, *stuff):
    for el in stuff:
        if el not in line: return False
    return True

def notinline(line, *stuff):
    for el in stuff:
        if el in line: return False
    return True

'''
I need to check whether a specific line is a (valid) function declaration
best: check by check
first check for ctype followed by name followed by ()
'''

def mightbefunctiondec(line):
    ctypes = ['int', 'float', 'double', 'bool', 'void']
    splitted = line.split()
    #if splitted[0] in ctypes:# and len(splitted) > 1 and allinline(splitted[1], *'()'):
    #    return True
    print(splitted)
    return False
    '''needed = '()'
    spacetab = ' \t'
    if not allinline(line, *needed) or not oneinline(line, *spacetab): return False
    splitted = line.replace(' ', '\t').split('\t')
    if splitted[0] not in ctypes: return False
    #print('might be func dec:', line)
    return True'''

def tab_function_name(line):
    needed = '()\t'
    forbidden = ' '
    return allinline(line, *needed) and notinline(*forbidden)

def iterate_file(file):
    errors = False
    for i, line in enumerate(file):
        if mightbefunctiondec(line):
            if not tab_function_name(line): print('line:', i, ':space before function name'); errors = True
    if errors: print("Error!"); exit()
    print("test.c:", "OK")

iterate_file(file)

#if __name__ == "__main__": iterate_file(file):