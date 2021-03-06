import venv
import os
import sys
import site
from pathlib import Path

class VenvController:
    
    def __init__(self): 
        self.venv_name = 'venv'
        self.base = str(Path().absolute() / self.venv_name)
        self.bin_dir = str(Path().absolute() / self.venv_name / 'bin')
    
    def create(self, project_name):
        # Create venv
        venv.create(
                self.base,
                prompt=f'arkistak-{project_name}',
                with_pip=True
        )

        
    def activate(self):
        
        # Only activating if venv created
        if not os.path.exists(self.base):
            return False
        
        # Activate new environment. refer to 
        # https://github.com/pypa/virtualenv/blob/main
        # /src/virtualenv/activation/python/activate_this.py
        os.environ['PATH'] = os.pathsep.join([self.bin_dir] + 
                os.environ.get("PATH", "").split(os.pathsep))
        os.environ['VIRTUAL_ENV'] = self.base
        prev_length = len(sys.path)
        for lib in "__LIB_FOLDERS__".split(os.pathsep):
            path = os.path.realpath(os.path.join(self.bin_dir, lib))
            site.addsitedir(path)

        sys.path[:] = sys.path[prev_length:] + sys.path[0:prev_length]
        sys.real_prefix = sys.prefix
        sys.prefix = self.base
        return True

