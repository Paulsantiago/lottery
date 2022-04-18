#from os import fork
from brownie import accounts, network , config, MockV3Aggregator,Contract,VRFCoordinatorMock
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
INITIAL_VALUE =  200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS =["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-dev-fork,mainnet-fork"]
def getAccount(index=None, id=None):
    #accounts[0]
    #accounts.add("env")
    #accounts.load("id")
    if(index):
        return accounts[index]
    if(id):
        return accounts.load(id)
    ######################################################
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or
        network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        print("getting account from ganache")
        return accounts[0]
    ##################################
    print("getting account from wallet")
    return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is { network.show_active() }")
    print("Deploying mocks ... ")
    account =getAccount()
    MockV3Aggregator.deploy(
        DECIMALS,INITIAL_VALUE,{"from":account}
    )
    print("Mocks Deployed!")
  

contract_to_mock = {
    "eth_usd_price_feed":MockV3Aggregator,
    "vrf_coordinator": VRFCoordinatorMock}
def getContract(contract_name):
    """
    This funtion will grab the contract addresses from the brownie config 
    if defined optherwise it will dweploy the mock version of the contract , and
    return the mock contract

    Args :
        contract_name(strings)
    Returns 
        brownie.networks,contrac.ProjectContract: the most recenltly deployerd verision
    of this contract
    MockV3Agregator[-1]
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type)<=0:
            #MockV3Agregator.lenght
            deploy_mocks()
        contract = contract_type[-1] # is the same that MockV3Agregator[-1]
    else:
        contract_address = config["config"][network.show_active()][contract_name]
        #address
        #abi
        contract = Contract.from_abi(
            contract_type._name,contract_address,contract_type.abi
        )
    return contract
