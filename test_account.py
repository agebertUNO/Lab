from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('John')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        self.p1.deposit(300.00)
        assert self.p1.get_balance() == 300.00

    def test_withdraw(self):
        self.p1.deposit(300.00)
        self.p1.withdraw(100.00)
        assert self.p1.get_balance() == 200.00