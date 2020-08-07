import sys,os

def setImportPathRoot(rootPath):
    fullPath = os.getcwd()+rootPath
    if not fullPath in sys.path:
        sys.path.index(fullPath)