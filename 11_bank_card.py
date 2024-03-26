"""

Hometask 14 lambda.

# write class for bank card.
# Class should reflect card lifecycle, card operations etc.
# use CVV, PIN, Name, Surname , end date, card_num as initial params
# class should have in addition to common logic some class attributes,
# as minimum one classmethod and
# as minimum  one staticmethod, two or more getters/setters,
# __str_ magic method
# do not forget about block

"""

import datetime
import random


class BankCard:
    """Make class."""

    bank = 'Best Bank'
    card = 'VISA'

    def __init__(self, name, surname, balance):
        """Make init."""
        self.name = name
        self.surname = surname
        self.balance = balance
        self.card_num = self.card_number
        self.exp_date = self.exp_date()
        self.card_pin = self.card_pin()
        self.card_cvv = self.card_cvv()

    @staticmethod
    def card_number():
        """secret_card = f"{'*' * 12}{card[-4:]}."""
        """card = str(random.randint(1000000000000000, 9999999999999999))
        it's also works."""
        card = str(random.randint(10 ** 15, (10 ** 16) - 1))
        return f"{'*' * 12}{card[-4:]}"

    @staticmethod
    def exp_date():
        """Find exp date."""
        today = datetime.date.today()
        exp_month = today.month
        exp_year = int(str(today.year + 4)[2:])
        return f'{exp_month:02d}/{exp_year}'

    @staticmethod
    def card_pin():
        """Make static method."""
        return random.randint(0000, 9999)

    @staticmethod
    def card_cvv():
        """Find random cvv code."""
        return random.randint(100, 999)

    @classmethod
    def get_account_info(cls):
        """Bank account."""
        return f'Bank is {cls.bank}'

    @classmethod
    def get_card_info(cls):
        """Card type."""
        return f"Card's type is {cls.card}"

    @classmethod
    def balance(cls):
        """Show balance."""
        return cls.balance

    def transfer_money(self, balance):
        """Make transfer money from ATM."""
        amount_transfer = float(input('Please enter transfer amount: '))
        new_balance = balance - amount_transfer
        if self.balance < amount_transfer:
            print("You don't have enough money")
        else:
            print(new_balance)
            return new_balance

    def top_up(self, amount):
        """Make top up money with ATM."""
        return self.balance + amount

    @staticmethod
    def transfer_from_card1_to_card2(amount=250):
        """Make transfer money from card to card."""
        bal_card1 = card1.balance - amount
        bal_card2 = card2.balance + amount
        return bal_card1, bal_card2

    def __str__(self):
        """Make info about card."""
        return f'About card for owner:\n'\
               f'Card owner is {self.name} {self.surname}\n' \
               f'Number Card is {self.card_number()}\n' \
               f'Balance is {self.balance}\n' \
               f'Expired date is {self.exp_date}\n' \
               f'CVV is {self.card_cvv}\n' \



if __name__ == '__main__':
    card1 = BankCard(name='Lorenzo', surname='Gonzales', balance=3000)
    card2 = BankCard(name='Carmen', surname='Perez', balance=200)
    print(card1)
    print(card2)
    print('------' * 10)
    top_up_card = card1.top_up(amount=100)
    print(f'This card was top up for 100 '
          f'and the balance now is {top_up_card}$')
    print('------' * 10)
    transfer_operation = card1.transfer_money(card1.balance)
    print(f' After transfer your account balance is {transfer_operation}$')
    print('------' * 10)
    trans = card1.transfer_from_card1_to_card2()
    print(f'After transfer money from card1 to card2 '
          f'the the rest of money on this cards is {trans}')
