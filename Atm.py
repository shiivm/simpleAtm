import csv
import time

class Atm:

    def __init__(self,acc_no):
        self.acc_no = acc_no
    
    def menu(self):
        print("\n 1.Balance Enquiry \t 2.Withdraw \n 3.Deposit \t\t 4.Exit\n" )
        choice =input('Select your choice: ')
        if choice == '1':
            self.balance_enquiry()

        elif choice == '2':
            self.withdraw()

        elif choice == '3':
            self.deposit()
        
        elif choice == '4':
            print('\n##################<<Thanks for using our ATM>>##################\n')
            exit()
        else:
            print('Invalid choice')
            self.menu()

    def balance_enquiry(self):
        file = open('data.csv','r')       
        data = csv.reader(file)
        for row in data:
            if(row[1] == self.acc_no):
                print("\nYour Account Balance is : {}".format(row[3]))
        time.sleep(1)
        self.menu()
        
        
