import os


class Markov():
    def __init__(self, path=''):
        path = os.path.join(os.getcwd(), path)
        if os.path.exists(path):
            with open(path) as txt:
                self.txt = txt.read()
        else:
            self.txt = ''
