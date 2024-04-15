"""
Hometask 21 Bank card operation.

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
        self._balance = balance
        self.__card_num = self.get_card_number
        self._exp_date = self.exp_date()
        self._card_pin = 1111
        self._card_cvv = self.card_cvv()

    @staticmethod
    def get_card_number():
        """secret_card = f"{'*' * 12}{card[-4:]}."""
        """card = str(random.randint(1000000000000000, 9999999999999999))
        it's also works."""
        """card = str(random.randint(10 ** 15, (10 ** 16) - 1))"""
        """f"{'*' * 12}{card[-4:]}" """
        return str(random.randint(10 ** 15, (10 ** 16) - 1))

    @staticmethod
    def exp_date():
        """Find exp date."""
        today = datetime.date.today()
        exp_month = today.month
        exp_year = int(str(today.year + 4)[2:])
        return f'{exp_month:02d}/{exp_year}'

    @staticmethod
    def card_cvv():
        """Find random cvv code."""
        return random.randint(100, 999)

    @property
    def cvv(self):
        """Getter."""
        return self._card_cvv

    @cvv.setter
    def cvv(self, value):
        """Setter."""
        self._card_cvv = value

    @property
    def pin(self):
        """Getter."""
        return self._card_pin

    @pin.setter
    def pin(self, value):
        """Setter."""
        self._card_pin = value

    @property
    def ex_date(self):
        """Getter."""
        return self._exp_date

    @ex_date.setter
    def ex_date(self, value):
        """Setter."""
        self._exp_date = value

    @classmethod
    def get_account_info(cls):
        """Bank account."""
        return f'Bank is {cls.bank}'

    @classmethod
    def get_card_info(cls):
        """Card type."""
        return f"Card's type is {cls.card}"

    @staticmethod
    def verification_pin(card_pin, enter_pin):
        """Check pin code."""
        if card_pin != enter_pin:
            raise ValueError('Incorrect PIN code')
        else:
            print('Entered PIN code is correct')

    def transfer_money(self, balance, enter_pin, amount_transf):
        """Make transfer money."""
        self.verification_pin(self._card_pin, enter_pin)
        new_balance = balance - amount_transf
        if self._balance <= amount_transf:
            print("You don't have enough money")
        else:
            return new_balance

    def top_up(self, amount):
        """Make top up money with ATM."""
        return self._balance + amount

    def transfer_from_card1_to_card2(self, amount, enter_pin):
        """Make transfer money from card to card."""
        self.verification_pin(self._card_pin, enter_pin)
        bal_card1 = card1._balance - amount
        bal_card2 = card2._balance + amount
        return bal_card1, bal_card2

    def __str__(self):
        """Make info about card."""
        card_num = self.get_card_number()
        hide_numbers = '*' * (len(card_num) - 4)
        last_numbers = card_num[-4:]
        return f'About card for owner:\n' \
               f'Card owner is {self.name} {self.surname}\n' \
               f'Number Card is {hide_numbers + last_numbers}\n' \
               f'Balance is {self._balance}\n' \
               f'Expired date is {self._exp_date}\n' \
               f'CVV is {self._card_cvv}\n' \


    @property
    def balance(self):
        """Balance."""
        return self._balance


if __name__ == '__main__':
    card1 = BankCard(name='Lorenzo', surname='Gonzales', balance=3000)
    card2 = BankCard(name='Carmen', surname='Perez', balance=200)
    print(card1)
    print(card2)
    print('------' * 10)
    top_up_card = card1.top_up(100)
    print(f'This card was top up for 100 '
          f'and the balance now is {top_up_card}$')
    print('------' * 10)
    transfer_operation = card1.transfer_money(card1.balance,
                                              enter_pin=1111, amount_transf=50)
    print(f' After transfer your account balance is {transfer_operation}$')
    print('------' * 10)
    trans = card1.transfer_from_card1_to_card2(250, enter_pin=1111)
    print(f'After transfer money from card1 to card2 '
          f'the the rest of money on this cards is {trans}')
