import os
import subprocess
from .venv_controller import VenvController
from .parse_args import parse_args

def create(args):
    venv = VenvController()
    venv.create(args[1])
    venv.activate()
    subprocess.call('pip install flask', shell=True)

def pip(args):
    venv = VenvController()    
            
    # Returns true after successful activation
    if venv.activate():
        subprocess.call(' '.join(args), shell=True)
    else:
        print('Project must be created before using pip.')


def main():
    args = parse_args()
    if not args[0]:
        print(args[1])
    else:
        args = args[1]
        if args[0] == 'create':
            create(args)
        elif args[0] == 'pip':
            pip(args)

if __name__ == '__main__':
    main()
