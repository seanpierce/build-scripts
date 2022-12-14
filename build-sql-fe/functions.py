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
build_script_prod = CONFIG.get('env', 'build-prod')

def compile(path: str, is_prod: bool) -> None:
    cmd = fr'"%ProgramFiles%\Git\bin\bash.exe" -c "cd {path}; yarn; {build_script_prod if is_prod else build_script}"'
    r = subprocess.Popen(cmd, shell=True)
    r.wait()
    r.kill

def print_name(process_name: str, is_prod: bool) -> str:
    if is_prod:
        return f'Production {process_name}'
    else:
        return process_name

def build_app(is_prod: bool) -> None:
    print('=====================')
    name = print_name('App', is_prod)
    print(f'Building {name}...')
    compile(app, is_prod)
    print(f'Building {name} Complete!')

def build_app_pro(is_prod: bool) -> None:
    print('=====================')
    name = print_name('App-Pro', is_prod)
    print(f'Building {name}...')
    compile(app_pro, is_prod)
    print(f'Building {name} Complete!')

def build_app_auth(is_prod: bool) -> None:
    print('=====================')
    name = print_name('App-Auth', is_prod)
    print(f'Building {name}...')
    compile(app_auth, is_prod)
    print(f'Building {name} Complete!')