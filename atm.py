__Author__ = 'Rohith'

class Atm:

    __counter = 1
    def __init__(self) -> None:
        self.__pin = ""
        self.__balance = 0
        self.__menu()

    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter = new
        else:
            print("Invalid Operation")
            
    @staticmethod
    def get_counter():
        return Atm.__counter

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == int:
            self.__pin = new_pin
        else:
            print("Invalid Operation")

    def __menu(self):
        user_input = input('''
                           Hello, How would you like to Proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit 
                           '''
                           )
        if user_input == "1":
            self.__create_pin()
            self.__menu()

        elif user_input == "2":
            self.__deposit()
            self.__menu()

        elif user_input == "3":
            self.__withdraw()
            self.__menu()

        elif user_input == "4":
            self.__check_balance()
            self.__menu()

        else:
            print("Exit")

    def __create_pin(self):
        self.__pin = int(input("Enter your pin"))
        print("Pin set Succesfully")

    def __deposit(self):
        temp = int(input("Enter your pin"))
        if temp == self.__pin:
            deposit_amount = int(input("Enter the Amount"))
            self.__balance += deposit_amount
            print("Deposit Successful")
        else:
            print("Invalid pin")

    def __withdraw(self):
        temp = int(input("Enter your pin"))
        if temp == self.__pin:
            withdraw_amount = int(input("Enter the amount"))
            if withdraw_amount <= self.__balance:
                self.__balance -= withdraw_amount
                print("Withdraw Successful")
            else:
                print(" Insufficient Balance")
        else:
            print("Invalid Pin")

    def __check_balance(self):
        temp = int(input("Enter your pin"))
        if temp == self.__pin:
            print(f'Your balance is {self.__balance}')
        else:
            print("Invalid Pin")
