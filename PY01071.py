# PY01071 - PYTHON FILE

import re

def check_file(name):
    if name[-3:].lower() == '.py':
        print('yes')
    else:
        print('no')

if __name__ == "__main__":
    name = input()
    check_file(name)

