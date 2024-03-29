from misc import update as UpMyPika
import os
UpMyPika.pip(package="yollor")
from misc import loading as Carregante
from misc import prints as VanGogh
import random as Randolinha
import argparse
from yollor import *
from misc import create as TheCreature
from misc import tools as FerramentaDePedrero

parser = argparse.ArgumentParser(description='YProjects Manager')
parser.add_argument('--web', '-w', action='store_true', help='Web Mode')
parser.add_argument('--python-terminal', '-pt', action='store_true', help='Python 4 Terminal mode')
parser.add_argument('-n', '--name', default='Y-Project', help='Project name')
args = parser.parse_args()
ProjectName = str(args.name)

if args.web:

    Carregante.start(texto="Starting your project with TailwindCSS and TypeScript", NV=2)

    indexH = """<!DOCTYPE html>
<html>
<head>
    <title>YProjs Generator</title>
    <link rel="stylesheet" href="assets/global.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="assets/tailwind.config.js"></script>
</head>
<body class="bg-zinc-950">
</body>
</html>"""
    TheCreature.create_archive(content=indexH, arqName="index", ext="html", ProjPath=f"{ProjectName}")
    
    globalC = """@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
"""
    TheCreature.create_archive(content=globalC, arqName="global", ext="css", ProjPath=f"{ProjectName}/assets")

    serverP = """import http.server
import socketserver
import random
import os
os.system('pip install yollor')
from yollor import *

tagn1 = f"{c.cyan('[')}{c.yellow('1')}{c.cyan(']')}"
tagn2 = f"{c.cyan('[')}{c.yellow('2')}{c.cyan(']')}"
hashtag = f"{c.cyan('[')}{c.yellow('#')}{c.cyan(']')}"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        request_info = f"{c.yellow('<--')} {c.yellow('|')} {c.cyan('Request Code')} {c.yellow('|')} {c.purple('IP')} {c.yellow('|')} {c.yellow('-->')}"
        
        request_line = f"{c.yellow('<--')} | {c.cyan(format % args)} | {c.green(self.headers.get('User-Agent', 'Unknown').split('(')[0].strip())} | {c.purple(self.client_address[0])} | {c.yellow('-->')}"
        print(request_line)


port = 5590

handler = CustomHTTPRequestHandler 

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Server running at http://localhost:{port}")
    httpd.serve_forever()
"""
    TheCreature.create_archive(content=serverP, arqName="server", ext="py", ProjPath=f"{ProjectName}")
    
    indexTSX = """// free for use
// https://github.com/Yyax13/ypg

// Insert your code here"""
    TheCreature.create_archive(content=indexTSX, arqName="app", ext="tsx", ProjPath=f"{ProjectName}/assets")
   
    tconfigJ = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}"""
    TheCreature.create_archive(content=tconfigJ, arqName="tailwind.config", ext="js", ProjPath=f"{ProjectName}/assets")
    
    readmeM = """# YPG

> YProjects Gerenciator (Linux only)

## How to use

clone the repo or download the project zip archive

go to the directory where ypg has been install

run this command on terminal: `sudo bash install.sh` (needs sudo)

## Web Mode
to create the web project, run ```ypg -w -n [name]``` or ```ypg --web -n [name]```

to run the auto-included non-php server, run ```python server.py``` in terminal/cmd (on the project directory), and the server will start in <a href="http://localhost:5590">http://localhost:5590</a>

## Python terminal-side mode
to create the project, run ```ypg -pt -n [name]``` or ```ypg --python-terminal -n [name]```

to run the python terminal-side project, run ```python main.py``` in terminal/cmd (on the project directory), and the server will start

## LICENSE
We Use the [[MIT LICENSE](LICENSE)](https://github.com/Yyax13/ypg/blob/main/LICENSE)

## Support
I'm the support, contact-me on discord or telegram

- discord: `solo.yyax`
- telegram: [Yyax13](https://t.me/Yyax13)




---

© 2023 Lucas de Moraes "Yyax" Claro"""
    TheCreature.create_archive(content=readmeM, arqName="README", ext="md", ProjPath=f"{ProjectName}")

elif args.python_terminal:

    Carregante.start(texto="Starting a python (terminal-side) project with prmTools (pre-made tools)", NV=2)
    mainP = """from misc import update
update.pip(package="yollor") #Do not delete these lines, they are the requeriments installer for the prmTools"""
    TheCreature.create_archive(content=mainP, arqName="main", ext="py", ProjPath=f"{ProjectName}")

    updtP = """import os
import subprocess

def pip(package):
    try:
        subprocess.check_output(["pip", "show", package])
        print(f'{package} already installed')
    except subprocess.CalledProcessError:
        os.system(f'pip install {package}')
        print(f'Done')
"""
    TheCreature.create_archive(content=updtP, arqName="update", ext="py", ProjPath=f"{ProjectName}/misc")

    loadP = """import os
from yollor import *
import time as SurubaTemporal

frame1 = '|'
frame2 = '/'
frame3 = '-'
frame4 = "\ "

def start(texto, NV):
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(NV):
        clear()
        print(f"{c.cyan(texto)} - {c.red(frame1)}")
        SurubaTemporal.sleep(0.3)
        clear()
        print(f"{c.cyan(texto)} - {c.red(frame2)}")
        SurubaTemporal.sleep(0.3)
        clear()
        print(f"{c.cyan(texto)} - {c.red(frame3)}")
        SurubaTemporal.sleep(0.3)
        clear()
        print(f"{c.cyan(texto)} - {c.red(frame4)}")
        SurubaTemporal.sleep(0.3)
        clear()
"""
    TheCreature.create_archive(content=loadP, arqName="loading", ext="py", ProjPath=f"{ProjectName}/misc")

    toolsP = """import os
import yollor
import sys

def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def sair():
    sys.exit(os.system('cls' if os.name == 'nt' else 'clear'))
"""
    TheCreature.create_archive(content=toolsP, arqName="tools", ext="py", ProjPath=f"{ProjectName}/misc")

    readmeM = """# YPG

> YProjects Gerenciator (Linux only)

## How to use

clone the repo or download the project zip archive

go to the directory where ypg has been install

run this command on terminal: `sudo bash install.sh` (needs sudo)

## Web Mode
to create the web project, run ```ypg -w -n [name]``` or ```ypg --web -n [name]```

to run the auto-included non-php server, run ```python server.py``` in terminal/cmd (on the project directory), and the server will start in <a href="http://localhost:5590">http://localhost:5590</a>

## Python terminal-side mode
to create the project, run ```ypg -pt -n [name]``` or ```ypg --python-terminal -n [name]```

to run the python terminal-side project, run ```python main.py``` in terminal/cmd (on the project directory), and the server will start

## LICENSE
We Use the [[MIT LICENSE](LICENSE)](https://github.com/Yyax13/ypg/blob/main/LICENSE)

## Support
I'm the support, contact-me on discord or telegram

- discord: `solo.yyax`
- telegram: [Yyax13](https://t.me/Yyax13)




---

© 2023 Lucas de Moraes "Yyax" Claro"""
    TheCreature.create_archive(content=readmeM, arqName="README", ext="md", ProjPath=f"{ProjectName}")

if args.web and args.python_terminal:
    exit("Use only one argument")
