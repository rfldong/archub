import os

def prog(filepath):
    return 'archub {}'.format(os.path.basename(filepath)[:-3])
