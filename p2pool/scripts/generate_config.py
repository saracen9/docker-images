import os
import random
import string
from helpers import mkdir_p

def random_password(length=64):
    available_chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    password = ''

    for i in range(length):
        random_seed = random.SystemRandom(os.urandom(i))
        character = random_seed.choice(available_chars)
        password = password + character

    return password

def create_config(path, port=None):
    mkdir_p(os.path.dirname(path))

    lines = []
    lines.append("rpcuser=p2pool")
    lines.append("rpcpassword={0}".format(random_password()))
    if port:
        lines.append("port={0}".format(port))

    with open(path, 'w') as f:
        f.write('\n'.join(lines))

if __name__ == ('__main__'):
    create_config(os.path.join(os.getcwd(), 'test.conf'))
