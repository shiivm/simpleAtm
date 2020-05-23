import csv
import time
import sys

from Atm import Atm

class Auth:
    def login(self):
        acc_no = input('Enter your account number:')
        pin = input('Enter your atm pin:')
        file = open('data.csv','r')       
        data = csv.reader(file)
        for row in data:
            if row[1]== acc_no and row[2] == pin:
                print("\nWelcom {}".format(row[0]))
                atm = Atm(acc_no)
                atm.menu()
        else:
            print('Invalid credentials')
            self.login()
        file.close()

    def register(self):
        name = input('Enter your name:')
        acc_no = input('Enter your account number:')
        pin = input('Enter your pin:')
        bal = 0
        fields = [name,acc_no,pin,bal] 
        file = open('data.csv','a')  
        writer = csv.writer(file)
        writer.writerow(fields)
        sys.stdout.write("Registering")
        for i in range(6):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(.6)
        print('\n')
        self.login()



