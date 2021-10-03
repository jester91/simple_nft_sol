#!/usr/bin/python3
import os
from brownie import BasicCollectible, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    #basic_Collectible = BasicCollectible[len(BasicCollectible)-1]
    #print(basic_Collectible.ownerof(0))
    BasicCollectible.deploy({"from": dev})
