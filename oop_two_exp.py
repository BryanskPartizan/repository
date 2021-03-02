from tkinter import Tk

class Purse(object):
    def __init__(self, currency_name, owner='Unknown'):
        self.__balance = 0.00
        self.currency_name = currency_name
        self.owner = owner

    def top_up_balance(self, amount):
        self.__balance = self.__balance + amount
        return amount

    def top_down_balance(self, amount):
        if amount > self.__balance:
            print('Недостаточно средств.')
            raise ValueError('Недостаточно средств.')
        else:
            self.__balance = self.__balance - amount
        return amount
    
    def info(self):
        print(f'owner is {self.owner}')
        print(f'currency: {self.currency_name}')
        print(f'Баланс кошелька: {self.__balance}')

    def __del__(self):
        return self.__balance

root = Tk()

root.mainloop()
    


my_purse = Purse('USD', 'Matthew')
my_purse.top_up_balance(10)
my_purse.info()
print('FIRST STAGE END')

emil_purse = Purse('USD', 'Emil')
emil_purse.top_up_balance(620)
emil_purse.info()
print('SECOND STAGE END')

my_purse.top_up_balance(emil_purse.top_down_balance(620))
emil_purse.info()
my_purse.info()
