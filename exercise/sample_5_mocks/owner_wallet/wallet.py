class InsufficientAmount(Exception):
    pass


class Wallet:

    def __init__(self, amount=0):
        self._balance = amount

    def _validate_operation(self, spending):
        if self._balance < spending:
            raise InsufficientAmount(f'Spending {spending} is greater then {self._balance} balance')

    def add_cash(self, cash):
        self._balance += cash

    def spend_cash(self, spending):
        self._validate_operation(spending)
        self._balance -= spending

        # if self._balance >= spending:
        #     self._balance -= spending
        # else:
        #     raise InsufficientAmount('Spending is greater then our balance')
        #

    def get_balance(self):
        return self._balance
