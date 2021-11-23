class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not self.valid_username(value):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    def valid_username(self, username):
        return 5 <= len(username) <= 15

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.valid_password_lendgth(value) and self.password_has_digit(value) and self.password_has_uppercase(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def valid_password_lendgth(self, password):
        return len(password) >= 8

    def password_has_uppercase(self, password):
        uppercase = [char for char in password if char.isupper()]
        return True if uppercase else False

    def password_has_digit(self, password):
        digits = [char for char in password if char.isdigit()]
        return True if digits else False

    def __str__(self):
        password = '*' * len(self.password)
        return f'You have a profile with username: "{self.username}" and password: {password}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile('Username', 'Passw0rd')
print(correct_profile)