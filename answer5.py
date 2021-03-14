class User:
    def __init__(self, mail, name, surname):
        self.mail = mail
        self.name = name
        self.surname = surname

    def say_hello(self):
        return "User %(name)s %(surname)s says hello." % {
            "name": self.name,
            "surname": self.surname
        }

class VIPUser(User):
    def __init__(self, name, surname, mail, card_number):
        super().__init__(name, mail, surname)
        self._card_number = card_number if self._check_card_number(card_number) else None

    @staticmethod
    def _check_card_number(card_number):
        return card_number > 999 and card_number % 2 == 0

    @staticmethod
    def use_vip_card():
        pass

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number if self._check_card_number(card_number) else None


if __name__ == '__main__':
    user = VIPUser("Brajanusz", "Kowalski", "Kowalski@mail.pl", 1999)
    print(user.card_number)
    user.card_number = 9998
    print(user.card_number)
