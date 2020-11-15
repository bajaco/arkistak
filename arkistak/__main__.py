import os
import subprocess
import sys
import importlib
import json
from pathlib import Path
from .venv_controller import VenvController
from .parse_args import parse_args

def create(args):
    
    # Verify template
    if not os.path.exists(args[1] + '.json'):
        print(f'Template file {args[1]}.json not found!')
        sys.exit()
    
    # Initialize and activate venv
    venv = VenvController()
    venv.create(args[1])
    venv.activate()
   
    # Make application directory
    os.mkdir(args[1])

    # Load template
    with open(args[1] + '.json') as f:
        template = json.load(f)
    
    # Verify generators 
    backend_path = (Path(__file__).absolute().parent / 
            'generators' / 'backend' / 
            (template['backend']['framework'] + '.py'))
    if not os.path.exists(str(backend_path)):
        print(f'Backend generator {template["backend"]["framework"]}.py not found!')
        sys.exit()
    
    frontend_path = (Path(__file__).absolute().parent / 
            'generators' / 'frontend' / 
            (template['frontend']['framework'] + '.py'))
    if not os.path.exists(str(frontend_path)):
        print(f'Frontend generator {template["frontend"]["framework"]}.py not found!')
        sys.exit()
    

    BackendGenerator = __import__(
            f'arkistak.generators.backend.{template["backend"]["framework"]}',
            fromlist = ['']).BackendGenerator 
    backendGenerator = BackendGenerator(args[1], template)
    backendGenerator.install()
    backendGenerator.generate()


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
