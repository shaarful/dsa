from abc import abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __get_dob(self):
        pass

    # Create abstract method
    @abstractmethod
    def print_details(self):
        pass

    @staticmethod
    def say_hello():
        print("hello")


class Employee(Person):
    # increment rate for all employee
    increment_rate = 0.1
    total_employee = 0
    __org_name = "FAO"

    def __init__(self, name, age, salary, mobile_no):
        super().__init__(name, age)
        self.__salary = salary
        self._mobile_no = mobile_no
        Employee.total_employee += 1

    def print_details(self):
        pass

    @classmethod
    def get_organization_name(cls):
        return cls.__org_name

    @property
    def email(self):
        return f"{self.name}@sharful.com"

    @email.setter
    def email(self, email):
        self.email = email

    @email.deleter
    def email(self):
        del self.email

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def increment(self):
        self.__salary += self.__salary * self.increment_rate


class Developer(Employee):
    increment_rate = 0.2

    def __int__(self, name, age, salary, mobile_no, language):
        super().__init__(name, age, salary, mobile_no)
        self.language = language


class Manager(Employee):
    increment_rate = 0.25

    def __init__(self, name, age, salary, mobile_no, no_of_employee=0):
        super().__init__(name, age, salary, mobile_no)
        self.no_of_employee = no_of_employee


mgr1 = Manager('sharful', 29, 20000, 123456)
dev1 = Developer("Dev1", 22, 2000, 1234)

# print(emp1.s)
Manager.say_hello()

print(Employee)
