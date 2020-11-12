import sys
import os
import subprocess
from .environment import VenvController
def main():

    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] == 'create':
            if len(args) == 2:
                venv = VenvController()
                venv.create(args[1])
                venv.activate()
                subprocess.call('pip install flask', shell=True)
            else:
                print('Project name required.')
        elif args[0] == 'pip':
            if len(args) > 1:
                venv = VenvController()
                
                # Returns true after activation
                if venv.activate():
                    subprocess.call(' '.join(args), shell=True)
                else:
                    print('Project must be created before using pip.')
            else:
                print('pip requires arguments')
        
        else:
            print('Invalid Command.')
    else:
        print('Invalid command')

   
if __name__ == '__main__':
    main()
