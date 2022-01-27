from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENT = [
    "ganache",
    "local-ganache",
    "development",
    "hardhat",
    "mainnet-fork",
    "mainnet-fork-dev",
]


def get_account(id=None, index=None):
    if id:
        return accounts(id)
    if index:
        return accounts(index)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    return None
