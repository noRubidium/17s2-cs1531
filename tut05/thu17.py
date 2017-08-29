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


class People(object):
    """docstring for People."""
    student_id = 0
    def __init__(self, name, address, phone):
        super(People, self).__init__()

        self.__name = name
        self.__address = address
        self.__phone = phone

    def change_address(self, addr):
        self.__address = addr

    def change_phone(self, phone):
        self.__phone = phone

    def __str__(self):
        return '%s #%d: %s' % (self.__class__.__name__, self.__id, self.__name)


class Attendee(People):
    """docstring for Attendee."""
    student_id = 0
    def __init__(self, name, address, phone):
        super(Attendee, self).__init__(name, address, phone)
        self.__id = Attendee.student_id
        Attendee.student_id += 1


class Trainer(People):
    """docstring for Trainer."""
    staff_id = 0
    def __init__(self, name, address, phone, field):
        super(Trainer, self).__init__(name, address, phone)
        self.__id = Trainer.staff_id
        self.__field = field
        Trainer.staff_id += 1

    def change_field(self, field):
        self.__field = field
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
        self.__attendee = set()
        self.__trainer = trainer

    def add_attendee(self, attendee):
        self.__attendee.add(attendee)

    def drop_attendee(self, attendee):
        self.__attendee.remove(attendee)

    def change_trainer(self, trainer):
        self.__trainer = trainer

    def __str__(self):
        s = list(map(str, self._attendee))
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
aarthi = Trainer("aarthi", "a@cse", "000", "Software?")
comp1531 = Course("COMP1531", "Software blah", "10/10/100000", "RC", aarthi)
comp1521 = Course("COMP1521", "Software blah", "10/10/100000", "RC", aarthi)
comp15311 = Course("COMP1531", "Software blah", "10/10/100000", "RC", aarthi)
abdul = Attendee('Whatever', 'ab@cse', '5304781297384')
abdul1 = Attendee('Whatever', 'ab@cse', '5304781297384')
minjie = Attendee('Minjie', 'ms@cse', '3249813')
comp1531.add_attendee(abdul)
comp1531.add_attendee(abdul1)
comp1531.add_attendee(minjie)

tc.add_course(comp1521)
tc.add_course(comp1531)
tc.add_course(comp15311)

print(tc)
