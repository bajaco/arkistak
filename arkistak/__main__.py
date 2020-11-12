import sys
import subprocess
from .environment import VenvController
def main():

    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] == 'create' and len(args) == 2:
            venv = VenvController(args[1])
            venv.create()
            venv.activate()
            subprocess.call('pip install flask', shell=True)
        else:
            print('Project name required.')
    else:
        print('Invalid command')

   
if __name__ == '__main__':
    main()
