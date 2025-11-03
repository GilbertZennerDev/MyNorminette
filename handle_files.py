def readfile(filename):
    try: return open(filename, 'r').read().splitlines()
    except Exception as e:
        print(e); exit()