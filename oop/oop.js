class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    get_dob() {
    }

    print_details() {
    }

    static say_hello() {
        console.log("hello")
    }
}

class Employee extends Person {
    // increment rate for all employee
    static increment_rate = 0.1
    static total_employee = 0
    static org_name = "FAO"


    constructor(name, age, salary, mobile_no) {
        super(name, age);
        this.__salary = salary
        this._mobile_no = mobile_no
        Employee.total_employee += 1
    }

    print_details() {
    }



    static get_organization_name() {
        return Employee.org_name
    }

    get email() {
        return `${this.name}@sharful.com`
    }


    set email(email) {
        this.email = email
    }

    get_salary() {
        return this.__salary
    }

    set_salary(salary) {
        this.__salary = salary
    }

    increment() {
        self.__salary += self.__salary * self.increment_rate
    }
}

class Developer extends Employee {
    static increment_rate = 0.2

    constructor(name, age, salary, mobile_no, language) {
        super(name, age, salary, mobile_no)
        this.language = language
    }
}

class Manager extends Employee {
    static increment_rate = 0.25

    constructor(name, age, salary, mobile_no, no_of_employee = 0) {
        super(name, age, salary, mobile_no)
        this.no_of_employee = no_of_employee
    }

}

mgr1 = new Manager('sharful', 29, 20000, 123456)
dev1 = new Developer("Dev1", 22, 2000, 1234)


Manager.say_hello()
console.log(Manager.total_employee);
console.log(Manager.increment_rate);
console.log(mgr1.email);
console.log(dev1.email);


