import subprocess
import os

class BackendGenerator:
    def __init__(self, name, template):
        self.name = name
        self.template = template

    def install(self):
        requirements = [
                'flask',
                'flask-cors',
                'Flask-SQLAlchemy',
                'Flask-Migrate'
        ]
        subprocess.call('pip install --upgrade pip', shell=True)
        for r in requirements:
            subprocess.call(f'pip install {r}', shell=True)

    def generate(self):
        os.chdir(self.name)
        os.mkdir('backend')


