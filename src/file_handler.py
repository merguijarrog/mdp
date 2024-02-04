def readFile(file):
    file = open(file,'r')
    with file as f:
        lines= f.readlines()
    file.close()
    return lines