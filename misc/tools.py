import os
import yollor
import sys

def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def sair():
    sys.exit(os.system(f'cls' if os.name == 'nt' else 'clear'))
