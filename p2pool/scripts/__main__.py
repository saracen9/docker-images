from generate_config import create_config
import os
from os.path import expanduser

HOME = expanduser("~")

create_config(os.path.join(HOME, '.bitcoin', 'bitcoin.conf'))
create_config(os.path.join(HOME, '.litecoin', 'litecoin.conf'))
