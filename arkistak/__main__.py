import subprocess
import venv
import os
import sys
import site
from pathlib import Path

def main():
    #Create venv
    venv_name = 'venv'
    bin_dir = str(Path().absolute() / (venv_name + '/bin'))
    base = str(Path().absolute() / venv_name)
    venv.create(base, prompt="arkistak-project", with_pip=True)
    
    # Activate new environment. refer to 
    # https://github.com/pypa/virtualenv/blob/main/src/virtualenv/activation/python/activate_this.py
    os.environ['PATH'] = os.pathsep.join([bin_dir] + os.environ.get("PATH", "").split(os.pathsep))
    os.environ['VIRTUAL_ENV'] = base
    prev_length = len(sys.path)
    for lib in "__LIB_FOLDERS__".split(os.pathsep):
        path = os.path.realpath(os.path.join(bin_dir, lib))
        site.addsitedir(path)

    sys.path[:] = sys.path[prev_length:] + sys.path[0:prev_length]
    sys.real_prefix = sys.prefix
    sys.prefix = base 
     
    # Install a module for test
    subprocess.call('pip install wikipedia', shell=True)

if __name__ == '__main__':
    main()
