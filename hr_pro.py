from datetime import datetime
class Employee:
   #Employee class here
    def __init__(self,name,age,salary,employment_year):
        self.name = name
        self.age  = age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        today = datetime.now()
        return today.year - int(self.employment_year)

    # def __str__(self):
    #     working_years = str(self.get_working_years())
    #     return 'Name: '+self.name+', Age: '+str(self.age)+', Salary: '+str(self.salary)+', Working years: '+working_years

class Manager(Employee):
    #Manager class here
    def __init__(self, name,age,salary,employment_year, bonus_percentage):
        super().__init__(name,age,salary,employment_year)
        self.bonus_percentage = bonus_percentage
    # def get_working_years(self):
    #     today = datetime.now()
    #     return today.year - self.employment_year
    def get_bonus(self):
        return float(self.bonus_percentage) * float(self.salary)

    def __str__(self):
        working_years = str(self.get_working_years())
        bonus = str(self.get_bonus())
        return 'Name: '+self.name+', Age: '+str(self.age)+', Salary: '+str(self.salary)+', Working years: '+working_years+', Bonus: ' +bonus


def main():
    # main code here

    user_input = 0


    employee_list = []
    manager_list = []


    while user_input != 5:
        print("""Welcome to HR Pro 2019
        Options:
        1. Show Employees
        2. Show Managers
        3. Add An Employee
        4. Add A Manager
        5. Exit
         """)
        print()
        user_input = int(input("What would you like to do? "))
        print("------------------\n")
        if user_input == 1:
            print("Employees\n")
            if len(employee_list) == 0:
                print("Please add employee")
            else:
                # for employee in employee_list:
                #     employee = Employee(name,age,salary,employment_year)
                #
                # print(employee)
                for i in range(0, len(employee_list)):
                    print("Name: "+ employee_list[i].name+", Age: "+str(employee_list[i].age)+", Salary: "+ str(employee_list[i].salary)+", working Years: "+str(employee_list[i].get_working_years()))
            print("------------------\n")
        elif user_input == 2:
            if len(manager_list) == 0:
                print("Please add manager")
            else:
                # for manager in manager_list:
                #     manager = Manager(name,age,salary,employment_year,bonus_percentage)
                # print(manager)
                for i in range(0, len(manager_list)):
                    print("Name: "+ manager_list[i].name+", Age: "+str(manager_list[i].age)+", Salary: "+ str(manager_list[i].salary)+", working Years: "+str(manager_list[i].get_working_years())+", Bonus: "+str(manager_list[i].get_bonus()))
            print("------------------\n")
        elif user_input == 3:
            name = input("Name: ")
            age  = input("Age: ")
            salary   =input("Salary: ")
            employment_year  =input("Employment Year: ")
            added_employee = Employee(name,age,salary,employment_year)
            employee_list.append(added_employee)
            print("Employee added succesfully")
        elif user_input == 4:
            name= input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            employment_year =input("Employment Year: ")
            bonus_percentage = input("Bonus Percentage: ")
            added_manager= Manager(name,age,salary,employment_year,bonus_percentage)
            manager_list.append(added_manager)
            print("Manager added succesfully")
        print("""Welcome to HR Pro 2019
        Options:
        1. Show Employees
        2. Show Managers
        3. Add An Employee
        4. Add A Manager
        5. Exit
         """)



if __name__ == '__main__':
    main()
