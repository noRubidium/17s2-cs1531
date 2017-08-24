class ConferenceCenter(object):
    """docstring for ConferenceCenter."""
    def __init__(self):
        super(ConferenceCenter, self).__init__()
        self._courses = set()

    def add_course(self, course):
        self._courses.add(course)

    def delete_course(self, course):
        self._courses.remove(course)

    def __str__(self):
        return '\n\n'.join(list(map(str, self._courses)))

class Person(object):
    """docstring for Person."""
    def __init__(self, name, address, phone):
        super(Person, self).__init__()
        self._name = name
        self._address = address
        self._phone = phone

    def change_address(self, address):
        self._address = address

    def change_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return '%s #%d: %s' % (self.__class__.__name__, self._id, self._name)

class Attendee(Person):
    """docstring for Attendee."""
    student_id = 0
    def __init__(self, name, address, phone):
        super(Attendee, self).__init__(name, address, phone)
        self._id = Attendee.student_id
        Attendee.student_id += 1


class Trainer(Person):
    """docstring for Trainer."""
    staff_id = 0
    def __init__(self, name, address, phone, field):
        super(Trainer, self).__init__(name, address, phone)
        self._field = field
        self._id = Trainer.staff_id
        Trainer.staff_id += 1

    def change_field(self, field):
        self._field = field


class Course(object):
    """docstring for Course."""
    def __init__(self, title, abstract, date, venue, trainer):
        super(Course, self).__init__()
        self._title = title
        self._abstract = abstract
        self._date = date
        self._venue = venue
        self._trainer = trainer
        self._attendees = set()

    def add_attendee(self, attendee):
        self._attendees.add(attendee)

    def drop_attendee(self, attendee):
        self._attendees.remove(attendee)

    def change_trainer(self, trainer):
        self._trainer = trainer

    def __str__(self):
        students = list(map(str, self._attendees))
        # print('THIS IS THE STUDENTS LIST', ', '.join(students))
        return 'COURSE NAME: %s, TRAINER: %s\n, STUDENTS: %s' % (self._title, str(self._trainer), ', '.join(students))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self._title == other._title:
                return True
        return False

    def __hash__(self):
        return self._title.__hash__()

system = ConferenceCenter()
aarthi = Trainer("Aarthi", "a@cse.unsw.edu.au", "+61 000", "Theory")
comp1531 = Course("COMP1531", "Software blah", "01/01/2017", "Webster", aarthi)
comp1521 = Course("COMP1521", "Software blah", "01/01/2017", "Webster", aarthi)
comp15311 = Course("COMP1531", "Software blah", "01/01/2017", "Webster", aarthi)
tom = Attendee("TOM", "t", "100")
ben = Attendee("BEN", "t", "100")
comp1531.add_attendee(tom)
comp1531.add_attendee(tom)
comp1531.add_attendee(ben)
system.add_course(comp1531)
system.add_course(comp15311)
system.add_course(comp1521)
print(system)
