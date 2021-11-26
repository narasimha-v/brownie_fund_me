from brownie import accounts, exceptions  # type: ignore
from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx_1 = fund_me.fund({"from": account, "value": entrance_fee})
    tx_1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx_2 = fund_me.withdraw({"from": account})
    tx_2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    try:
        fund_me.withdraw({"from": bad_actor})
    except exceptions.VirtualMachineError:
        pass
