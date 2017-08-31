from abc import abstractmethod
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
        courses = list(map(str, self.__courses))
        return '\n\n'.join(courses)


def get_conversion(currency='AUD'):
    d = {'AUD': 1, 'USD': 1.27, 'PND': 1/0.61}
    return d.get(currency, 1)


class CreditCard(object):
    """docstring for CreditCard."""
    def __init__(self, card_number):
        super(CreditCard, self).__init__()
        self.card_number = card_number
        self.balance = 0

    def charge(self, amount, currency='AUD'):
        amount = amount * get_conversion(currency)
        if amount > self.balance:
            print('You are broke, lol!')
            return False
        self.balance -= amount
        return True

    def top_up(self, amount, currency='AUD'):
        if amount < 0:
            print('GO AWAY! STOP HACKING ME!')
            return
        mount = amount * get_conversion(currency)
        self.balance += amount

    def check_balance(self, currency='AUD'):
        return self.balance / get_conversion(currency)


class People(object):
    """docstring for People."""
    student_id = 0
    def __init__(self, name, address, phone, id):
        super(People, self).__init__()

        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__id = id

    @property
    def address(self):
        return self.__address

# p.address = "B"

    @address.setter
    def address(self, addr):
        if addr == 'ABDUL':
            print('WRONG PLACE')
            return
        self.__address = addr

    def change_phone(self, phone):
        self.__phone = phone

    @abstractmethod
    def update_balance(self, amount):
        pass

    def __str__(self):
        return '%s #%d: %s' % (self.__class__.__name__, self.__id, self.__name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.__name == other.__name:
                return True
        return False

    def __hash__(self):
        return self.__name.__hash__()

class Attendee(People):
    """docstring for Attendee."""
    student_id = 0
    def __init__(self, name, address, phone, credit_card):
        super(Attendee, self).__init__(name, address, phone, Attendee.student_id)
        self.__credit_card = credit_card
        Attendee.student_id += 1

    def update_balance(self, amount):
        return self.__credit_card.charge(amount)

class Trainer(People):
    """docstring for Trainer."""
    staff_id = 0
    def __init__(self, name, address, phone, field, credit_card):
        super(Trainer, self).__init__(name, address, phone, Trainer.staff_id)
        self.__field = field
        self.__credit_card = credit_card
        Trainer.staff_id += 1

    def change_field(self, field):
        self.__field = field

    def update_balance(self, amount):
        return self.__credit_card.top_up(amount)
# course = Course(....)
# course.add(2) -> Course.add(course, 2)


class Course(object):
    """docstring for Course."""
    def __init__(self, title, abstract, date, venue, trainer):
        super(Course, self).__init__()
        self.__title = title
        self.__abstract = abstract
        self.__date = date
        self.__venue = venue
        self.__attendee = list()
        self.__trainer = trainer

    def add_attendee(self, attendee):
        if attendee in self.__attendee:
            return
        if not attendee.update_balance(500):
            return
        self.__attendee.append(attendee)

    def drop_attendee(self, attendee):
        self.__attendee.remove(attendee)

    def change_trainer(self, trainer):
        self.__trainer = trainer

    def __str__(self):
        s = list(map(str, self.__attendee))
        return 'NAME: %s\n Trainer: %s\n Attendees: %s' % (self.__title, str(self.__trainer), ', '.join(s))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.__title == other.__title:
                return True
        return False

    def __hash__(self):
        return self.__title.__hash__()
    # def add(self, num):
    #     self.num += num

tc = ConferenceCenter()
ac = CreditCard('dskfjashdkf')
aarthi = Trainer("aarthi", "a@cse", "000", "Software?", ac)
comp1531 = Course("COMP1531", "Software blah", "10/10/100000", "RC", aarthi)
comp1521 = Course("COMP1521", "Software blah", "10/10/100000", "RC", aarthi)
comp15311 = Course("COMP1531", "Software blah", "10/10/100000", "RC", aarthi)
ac = CreditCard('93482172398')
ac.balance = 800
abdul = Attendee('Whatever', 'ab@cse', '5304781297384', ac)

mc = CreditCard('10012347819273498')
mc.balance = 800
minjie = Attendee('Minjie', 'ms@cse', '3249813', mc)

comp1531.add_attendee(abdul)
print('ABDUL ATTEND')
comp1531.add_attendee(abdul)
print('ABDUL ATTEND')

comp1531.add_attendee(minjie)
print('MINJIE ATTEND')

tc.add_course(comp1521)
tc.add_course(comp1531)
tc.add_course(comp15311)

aarthi.update_balance(1)

print(tc)
