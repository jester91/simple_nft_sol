#!/usr/bin/python3
from brownie import PrimaryCollectible, accounts, network, config
from scripts.helpful_scripts import fund_with_link
import os


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    # publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False # Currently having an issue with this
    #publish_source = False
    primary_collectible = PrimaryCollectible.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
        #publish_source=publish_source,
    )
    fund_with_link(primary_collectible.address)
    return primary_collectible