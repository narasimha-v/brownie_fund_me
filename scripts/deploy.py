from brownie import FundMe, config, network  # type: ignore

from scripts.helpful_scripts import (
    deploy_mock_and_get_address,
    get_account,
    LOCAL_BLOCKCHSIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHSIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        price_feed_address = deploy_mock_and_get_address()

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
