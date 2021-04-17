class InsufficientAmount(Exception):
    pass


class Wallet:

    def __init__(self, amount=0):
        self._blance = amount

    def _validate_operation(self, spending):
        if spending > self._blance:
            raise InsufficientAmount(f'Spending {spending} is greater than {self._blance} our balance')

    def add_cash(self, cash):
        self._blance += cash

    def spend_cash(self, spending):
        self._validate_operation(spending)
        self._blance -= spending

    def get_balance(self):
        return self._blance