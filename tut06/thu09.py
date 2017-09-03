from abc import abstractmethod, ABCMeta
# property
# say one of the method can be used as a property
class ConferenceCenter(object):
    """docstring for ConferenceCenter."""
    def __init__(self):
        super(ConferenceCenter, self).__init__()
        self.__courses = set()

    def add_course(self, course):
        self.__courses.add(course)

    def delete_course(self, course):
        self.__courses.remove(course)

    def __str__(self):
        return '\n\n'.join(list(map(str, self.__courses)))


class Person(metaclass=ABCMeta):
    """docstring for Person."""
    def __init__(self, name, address, phone, credit_card, id):
        super(Person, self).__init__()
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__credit_card = credit_card
        self.__id = id

    @abstractmethod
    def update_balance(self, amount):
        pass

    @property
    def address(self):
        return self.__name + ' has address ' + self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def get_id(self):
        return self.__id

    def change_phone(self, phone):
        self.__phone = phone

    def get_credit_card(self):
        return self.__credit_card

    def __str__(self):
        return '%s #%d: %s' % (self.__class__.__name__, self.__id, self.__name)

CURRENCY = 'USD'

class CreditCard(object):
    def __init__(self, card_number, balance):
        self.__card_number = card_number
        self.__balance = balance

    def get_card_number(self):
        return self.__card_number

    @property
    def balance(self):
        return self.get_balance_currency(CURRENCY)

    @balance.setter
    def balance(self, amount):
        return self.charge(amount, CURRENCY)

    def get_balance_currency(self, currency='pounds'):
        if currency == 'USD':
            return self.__balance * 1.2
        if currency == 'AUD':
            return self.__balance * 1.6
        return self.__balance

    def charge(self, amount, currency='pounds'):
        if amount > self.get_balance_currency(currency):
            print('Insufficient balance!')
            return False
        self.__balance -= amount
        return True

    def topup(self, amount, currency='pounds'):
        self.__balance += amount
        return True


class Attendee(Person):
    """docstring for Attendee."""
    student_id = 0
    def __init__(self, name, address, phone, credit_card):
        super(Attendee, self).__init__(name, address, phone, credit_card, Attendee.student_id)
        Attendee.student_id += 1

    def update_balance(self, amount):
        self.get_credit_card().balance = amount
        return True


class Trainer(Person):
    """docstring for Trainer."""
    staff_id = 0
    def __init__(self, name, address, phone, field, credit_card):
        super(Trainer, self).__init__(name, address, phone, credit_card, Trainer.staff_id)
        self.__field = field
        Trainer.staff_id += 1

    def change_field(self, field):
        self.__field = field

    def update_balance(self, amount):
        return self.get_credit_card().topup(amount)


class Course(object):
    """docstring for Course."""
    def __init__(self, title, abstract, date, venue, trainer):
        super(Course, self).__init__()
        self.__title = title
        self.__abstract = abstract
        self.__date = date
        self.__venue = venue
        self.__trainer = trainer
        self.__attendees = list()

    def check_attendee(self, attendee):
        return attendee in self.__attendees

    def add_attendee(self, attendee):
        if self.check_attendee(attendee):
            return
        if not attendee.update_balance(500):
            return
        self.__attendees.append(attendee)

    def drop_attendee(self, attendee):
        self.__attendees.remove(attendee)

    def change_trainer(self, trainer):
        self.__trainer = trainer

    def end_session(self):
        self.__trainer.update_balance(300 * len(attendee))

    def __str__(self):
        students = list(map(str, self.__attendees))
        # print('THIS IS THE STUDENTS LIST', ', '.join(students))
        return 'COURSE NAME: %s, TRAINER: %s\n, STUDENTS: %s' % (self.__title, str(self.__trainer), ', '.join(students))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.__title == other.__title:
                return True
        return False

    def __hash__(self):
        return self.__title.__hash__()

system = ConferenceCenter()
ac = CreditCard(10000, 100)
aarthi = Trainer("Aarthi", "a@cse.unsw.edu.au", "+61 000", "Theory", ac)
comp1531 = Course("COMP1531", "Software blah", "01/01/2017", "Webster", aarthi)
comp1521 = Course("COMP1521", "Software blah", "01/01/2017", "Webster", aarthi)
comp15311 = Course("COMP1531", "Software blah", "01/01/2017", "Webster", aarthi)
tc = CreditCard(10000, 1500)
tom = Attendee("TOM", "t", "100", tc)
bc = CreditCard(10000, 30)
ben = Attendee("BEN", "t", "100", bc)

comp1531.add_attendee(tom)
comp1531.add_attendee(tom)
comp1531.add_attendee(ben)

system.add_course(comp1531)
system.add_course(comp15311)
system.add_course(comp1521)
print('TOM HAS:', tc.get_balance_currency())
print(system)
