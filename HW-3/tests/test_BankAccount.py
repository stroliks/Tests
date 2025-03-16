

from main import BankAccount

import pytest

@pytest.mark.parametrize("value, expected_result",
                             [
                                 (["a"], TypeError),
                                 (-1, ValueError),
                             ])
def test_account_negativ_deposit(value, expected_result):
    acc = BankAccount()
    with pytest.raises(expected_result):
        acc.deposit(value)

@pytest.mark.parametrize("value, expected_result",
                             [
                                 (1, 1),
                                 (100, 100),
                             ])
def test_account_positive_deposit(value, expected_result):
    acc = BankAccount()
    acc.deposit(value)
    assert acc.get_balance() == expected_result

@pytest.mark.parametrize("value, expected_result",
                             [
                                 (["a"], TypeError),
                                 (-1, ValueError),
                                 (200, ValueError),
                                 (0, ValueError),
                             ])
def test_account_negativ_withdraw(value, expected_result):
    acc = BankAccount()
    with pytest.raises(expected_result):
        acc.withdraw(value)

@pytest.mark.parametrize("value, expected_result",
                             [
                                 (100, 0),
                                 (1, 99),
                             ])
def test_account_positive_withdraw(value, expected_result):
    acc = BankAccount()
    acc.set_balance(100)
    acc.withdraw(value)
    assert acc.get_balance() == expected_result