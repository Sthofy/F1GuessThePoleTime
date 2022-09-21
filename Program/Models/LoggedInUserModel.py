class LoggedInUserModel:
    uid = 0
    username = ''
    email = ''
    password = ''
    phone = ''

    def __init__(self, uid, username, email, password, phone):
        self.uid = uid
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone

    def get_uid(self):
        return self.uid

    def set_uid(self, value):
        self.uid = value

    def get_username(self):
        return self.username

    def set_username(self, value):
        self.username = value

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    def get_password(self):
        return self.password

    def set_password(self, value):
        self.password = value

    def get_phone(self):
        return self.phone

    def set_phone(self, value):
        self.phone = value
