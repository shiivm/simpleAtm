from Auth import Auth

class Main:

    def user(self):
        print('Choose option: \n 1.Register \t 2.Login')
        choice = input('Enter your choice :')

        auth = Auth()
        if choice == '1':
            auth.register()
        elif choice == '2':
            auth.login()
        else :
            print('Invalid choice')
            self.user()

if __name__ == '__main__':
   print('Welcome to Indian Bank')

   main = Main()
   main.user()
