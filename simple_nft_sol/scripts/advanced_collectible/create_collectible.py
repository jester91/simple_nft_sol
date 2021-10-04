#!/usr/bin/python3
from brownie import PrimaryCollectible, accounts, config
from scripts.helpful_scripts import get_breed, fund_with_link
import time


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    primary_collectible = PrimaryCollectible[len(PrimaryCollectible) - 1]
    fund_with_link(primary_collectible.address)
    transaction = primary_collectible.createCollectible("None", {"from": dev})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    time.sleep(35)
    requestId = transaction.events["requestedCollectible"]["requestId"]
    token_id = primary_collectible.requestIdToTokenId(requestId)
    breed = get_breed(primary_collectible.tokenIdToBreed(token_id))
    print("Zeus breed of tokenId {} is {}".format(token_id, breed))