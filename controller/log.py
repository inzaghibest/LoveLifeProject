__author__ = 'zhxp'

class Log:
    def __init__(self, filename = ""):
        self.file = open(r'filename', 'w')
    def logAppend(self, line):
        if(self.file is None):
            return false


