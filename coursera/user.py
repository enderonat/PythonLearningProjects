class User:
    def __init__(self, first_name, last_name, skin_color, hair_color):

        self.first_name = first_name
        self.last_name = last_name
        self.skin = skin_color
        self.hair = hair_color
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is {self.skin} and has {self.hair} hair')

    def greet_user(self):
        print(f'greetings {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, skin_color, hair_color):
        super().__init__(first_name, last_name, skin_color, hair_color)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["can add posts", "can delete posts", "can ban user"]

    def show_privileges(self):
        print(f'this user {self.privileges}')


me = Admin('Ender', 'Onat', 'esmer', 'siyah')
asli = User('ASlı', '', 'esmer', 'sarı')

me.describe_user()
me.greet_user()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.reset_login_attempts()
me.privileges.show_privileges()
print(me.login_attempts)

asli.describe_user()
asli.greet_user()
asli.increment_login_attempts()
print(asli.login_attempts)
