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