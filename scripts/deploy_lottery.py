from scripts.helpful_scripts import getAccount,getContract
from brownie import Lottery
def deploy_lottery():
    account = getAccount()
    deploy_lottery(id="freecodecamp-account")
    lottery=Lottery.deploy(
        get_contract("eth_usd_price_feed").address
    )

def main():