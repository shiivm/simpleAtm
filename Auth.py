import csv
import time
import sys

from Atm import Atm

class Auth:
    def login(self):
        acc_no = input('Enter your account number:')
        pin = input('Enter your atm pin:')
        with open('data.csv','r', newline='') as file:
            data = csv.DictReader(file)
            for row in data:
                if row['accountNo']== acc_no and row['pin'] == pin:
                    print("\nWelcom {}".format(row['name']))
                    atm = Atm(row)
                    atm.menu()
            else:
                print('Invalid credentials')
                self.login()

    def register(self):
        name = input('Enter your name:')
        acc_no = input('Enter your account number:')
        pin = input('Enter your pin:')
        bal = 0
        with open('data.csv','a', newline='') as file:
            fieldnames = ['name', 'accountNo','pin','balance']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writerow({'name':name,'accountNo':acc_no,'pin':pin,'balance':bal})
            sys.stdout.write("Registering")
            for i in range(6):
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(.6)
        print('\n')
        self.login()



