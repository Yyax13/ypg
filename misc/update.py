import os as MinT
import subprocess
def pip(package):
    try:
        subprocess.check_output(["pip", "show", package])
        print(f'O pacote {package} já está instalado.')
    except subprocess.CalledProcessError:
        os.system(f'pip install {package}')
        print(f'O pacote {package} foi instalado.')
