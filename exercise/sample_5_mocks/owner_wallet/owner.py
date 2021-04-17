from exercise.sample_5_mocks.owner_wallet import wallet
from exercise.sample_5_mocks.owner_wallet.wallet import Wallet


class Owner:
    def __init__(self, first_name, last_name, wallet: Wallet):
        self.first_name = first_name
        self.last_name = last_name
        self._wallet = wallet

    # def replace_wallet(self, wallet):
    #     self._wallet = wallet
    def supply_wallet(self, cash):
        self._wallet.add_cash(cash)

    def withdraw_wallet(self, cash):
        self._wallet.spend_cash(cash)

    def check_if_can_afford(self, cash):
        return self._wallet.get_balance() >= cash


if __name__ == '__main__':
    wallet = Wallet()
    wallet.add_cash(10)
    wallet.spend_cash(5)
    print(wallet.get_balance())
    owner = Owner('Patryk', 'Wiener', wallet)
    owner.supply_wallet(10)
    owner.withdraw_wallet(10)
    new_wallet = Wallet()
    # owner.replace_wallet(new_wallet)
