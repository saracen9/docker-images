from generate_config import create_config
from xcoin import compile_from_source
import os
from os.path import expanduser

HOME = expanduser("~")

'''
Coins and Ports:
    8333/tcp  # bitcoin peer to peer
    10333/tcp # litecoin peer to peer
    8334/tcp  # namecoin peer to peer
    8337/tcp  # ixcoin peer to peer
    6334/tcp  # devcoin peer to peer
    7337/tcp  # i0coin peer to peer
    8492/tcp  # fusioncoin peer to peer
    9333/tcp  # P2pool peer to peer
    9332/tcp  # P2Pool connections and Web interface
'''
COINS = {
    'bitcoin': {
        'git': None,
        'port': 8333,
    },
    'litecoin': {
        'git': 'git://github.com/litecoin-project/litecoin.git',
        'port': 10333,
    },
    'namecoin': {
        'git': 'git://github.com/namecoin/namecoin.git',
        'port': 8334,
    },
    'devcoin': {
        'git': 'https://github.com/coinzen/devcoin.git',
        'port': 6334,
    },
    'ixcoin': {
        'git': 'git://github.com/ixcoin/ixcoin.git',
        'port': 8337,
    },
    'iocoin': {
        'git': 'git://github.com/ixcoin/ixcoin.git',
        'port': 7337,
    },
}

for coin in COINS:
    print coin, COINS[coin]
    create_config(os.path.join(HOME, '.{0}'.format(coin), '{0}.conf'.format(coin)),
        port=COINS[coin]['port'])
    if coin != 'bitcoin':
        compile_from_source(COINS[coin], HOME)
