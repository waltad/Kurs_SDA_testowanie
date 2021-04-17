import pytest

from exercise.sample_2_wallet.sample_2_wallet.wallet import Wallet, InsufficientAmount


class TestWallet:
    def setup_method(self):
        self.empty_wallet = Wallet()
        self.wallet = Wallet(20)

    def test_default_initial_amount(self):
        expected = 0
        actual = self.empty_wallet.get_balance()
        assert actual == expected

    def test_setting_initial_amount(self):
        expected = 20
        actual = self.wallet.get_balance()
        assert actual == expected

    def test_spend_cash(self):
        expected = 10
        self.wallet.spend_cash(10)
        actual = self.wallet.get_balance()
        assert actual == expected

    def test_add_cash(self):
        expected = 30
        self.wallet.add_cash(10)
        actual = self.wallet.get_balance()
        assert actual == expected

    def test_spend_cash_raises_exception_on_insufficient_amount(self):
        with pytest.raises(InsufficientAmount):
            self.empty_wallet.spend_cash(10)

    @pytest.mark.parametrize('earned,spending,expected', [
        [20, 10, 10],
        [30, 30, 0],
    ])
    def test_transactions(self, earned, spending, expected):
        self.empty_wallet.add_cash(earned)
        self.empty_wallet.spend_cash(spending)
        actual = self.empty_wallet.get_balance()
        assert actual == expected
