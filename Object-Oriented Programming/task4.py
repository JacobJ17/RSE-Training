class Person:
    """A person."""
    def __init__(self, name):
        self.name = name
        self.id = None

    def __str__(self):
        return self.name

    def set_id(self, id):
        raise NotImplementedError('set_id not implemented')

    def get_id(self):
        return self.id

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return 'Patient: ' + super().__str__()

    def set_id(self, id):
        self.id = 'P' + str(id).zfill(4)


class Doctor(Person):
    """A doctor in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return 'Doctor: ' + super().__str__()

    def set_id(self, id):
        self.id = 'D' + str(id).zfill(4)

class Administrator:
    """An administrator in an inflammation study."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Administrator: ' + self.name

    def set_id(self, id):
        self.id = 'A' + str(id).zfill(4)

    def get_id(self):
        return self.id


class Trial:
    """All patients and doctors involved in an inflammation study"""
    def __init__(self):
        self.list_of_people = []

    def add_person(self, new_person):
        if isinstance(new_person, Person):
            self.list_of_people.append(new_person)
        elif hasattr(new_person, 'get_id'):
            new_person_id = new_person.get_id()
            if new_person_id[0] == 'D':
                person = Doctor(new_person_id)
            elif new_person_id[0] == 'P':
                person = Patient(new_person_id)
            elif new_person_id[0] == 'A':
                person = Administrator(new_person_id)
            else:
                raise TypeError('could not recognise person id, should start with D, P or A')
        
            self.list_of_people.append(person)
        
        else:
            raise TypeError('person must be a Person object or have a get_id method')


    def print_people(self):
        for person in self.list_of_people:
            print(person)

    def set_ids(self):
        for i, person in enumerate(self.people):
            person.set_id(i + 1)
