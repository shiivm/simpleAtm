import csv
import time
import os

class Atm:

    def __init__(self,row):
        self.name = row['name']
        self.acc_no = row['accountNo']
        self.balance = float(row['balance'])
        self.filename = 'data.csv'
    
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
        print("\nYour Account Balance is : {}".format(self.balance))
        time.sleep(1)
        self.menu()

    def withdraw(self):
        amount = float(input("Enter amount: "))
        if(amount > self.balance):
            print("Insufficient balance")
            self.menu()
        else:
            self.balance  -= float(amount)
            mylist = self.prepaer_update_data(self.balance); 
            self.update_file(mylist)
            print('Please collect the cash')
            self.menu()

    def deposit(self):
        amount = float(input('Please enter amont to be deposited: '))
        if amount <= 0:
            print('Please enter amount greater than 0')
            self.deposit()
        else:
            self.balance  += float(amount)
            mylist = self.prepaer_update_data(self.balance); 
            self.update_file(mylist)
            print('Money deposited successfully')
            self.menu()

    def prepaer_update_data(self,amount):
        mylist = []; 
        fieldnames = ['name', 'accountNo','pin','balance']
        try:
            with open(self.filename,'r+', newline='') as file:
                data = csv.DictReader(file)
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                for row in data:
                    if row['accountNo'] == self.acc_no:
                        mylist.append({'name' : row['name'],'accountNo' : row['accountNo'],'pin':row['pin'],'balance' : float(amount)})
                    else:
                        mylist.append(row)
        except:
            pass

        return mylist
    
    def update_file(self,data):
        if(len(data) == 0):
            return
        tempfilename = 'temp.csv'
        fieldnames = ['name', 'accountNo','pin','balance']
        try:
            os.remove(tempfilename)  # delete any existing temp file
        except OSError:
            pass
        try:
            with open(tempfilename,'a', newline='') as file:
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                writer.writeheader()
                for item in data:
                    writer.writerow(item)
            os.rename(tempfilename,self.filename)
        except:
            pass
