#!"d:\santhosh\office\accelerate\python - webapp\sizingautomation\sa_venv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'nose2==0.7.4','console_scripts','nose2-3.7'
__requires__ = 'nose2==0.7.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('nose2==0.7.4', 'console_scripts', 'nose2-3.7')()
    )
