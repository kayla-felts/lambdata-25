from lambdata.wallet import Wallet
import pytest

@pytest.fixture
def empty_wallet():
    '''Returns a wallet instance with a zero ballance'''
    wallet = Wallet()
    return wallet

@pytest.fixture
def wallet():
    '''Returns wallet with balance of 20'''
    return wallet(20)



def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_ininitial_amount(wallet):
    assert wallet.balance == 20

def test_wall_add_cash(wallet):
    wallet.add_cash(100)
    assert wallet.balance == 120

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

