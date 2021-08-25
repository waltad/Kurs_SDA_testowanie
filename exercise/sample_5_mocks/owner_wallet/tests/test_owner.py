from unittest.mock import MagicMock

from exercise.sample_5_mocks.owner_wallet.owner import Owner


class TestOwner:
    FIRST_NAME = 'Grzegorz'
    LAST_NAME = 'Brzeczyszczykiewicz'

    def setup_method(self):
        self.wallet_mock = MagicMock()
        self.owner = Owner(self.FIRST_NAME, self.LAST_NAME, self.wallet_mock)

    def test_owner_first_name(self):
        expected = self.FIRST_NAME
        actual = self.owner.first_name
        assert actual == expected

    def test_owner_last_name(self):
        expected = self.LAST_NAME
        actual = self.owner.last_name
        assert actual == expected

    def test_owner_supply_wallet(self):
        amount = 20
        self.owner.supply_wallet(amount)
        self.wallet_mock.add_cash.assert_called_once_with(amount)

    def test_owner_withdraw_wallet(self):
        amount = 20
        self.owner.withdraw_wallet(amount)
        self.wallet_mock.spend_cash.assert_called_once_with(amount)

    def test_owner_check_if_can_afford_true(self):
        amount = 20
        self.owner.check_if_can_afford_true(amount)
        self.wallet_mock.get_balance.assert_called_once_with(amount)

    def test_owner_check_if_can_afford_false(self):
        pass
