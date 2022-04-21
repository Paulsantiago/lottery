from scripts.helpful_scripts import getAccount,getContract
from brownie import Lottery,network,config
def deploy_lottery():
    account = getAccount()
    #deploy_lottery(id="freecodecamp-account")
    lottery=Lottery.deploy(
        getContract("eth_usd_price_feed").address,
        getContract("vrf_coordinator").address,
        getContract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed lottery!!")
    return lottery

def main():
    deploy_lottery()