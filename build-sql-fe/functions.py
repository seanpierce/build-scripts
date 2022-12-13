import configparser
import os
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
CONFIG = configparser.RawConfigParser()
CONFIG.read(f'{dir_path}/env.ini')

root = CONFIG.get('env', 'root')
app = f"{root}App"
app_pro = f"{root}App-Pro"
app_auth = f"{root}App-Auth"
build_script = CONFIG.get('env', 'build')

def compile(path: str) -> None:
    cmd = fr'"%ProgramFiles%\Git\bin\bash.exe" -c "cd {path}; yarn; {build_script}"'
    r = subprocess.Popen(cmd, shell=True)
    r.wait()
    r.kill

def build_app() -> None:
    print('Building App...')
    compile(app)
    print('Building App Complete!')

def build_app_pro() -> None:
    print('Building App-Pro...')
    compile(app_pro)
    print('Building App-Pro Complete!')

def build_app_auth() -> None:
    print('Building App...')
    compile(app_auth)
    print('Building App-Auth Complete!')