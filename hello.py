from datetime import datetime

class Bank:
    users = {}
    total_users = 0

class User(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.balance = 0
        self.loan = 0
        self.transaction_history = {}
        self.count = 100

    def user_id(self):
        Id = self.count
        self.count += 1
        return Id
    
    def new_account(self,username:str,password:str):
        if username not in self.users:
            self.users[username] = {'Id':self.user_id(),'password':password,'balance':self.balance,'loan':self.loan}
            self.transaction_history[username] = []
            Bank.total_users += 1 
        else:
            print(f"{username} already exists")
    
    def get_balance(self,username):
        if username in self.users:
            print(f"username: {username} || Current Balance: ${self.users[username]['balance']:.2f}")
    
    def deposit(self,username,amount):
        try:
            if username in self.users:
                self.users[username]['balance'] += amount
                print(f"The Deposit of ${amount:.2f} was successful.✅")
                # self.get_balance(username)
                admin.total_bank_balance += amount
                transaction = f"Deposit: ${amount:.2f} : [{datetime.now().strftime('%d-%m-%Y : %H:%M:%S')}]"
                self.transaction_history[username].append(transaction)
            else: print(f"{username} is not found!")
        except: print('Deposit interrupted---⚠')

    def withdraw(self,username,amount):
        try:
            if admin.total_bank_balance>amount:
                if username in self.users:
                    if self.users[username]['balance'] >= amount:
                        self.users[username]['balance'] -= amount
                        admin.total_bank_balance -= amount
                        print(f"The Withdraw of ${amount:.2f} was successful.✅")
                        self.get_balance(username)
                        transaction = f"Withdraw: ${amount:.2f} : [{datetime.now().strftime('%d-%m-%Y : %H:%M:%S')}]"
                        self.transaction_history[username].append(transaction)
                    else: print("Sorry, Not enough balance")
                else: print(f"{username} is not found!")
            else: print('The bank is bankrupt🔒')
        except: print('Withdraw interrupted---⚠')
    
    def transfar_amount(self,username,amount,target_user):
        try:
            if username in self.users:
                if target_user in self.users:
                    if self.users[username]['balance'] > amount:
                        self.users[username]['balance'] -= amount
                        self.users[target_user]['balance'] += amount
                        print('The Transfar of $90 was successful.✅')
                        self.get_balance(username)
                        transaction = f"Transfar: ${amount:.2f} To {target_user} : [{datetime.now().strftime('%d-%m-%Y : %H:%M:%S')}]"
                        self.transaction_history[username].append(transaction)
                        transaction = f"Accept: ${amount:.2f} from {username} : [{datetime.now().strftime('%d-%m-%Y : %H:%M:%S')}]"
                        self.transaction_history[target_user].append(transaction)
                    else: print('Not enough balance!')
                else: print('Target user not found!')
            else: print(f"{username} is not found!")
        except:print('Transfar interrupted---⚠')
    
    def show_me(self,username):
        if username in self.users:
            print(f"{' '*10}{'='*20}")
            print(f"User_id: {self.users[username]['Id']}")
            print(f"Username: {username} || Password: {self.users[username]['password']}\nBalance: {self.users[username]['balance']:.2f} || Loan amount: {self.users[username]['loan']:.2f}")
            print(f"{' '*10}{'='*20}")
    
    def all_user_info(self):
        if Bank.total_users != 0:
            a = 1
            for key,value in self.users.items():
                print(f"{' '*10}{'-'*10} SHOW USERS #{a} {'-'*10}")
                print(f"User_id: {value['Id']}")
                print(f"Username: {key} || Password: {value['password']}\nBalance: {value['balance']:.2f} || Loan amount: {value['loan']:.2f}")
                print(f"{' '*10}{'-'*11} END USERS {'-'*12}")
                a += 1
        else: print('\nSorry, no user is currently available.')

    def get_loan(self,username):
        try:
            if admin.loan_feature == True:
                if self.users[username]['loan'] == 0:
                    amount = int(input('Enter the amount for loan: '))
                    if username in self.users and admin.total_bank_balance>amount:
                        if 2*self.users[username]['balance'] >= amount > 0:
                            self.users[username]['balance'] += amount
                            self.users[username]['loan'] += amount
                            transaction = f"Loan Amount: ${amount:.2f} : [{datetime.now().strftime('%d-%m-%Y : %H:%M:%S')}]"
                            self.transaction_history[username].append(transaction)
                            print(f"The loan of ${amount:.2f} was successfully processed.✅")
                            self.get_balance(username)
                        else: print(f"Sorry your bank account is not eligible for loan!")
                    else: print("Sorry, you must fulfill the loan terms before taking the loan")
                else: print('Sorry, you cannot apply for another loan until your previous one is fully repaid.\n')
            else: print("Sorry, the bank has stopped giving loans for now🛑")
        except: print('Loan interrupted---⚠')
    
    def loan_give_back(self,username):
        if self.users[username]['loan'] != 0:
            while(True):
                print(f"1. If you have enough money in your account to repay the loan then press [1]\n2. If you don't have enough money or you want to \n   repay the loan in installments then press [2]\n3. Exit\n")
                press = input('Enter your choice(1/2/3): ')
                if press == '1':
                    k_lon = self.users[username]['loan']
                    self.users[username]['balance'] -= k_lon
                    self.users[username]['loan'] -= k_lon
                    transaction = f"Lonn repayment: ${k_lon:.2f} : [{datetime.now().strftime('%d-%m-%Y : %H:%M%S')}]"
                    self.transaction_history[username].append(transaction)
                    print(f"Loan repayment of ${k_lon:.2f} successful✅ Remaining loan: ${self.users[username]['loan']}")
                    break
                elif press == '2':
                    try:
                        amount = int(input('Please input the amount you wish to repay the loan: '))
                        print('\n🔰This amount will first be deposited to your account and then deducted from the account🔰\n')
                        self.deposit(username,amount)
                        if self.users[username]['loan'] >= amount and amount > 0:
                            self.users[username]['balance'] -= amount
                            self.users[username]['loan'] -= amount
                            transaction_1 = f"Loan repayment: ${amount:.2f} : [{datetime.now().strftime('%d-%m-%Y : %H:%M%S')}]"
                            self.transaction_history[username].append(transaction_1)
                            print(f"Loan repayment of ${amount:.2f} successful✅ Remaining loan: ${self.users[username]['loan']:.2f}\n")
                            break
                        elif self.users[username]['loan'] < amount:
                            n_loan = self.users[username]['loan']
                            self.users[username]['balance'] -= n_loan
                            extra_money = amount - n_loan
                            self.users[username]['loan'] -= n_loan
                            transaction_2 = f"Loan repayment: ${n_loan:.2f} : [{datetime.now().strftime('%d-%m-%Y : %H:%M:%S')}]"
                            self.transaction_history[username].append(transaction_2)
                            print(f"Loan overpaid! Loan repayment of ${n_loan:.2f} successful✅,Remaining amount of ${extra_money:.2f} added to the balance.\n")
                            break
                    except: print('Loan repayment interrupted---⚠')
                elif press == '3':
                    break
                else: print('Sorry, invalid input. Please try again!')
        else: print(f"Sorry, you can't repay the loan\nbecause your loan amount is: ${self.users[username]['loan']:.2f}")

    def Transact_history(self, username):
        if username in self.transaction_history:
            print(f"Transaction History for {username}:")
            for transaction in self.transaction_history[username]:
                print(transaction)
        else:
            print(f"No transaction history found for {username}")

class Admin(User):
    def __init__(self) -> None:
        super().__init__()
        self.admins = {'admin':{'password':'123'}}
        self.total_bank_balance = 1000000
        self.loan_feature = False
    
    def admin_account(self,username,passwrod):
        if username not in self.admins:
            self.admins[username] = {'password':passwrod}
        else: print(f'Sorry,{username} already exist!')
    
    def admin_replace(self,current_user,current_pass,new_user,new_pass):
        if current_user in self.admins and self.admins[current_user]['password'] == current_pass:
            self.admins[new_user] = self.admins[current_user]
            self.admins[new_user]['password'] = new_pass
            del self.admins[current_user]
            print('Admin username and password changed successfully✅')
        else: print('This username does not exist!')
    
    def add_bank_balance(self,username,amount):
        if username in self.admins:
            self.total_bank_balance += amount
        else: print('Sorry,Admin not found!')
    
    def show_all_admin_pass(self):
        a = 1
        print(f"{' '*10}{'-'*10} All_ADMIN_PASS {'-'*10}")
        for key,value in self.admins.items():
            print(f"# ADMIN-{a}:: Username: {key} || Password: {value['password']}")
            a += 1
        print(f"{' '*10}{'-'*10}{'='*15}{'-'*10}")

    def show_bank_info(self):
        a = 1
        print(f"{' '*10}{'-'*10} SHOW BANKS INFO # {a} # {'-'*10}")
        for key,value in self.admins.items():
            print(f"# ADMIN-{a}:: Username: {key} || Password: {value['password']}")
            a += 1
        print(f"Total Bank User: {Bank.total_users}")
        if self.loan_feature == True:
            print("# Loan Feature: Enable✅")
        else: print("# Loan Feature: Disable❌")
        print(f"Total Bank Balance: ${self.total_bank_balance:.2f}")
        print(f"{' '*10}{'-'*11}{'='*17}{'-'*12}")

    def show_bank_balance(self):
        print(f"Total Bank Balance: ${self.total_bank_balance:.2f}")

    def loan_feature_set(self,username,loan:bool):
        if username in self.admins:
            self.loan_feature = loan
        else: print('Admin is not found!')

user = User()
admin = Admin()

while(True):
    print(f"{' '*5}{'*'*5}KNJI bank{'*'*5}")
    print('1. Create an Account\n2. Login an Account\n3. Login for admin\n4. Exit')
    user_input = input('Enter your choice(1/2/3/4): ')
    if user_input == '4':
        exit('____Thank you for visiting our Bank_____\n\n')
    elif user_input == '1':
        user_name = input('Enter Your Username: ')
        pass_word = input('Enter Your Password: ')
        user.new_account(user_name,pass_word)
        print('Your account has been created successfully✅')
        print('\t-------------------\n')
    elif user_input == '2':
        username = input('Enter Your Username: ')
        password = input('Enter Your Password: ')
        if username in user.users and user.users[username]['password'] == password:
            print(f"{' '*5}{'*'*5}Welcome to our bank{'*'*5}")
            while(True):
                print('1. Deposit\n2. Withdraw\n3. Transfar\n4. Take Loan\n5. Repay the loan \n6. My Info\n7. Transaction history\n8. Exit\n')
                n = input('Enter your choice(1/2/3/4/5/6/7/8): ')
                if n == '8':
                    print('\t-------------------\n')
                    break
                elif n == '1':
                    dip_amount = int(input('Please input the amount you wish to deposit: '))
                    user.deposit(username,dip_amount)
                    user.get_balance(username)
                    print('\t-------------------\n')
                elif n == '2':
                    wit_amount = int(input('Please indicate the amount you would like to withdraw: '))
                    user.withdraw(username,wit_amount)
                    print('\t-------------------\n')
                elif n == '3':
                    target_user = input('Enter the targeted username to Transfer money: ')
                    tr_amount = int(input('Input the amount of money to Transfer: '))
                    user.transfar_amount(username,tr_amount,target_user)
                    print('\t-------------------\n')
                elif n == '4':
                    user.get_loan(username)
                    print('\t-------------------\n')
                elif n == '5':
                    user.loan_give_back(username)
                    print('\t-------------------\n')
                elif n == '6':
                    user.show_me(username)
                    print('\t-------------------\n')
                elif n == '7':
                    user.Transact_history(username)
                    print('\t-------------------\n')
                else: 
                    print('Sorry, invalid input. Please try again!')
                    print('\t-------------------\n')
        else: 
            print('Please input the valid username and password.\n')
            print('\t-------------------\n')
    elif user_input == '3':
        in_admin = input('Enter your username: ')
        in_password = input('Enter your password: ')
        if in_admin in admin.admins and admin.admins[in_admin]['password'] == in_password:
            print(f"{' '*5}{'*'*5}HELLO: {in_admin} :ADMIN{'*'*5}")
            while(True):
                print('1. Create a new account\n2. Change the current username and password of the admin account\n3. Show all users\n4. Show Bank info\n5. Show Total Bank Balance\n6. Loan (enable/disable)\n7. Check transaction history for any Bank user.\n8. Exit')
                k = input('Enter your choice(1/2/3/4/5/6/7/8): ')
                if k == '8':
                    print('\t-------------------\n')
                    break
                elif k == '1':
                    new_user = input('Enter a new username for the admin: ')
                    new_pass = input('Enter a new password for the admin: ')
                    admin.admin_account(new_user,new_pass)
                    print('Your account has been created successfully✅')
                    print('\t-------------------\n')
                elif k == '2':
                    admin.show_all_admin_pass()
                    while(True):
                        key = input('If you want to change your current username and password press [ y ] otherwise press [ x ].\nPRESS KEY: ')
                        if key == 'x' or key =='X':
                            print('-------------------\n')
                            break
                        elif key == 'y' or key == 'Y':
                            current_username = input('Enter the current username: ')
                            current_password = input('Enter the current password: ')
                            if current_username in admin.admins and admin.admins[current_username]['password'] == current_password:
                                new_user = input('Input a new username: ') 
                                new_pass = input('Input a new password: ')
                                admin.admin_replace(current_username,current_password,new_user,new_pass)
                                print('\t-------------------\n')
                                break
                            else: 
                                print('\nThis username does not exist, try again!')
                                print('\t-------------------\n')
                        else: 
                            print('Sorry, invalid input. Please try again!')
                            print('\t-------------------\n')

                elif k == '3':
                    user.all_user_info()
                    print('\t-------------------\n')
                elif k == '4':
                    admin.show_bank_info()
                    print('\t-------------------\n')
                elif k == '5':
                    admin.show_bank_balance()
                    print('\t-------------------\n')
                elif k == '6':
                    if admin.loan_feature == True:
                        while(True):
                            print('Loan feature: Enable✅\n')
                            word1 = input('If you want to disable the Loan feature then press [ y ] otherwise press [ x ].\nPRESS KEY: ')
                            if word1 == 'y' or word1 == 'Y':
                                admin.loan_feature_set(in_admin,False)
                                print('The loan feature was successfully deactivated ---🚫')
                                print('\t-------------------\n')
                                break
                            elif word1 == 'x' or word1 == 'X':
                                print('\t-------------------\n')
                                break
                            else:
                                print('Sorry, invalid input. Please try again!')
                                print('\t-------------------\n')

                    elif admin.loan_feature == False:
                        while(True):
                            print('Loan feature: Disable🚫\n')
                            word2 = input('If you want to enable the Loan feature then press [ y ] otherwise press [ x ].\nPRESS KEY: ')
                            if word2 == 'y' or word2 == 'Y':
                                admin.loan_feature_set(in_admin,True)
                                print('The loan feature was successfully activated---✅')
                                print('\t-------------------\n')
                                break
                            elif word2 == 'x' or word2 == 'X':
                                print('\t-------------------\n')
                                break
                            else:
                                print('Sorry, invalid input. Please try again!')
                                print('\t-------------------\n')
                elif k == '7':
                    bank_user = input('Enter the targeted username: ')
                    user.Transact_history(bank_user)
                    print('\t-------------------\n')
                else:
                    print('\t-------------------\n')
                    break
        else: 
            print('Sorry, invalid input. Please try again!')
            print('\t-------------------\n')
    else: 
        print('Sorry, invalid input. Please try again!\n')
        print('\t-------------------\n')