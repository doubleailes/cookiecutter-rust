import subprocess
import os
import sys

try:
    # initialise git repo
    os.system("git init")
    # change current working directory
    os.chdir("docs/themes")
    # add git submodule
    os.system("git submodule add https://github.com/aaranxu/adidoks.git")
    # gently exit
    sys.exit(0)
except Exception as err:
    print(err)
    # if error exit with code 1
    sys.exit(1)
