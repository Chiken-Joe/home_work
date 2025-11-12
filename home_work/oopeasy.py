

class CoffeeMachine:
    def __init__(self):
        self.water_level = 1000
        self.coffee_beans = 500

    def make_espresso(self):
        if self.water_level >= 50 and self.coffe_beans >= 30:
            self.water_level -= 50
            self.coffee_beans -= 30
            print("Ваш эспрессо готов")
        else:
            print("Нехватка ресурсов")

    def show_status(self):
        print(f"Уровень воды: {self.water_level} мл")
        print(f"Уровень кофе: {self.coffee_beans} мл")


class BankAccount:
    def __init__(self, owner_name: str, initial_balance:int = 0):
        self.owner_name = owner_name
        self.balance = initial_balance
        print(f"Создан счет для {self.owner_name} с начальным балансом {self.balance} рублс")

    def deposit(self, amount):
        self.balance += amount
        print(f"На счет зачислено {amount} рублс. Новый баланс {self.balance} рублс")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств для операции")
        print(f"Со счета было снято {amount} рублс. Текущий баланс {self.balance}")

    def get_balance(self):
        print(f"Текущий баланс составляет: {self.balance} рублс")


class User:
    def __init__ (self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
        self.is_admin = False

    def  deactivate(self):
        self.is_active = False
        print("пип пип пип...Пользователь диактевейтед бичез")

    def make_admin(self):
        self.is_admin = True
        print("Оскорбление админа - бан,оскорбление мамы админа - бан + расстрел")

    def get_info(self):
        info = f"Пользователь {self.username}, Email: {self.email}, Активен: {self.is_active}, Админ: {self.is_admin}"
        print(info)

class Shop:
    sales_tax = 0.05

    def __init__(self, location, inventory:dict = {'яблоки': 100} ):
        self.location = location
        self.inventory = inventory

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory [item] += quantity
        else:
            self.inventory[item] = quantity

    def calculate_price(self, item, quantity):
        price = {'яблоки': 10, 'груши': 15}
        price_per_item = price[item]
        total_price = (price_per_item * quantity) * (1 + self.sales_tax)
        print(f"Итоговая цена с налогом: {total_price:.2f}")


class Vehicle:

    def __init__(self, brand , max_speed):
        self.current_speed = 0
        self.brand = brand
        self.max_speed = max_speed

    def start_engine(self):
        print(f"У машины марки {self.brand} запущен двигатель")

    def  accelerate(self, speed_increase):
        self.current_speed += speed_increase
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
            print(f"ЯРИК,БЛЯТЬ,БАЧОК ПОТИК: {self.max_speed} км/ч")
        else:
            print(f"Текущая скорость: {self.current_speed} км/ч")


class Car(Vehicle):

    def beep(self):
        print("Би-бип!")

    def __init__(self, brand, max_speed):
        super().__init__(brand, max_speed)


class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print("Сотрудник: [name], Зарплата: [salary]")


class Manager(Employee):

    def __init__(self, name, salary, department):
        self.department = department
        super().__init__(name, salary)

    def get_details(self):
        print("Менеджер: [name], Зарплата: [salary], Отдел: [departamen]")


class Weepon():
    damage = 10

    def attack(self):
        print("Нанесен урон: {self.damage}")


class Sword(Weepon):

    def __init__(self, damage = 25):
        self.damage = damage

    def attack(self):
        print("Удар мечом! Нанесен урон: {self.damage}")

class Bow(Weepon):

    def __init__(self, damage = 15):
        self.damage = damage

    def attack(self):
        print("Выстрел из лука в глаз! Нанесен урон: {self.damage}")


class TestCase():
    name = ""
    status = 'Not Run'

    def run_test(self):
        self.status = "Passed"

    def fail_test(self):
        self.status = "Failed"

    def get_info(self):
        print("Test: [self.name], status: [self.status].")


class BugReport():

    def __init__(self, title, reporter, priority = "Medium"):
        self.title = title
        self.reporter = reporter
        self.priority = priority
    # def update_priority(new_priority):


class TestEnvironment():
    default_browser = 'Chrome'

    def __init__(self, base_url ):
        self.base_url = base_url

    def get_details(self):
        print("Адрес: [self.base_url], браузер: [default_browser]")


class BasePage():

    def __init__(self, driver ):
        self.driver = driver

    def  open_url(url):
        print("Opening [url] using [self.driver]")

class LoginPage(BasePage):

    def login(username, password):
        print("Logging in with [username]")


class ApiRequest():

    def send(self):
        print("Error: Method not implemented")

class GetRequest(ApiRequest):

    def send(self):
        print("Sending GET request...")

class PostRequest(ApiRequest):

    def send(self):
        print("Sending POST request...")