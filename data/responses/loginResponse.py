class LoginResponse:
    def __init__(self, id, fullname):
        self.id = id
        self.fullname = fullname

    def to_json(self):
        return{

            'id': self.id,
            'fullname': self.fullname,

        }