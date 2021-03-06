
from brownie import Lottery, accounts,config,network
from web3 import Web3
def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from":account},
    )
    print("entrance Fee: ",lottery.getEntranceFee())
    assert lottery.getEntranceFee()>Web3.toWei(0.016,"ether") # at this moment approximatly
    assert lottery.getEntranceFee()<Web3.toWei(0.018,"ether")





