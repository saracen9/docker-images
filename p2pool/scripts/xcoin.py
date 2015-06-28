import subprocess
import time

p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()

def compile_from_source(coin, root_dir):
    # Clone the repo
    print("Cloning the {0} repo".format(coin))
    cmd  = """git clone {repo}""".format(repo=coin['git'])
    p = subprocess.Popen(cmd, shell=True)  #, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
