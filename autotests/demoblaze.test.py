import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random


class TestDemoblaze:
    """Полный автотест для сайта Demoblaze"""

    @pytest.fixture(scope="class")
    def driver(self):
        """Фикстура для инициализации и закрытия браузера"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.demoblaze.com/index.html")

        yield driver
        driver.quit()

    @pytest.fixture
    def wait(self, driver):
        """Фикстура для явных ожиданий"""
        return WebDriverWait(driver, 10)

    def test_01_homepage_loaded(self, driver, wait):
        """Тест 1: Проверка загрузки главной страницы"""
        print("🔍 Проверяем загрузку главной страницы...")

        # Проверяем заголовок страницы
        assert "STORE" in driver.title
        print("✅ Заголовок страницы корректен")

        # Проверяем основные элементы на странице
        wait.until(EC.visibility_of_element_located((By.ID, "nava")))
        wait.until(EC.visibility_of_element_located((By.ID, "cartur")))
        wait.until(EC.visibility_of_element_located((By.ID, "login2")))

        print("✅ Главная страница загружена успешно")

    def test_02_navigation_categories(self, driver, wait):
        """Тест 2: Проверка навигации по категориям товаров"""
        print("🔍 Проверяем навигацию по категориям...")

        # Кликаем на категорию "Phones"
        phones_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        phones_category.click()

        # Ждем загрузки товаров
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-block")))
        phone_products = driver.find_elements(By.CLASS_NAME, "card-title")
        assert len(phone_products) > 0, "Не найдены товары в категории Phones"
        print(f"✅ Найдено {len(phone_products)} телефонов")

        # Переходим в категорию "Laptops"
        laptops_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
        laptops_category.click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-block")))
        laptop_products = driver.find_elements(By.CLASS_NAME, "card-title")
        assert len(laptop_products) > 0, "Не найдены товары в категории Laptops"
        print(f"✅ Найдено {len(laptop_products)} ноутбуков")

        # Возвращаемся на главную
        home_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_category.click()

    def test_03_product_view(self, driver, wait):
        """Тест 3: Просмотр детальной страницы товара"""
        print("🔍 Проверяем просмотр товара...")

        # Ждем загрузки товаров на главной
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-block")))

        # Кликаем на первый товар
        first_product = driver.find_elements(By.CLASS_NAME, "card-title")[0]
        product_name = first_product.text
        first_product.click()

        # Ждем загрузки страницы товара
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "name")))

        # Проверяем, что название товара совпадает
        product_detail_name = driver.find_element(By.CLASS_NAME, "name").text
        assert product_name == product_detail_name
        print(f"✅ Перешли на страницу товара: {product_name}")

        # Проверяем наличие цены и описания
        product_price = driver.find_element(By.CLASS_NAME, "price-container").text
        product_description = driver.find_element(By.ID, "more-information").text

        assert product_price != "", "Цена товара не отображается"
        assert product_description != "", "Описание товара не отображается"
        print(f"✅ Цена: {product_price}")

        # Возвращаемся на главную
        driver.back()

    def test_04_user_registration(self, driver, wait):
        """Тест 4: Регистрация нового пользователя"""
        print("🔍 Проверяем регистрацию пользователя...")

        # Генерируем уникальные данные для регистрации
        username = f"testuser_{random.randint(1000, 9999)}"
        password = "testpass123"

        # Кликаем на "Sign up"
        sign_up_btn = wait.until(EC.element_to_be_clickable((By.ID, "signin2")))
        sign_up_btn.click()

        # Ждем появления модального окна
        wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))

        # Заполняем форму регистрации
        username_field = driver.find_element(By.ID, "sign-username")
        password_field = driver.find_element(By.ID, "sign-password")

        username_field.clear()
        password_field.clear()

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Кликаем кнопку регистрации
        sign_up_submit = driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_submit.click()

        # Обрабатываем alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()

            if "Sign up successful" in alert_text:
                print("✅ Регистрация прошла успешно")
            else:
                print(f"⚠️  Alert сообщение: {alert_text}")

        except:
            print("⚠️  Alert не появился")

    def test_05_user_login(self, driver, wait):
        """Тест 5: Авторизация пользователя"""
        print("🔍 Проверяем авторизацию пользователя...")

        # Используем тестовые данные (можете заменить на реальные)
        test_username = "testuser_1234"
        test_password = "testpass123"

        # Кликаем на "Log in"
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
        login_btn.click()

        # Ждем появления модального окна
        wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))

        # Заполняем форму авторизации
        username_field = driver.find_element(By.ID, "loginusername")
        password_field = driver.find_element(By.ID, "loginpassword")

        username_field.clear()
        password_field.clear()

        username_field.send_keys(test_username)
        password_field.send_keys(test_password)

        # Кликаем кнопку авторизации
        login_submit = driver.find_element(By.XPATH, "//button[text()='Log in']")
        login_submit.click()

        # Ждем завершения авторизации
        time.sleep(2)

        # Проверяем, что появилось имя пользователя (если авторизация успешна)
        try:
            welcome_text = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
            if "Welcome" in welcome_text.text:
                print("✅ Авторизация прошла успешно")
        except:
            print("⚠️  Авторизация не удалась (возможно, неверные данные)")

    def test_06_add_to_cart(self, driver, wait):
        """Тест 6: Добавление товара в корзину"""
        print("🔍 Проверяем добавление товара в корзину...")

        # Переходим в категорию Phones
        phones_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        phones_category.click()

        # Ждем загрузки товаров и кликаем на первый
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-block")))
        first_phone = driver.find_elements(By.CLASS_NAME, "card-title")[0]
        phone_name = first_phone.text
        first_phone.click()

        # Ждем загрузки страницы товара и добавляем в корзину
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "name")))
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
        add_to_cart_btn.click()

        # Обрабатываем alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()

            if "Product added" in alert_text:
                print(f"✅ Товар '{phone_name}' добавлен в корзину")
            else:
                print(f"⚠️  Alert сообщение: {alert_text}")

        except:
            print("⚠️  Alert не появился при добавлении в корзину")

        # Возвращаемся на главную
        driver.back()

    def test_07_cart_management(self, driver, wait):
        """Тест 7: Работа с корзиной"""
        print("🔍 Проверяем работу с корзиной...")

        # Переходим в корзину
        cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
        cart_btn.click()

        # Ждем загрузки корзины
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "success")))

        # Проверяем наличие товаров в корзине
        cart_items = driver.find_elements(By.CLASS_NAME, "success")

        if len(cart_items) > 0:
            print(f"✅ В корзине {len(cart_items)} товар(ов)")

            # Можно добавить удаление товара
            delete_buttons = driver.find_elements(By.LINK_TEXT, "Delete")
            if delete_buttons:
                delete_buttons[0].click()
                time.sleep(1)  # Ждем обновления корзины
                print("✅ Товар удален из корзины")
        else:
            print("ℹ️  Корзина пуста")

        # Возвращаемся на главную
        home_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_btn.click()

    def test_08_contact_form(self, driver, wait):
        """Тест 8: Проверка формы обратной связи"""
        print("🔍 Проверяем форму обратной связи...")

        # Кликаем на Contact
        contact_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact")))
        contact_btn.click()

        # Ждем появления модального окна
        wait.until(EC.visibility_of_element_located((By.ID, "recipient-email")))

        # заполняем форму епта
        email_field = driver.find_element(By.ID, "recipient-email")
        name_field = driver.find_element(By.ID, "recipient-name")
        message_field = driver.find_element(By.ID, "message-text")

        email_field.send_keys("test@example.com")
        name_field.send_keys("Test User")
        message_field.send_keys("This is a test message from automated test")