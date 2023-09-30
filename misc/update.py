import os as MinT

def pip(package):
    MinT.system(f'pip install {package} --user -q' if MinT.name == 'nt' else f'pip install {package} -q')