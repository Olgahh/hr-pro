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
        return today.year - self.employment_year

    def __str__(self):
        working_years = str(self.get_working_years())
        return 'Name: '+self.name+', Age: '+str(self.age)+', Salary: '+str(self.salary)+', Working years: '+working_years

class Manager(Employee):
    #Manager class here
    def __init__(self, name,age,salary,employment_year, bonus_percentage):
        super().__init__(name,age,salary,employment_year)
        self.bonus_percentage = bonus_percentage
    def get_working_years(self):
        today = datetime.now()
        return today.year - self.employment_year
    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
        working_years = str(self.get_working_years())
        bonus = str(self.get_bonus())
        return 'Name: '+self.name+', Age: '+str(self.age)+', Salary: '+str(self.salary)+', Working years: '+working_years+', Bonus: ' +bonus


def main():
    # main code here
    print("Welcome to HR Pro 2019 ")
    options = ['Show Employees','Show Managers','Add An Employee','Add A Manager','Exit']

    user_input = 0
    number = 1

    employee_list = []
    manager_list = []


    while user_input != 5:
        print("Options: ")
        for option in options:
            print("{}. {}".format(number , option))
            number +=1
        print()
        user_input = int(input("What would you like to do? "))
        print("------------------\n")
        if user_input == 1:
            print("Employees\n")
            if len(employee_list) == 0:
                print("Please add employee")
            else:
                for item in employee_list:
                    employee = Employee(name_emp,age_emp,salary_emp,employment_year_emp)
                print(employee.__str__())
            number=1
        elif user_input == 2:
            if len(manager_list) == 0:
                print("Please add manager")
            else:
                for item in manager_list:
                    manager = Manager(name_man,age_man,salary_man,employment_year_man,bonus_percentage_man)
                print(manager.__str__())
            number =1
        elif user_input == 3:
            name_emp = input("Name: ")
            age_emp = input("Age: ")
            salary_emp =input("Salary: ")
            employment_year_emp =int(input("Employment Year: "))
            added_employee = Employee(name_emp,age_emp,salary_emp,employment_year_emp)
            employee_list.append(added_employee)
            print("Employee added succesfully")
            number=1
        elif user_input == 4:
            name_man = input("Name: ")
            age_man = input("Age: ")
            salary_man = int(input("Salary: "))
            employment_year_man =int( input("Employment Year: "))
            bonus_percentage_man = float(input("Bonus Percentage: "))
            added_manager= Manager(name_man,age_man,salary_man,employment_year_man,bonus_percentage_man)
            manager_list.append(added_manager)
            print("Manager added succesfully")
            number=1



if __name__ == '__main__':
    main()
