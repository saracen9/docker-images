import subprocess
import time
import os
from helpers import mkdir_p

p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()

def compile_from_source(coin, root_dir, name):
    # Check root exists
    mkdir_p(root_dir)

    # Clone the repo
    print("Cloning the {0} repo".format(coin))
    os.chdir(root_dir)
    cmd  = """git clone {repo}""".format(repo=coin['git'])
    p = subprocess.Popen(cmd, shell=True)  #, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Compile
    flags = [
        '--without-gui',
        '--enable-upnp-default',
        '--disable-wallet',
    ]
    os.chdir(name)
    cmd = "./autogen.sh"
    p = subprocess.Popen(cmd, shell=True)

    cmd = ["./configure"]
    [cmd.append(flag) for flag in flags]
    p = subprocess.Popen(cmd, shell=True)

    cmd = "make"
    p = subprocess.Popen(cmd, shell=True)

    cmd = "strip src/{0}d".format(name)
    p = subprocess.Popen(cmd, shell=True

    cmd = "make install"
    p = subprocess.Popen(cmd, shell=True)
