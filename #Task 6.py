#Task 6
# Problem 1 Bank Account
class BankAccount: #Base Class
    def __init__(self, account_number, balance):
        self.account_number = account_number #assigning the variable
        self.__balance = balance # to keep this as Private variable (encapsualtion)

    def get_balance(self): #to get the balance
        return self.__balance
    
    def deposit(self,amount): #defining the deposit
        if amount >0 : #Amount should be greater than 0 for Deposits
            self.__balance += amount # Balance should be Previus balance + deposit amount 
            print("Amount Deposited:", amount) #to display the deposit amount
            print("Balance after deposit :",self.__balance) # to display the new balance
        else:
            print("Please deposit minimum of Rs1") # if the amount selected as Zero then it should throw an error

    def withdraw(self,amount): #defining for withdraw
         if amount <= self.__balance: # if condition for withdrawal should not exceed the balance amount
             self.__balance -= amount
             print("Amount withdrawn:", amount)
             print("Remaining Balance:",self.__balance)
         else:
             print("Insufficient balance") #if its exceed it throw insufficient balance
    
class SavingsAccount(BankAccount): #subclass Savings account
    def __init__(self, account_number, balance, interest_rate): #defining the criteria
        BankAccount.__init__(self, account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self): #defining for interest calculation
        interest = self.get_balance()*self.interest_rate / 100 # Balance * Interest rate as the interest rate denotes in integers hence divide by 100 given to convert into percentage
        print("Interest:", interest) #just to understand the interest amount
        return interest
    

class CurrentAccount(BankAccount): #subclass Current account
    def __init__(self, account_number, balance, min_balance): #criteria min balance requirements
        BankAccount.__init__(self, account_number, balance) 
        self.min_balance = min_balance
    

    def withdraw(self, amount): # withdrawal amount criteria
        if self.get_balance() - amount >= self.min_balance: #withdrawal amount not exceed minimum balance
            BankAccount.withdraw(self,amount)
        else:
            print("Withdrwal denied due to minimum balance requirements")

#to check the output assining the values for each variables
Savings = SavingsAccount("MYSBAC001",10000,2.5)
print("Account Balance in Savings account:", Savings.get_balance())
Savings.deposit(5000)
Savings.withdraw(7500)
Savings.calculate_interest()
print(" ")

Savings = SavingsAccount("MYSBAC001",1000,2.5)
print("Account Balance in Savings account:", Savings.get_balance())
Savings.deposit(5000)
Savings.withdraw(7500)
Savings.calculate_interest()
print(" ")


Current = CurrentAccount("MYCUAC002", 5000, 1500)
Current.deposit(275)
Current.withdraw(2500)
print(" ")

Current = CurrentAccount("MYCUAC002", 5000, 10000)
Current.deposit(5275)
Current.withdraw(2500)
print(" ")


#problem 2- Employee Management

class employee: #Base class employee
    def __init__(self, name, base_salary): # defining name & base salary
        self.name = name 
        self.base_salary = base_salary

    def calculate_salary(self): # defining to calculate salary
        return self.base_salary
    
class RegularEmployee(employee): # subclass regular employee gets additional benefits
    def __init__(self, name, base_salary, benefits):
        employee.__init__(self, name, base_salary)
        self.benefits = benefits

    def calculate_salary(self):
        total_salary = self.base_salary + self.benefits #salary = base salary + benefits
        print(f"RegularEmployee: {self.name}, {total_salary}")
        return total_salary
    
class ContractEmployee(employee): #subclass contract employee calculation is based on hours worked
    def __init__(self, name, hours_worked, rate_perhour):
        employee.__init__(self, name, 0 )
        self.hours_worked = hours_worked
        self.rate_perhour = rate_perhour

    def calculate_salary(self):
        total_salary = self.hours_worked * self.rate_perhour
        print(f"Contract Employee: {self.name}, {total_salary}")
        return total_salary

class Manager(employee): # subclass Manager gets base salary and sharing in profits
    def __init__(self, name, base_salary, profit_share):
        employee.__init__(self, name, base_salary)
        self.profit_share = profit_share

    def calculate_salary(self):
        total_salary = self.base_salary + self.profit_share
        print(f"Manger: {self.name}, {total_salary}")
        return total_salary
    
print(" ")

# assigning the values to check the output

employee = [
    RegularEmployee("Nithya",10000,5000),
    ContractEmployee("Kethav",20,1000),
    Manager("Yashvini", 20000, 5000)
]


for emp in employee:
    emp.calculate_salary()

        

#problem 3 Vehicle Rental
class vehicle: # class vehicle
    def __init__(self, model, rental_rate): #defining the model & rental rate
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self,days): #rebtal amount = rate * days
        rental = self.rental_rate * days
        return rental
    
class Car(vehicle): #subclass Car based on the seater 
    def __init__(self, model, rental_rate, seats):
        vehicle.__init__(self, model, rental_rate)
        self.seats = seats

    def calculate_rental(self, days):
        total_amount = self.rental_rate * days
        print(f"Total Rental amount: {self.model}, Total Rental Cost is {total_amount}")
        return total_amount

class Bike(vehicle): # subclass bike based on the type like battery or petrol
    def __init__(self, model, rental_rate, type):
        vehicle.__init__(self, model, rental_rate)
        self.type = type
         
    def calculate_rental(self, days):
        total_amount = self.rental_rate * days
        print(f"Total Rental amount: {self.model}, Total Rental Cost is {total_amount}")
        return total_amount
    
class Truck(vehicle): # subclass truck rental is based on the load capacity
    def __init__(self, model, rental_rate, load_capacity):
        vehicle.__init__(self, model, rental_rate)
        self.load_capacity = load_capacity
         
    def calculate_rental(self, days):
        total_amount = self.rental_rate * days
        print(f"Total Rental amount: {self.model}, Total Rental Cost is {total_amount}")
        return total_amount

vehicle = [
    Car("Ferrari",5000,4),
    Bike("Kawasaki",1000,"petrol"),
    Truck("Tesla",200,1000)
]

print(" ")

for x in vehicle:
    x.calculate_rental(5) # rental cost for 5 days.

        
    







    

        
    
