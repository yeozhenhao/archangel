class Player:
        def is_valid(self):
                return self.name != "" and self.floor != "" and self.room_number != ""

        def __init__(self, **kwargs):
                self.name = kwargs.get('name')
                self.fbname = kwargs.get('fbname')
                self.floor = int(kwargs.get('floor'))
                self.room_number = kwargs.get('room_number')
                self.gender = kwargs.get('gender')
                self.year = int(kwargs.get('year'))
                self.gender_pref = kwargs.get('gender_pref')
                self.faculty = kwargs.get('faculty')
                self.interests = kwargs.get('interests')

        def __repr__(self):
                return str(self.name)

