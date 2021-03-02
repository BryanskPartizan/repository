import random

class Verification(object):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__password_len()
        self.__difficult()

    def __password_len(self):
        if len(self.password) < 7:
            raise ValueError('Password is very simple')

    def __difficult(self):
        if 8 < len(self.password) < 12:
            return 'simple'
        elif 11 < len(self.password) < 16:
            return 'normal'

    def save(self):
        with open('users', 'a') as users_data:
            users_data.write(f'{self.login, self.password, self.__difficult()}' + '\n')



if __name__ == "__main__":
    users_list = []
    for i in range(1000):
        users_list.append(Verification(str(f'{i+1}'), str(random.randint(10000000, 100000000000))))
        users_list[i].save()

