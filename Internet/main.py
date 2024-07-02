import os

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

# Укажите директорию установки Firefox
install_dir = "/snap/firefox/current/usr/lib/firefox"
driver_loc = os.path.join(install_dir, "geckodriver")
binary_loc = os.path.join(install_dir, "firefox")

# Настройка сервисов и опций
service = FirefoxService(driver_loc)
opts = webdriver.FirefoxOptions()
opts.binary_location = binary_loc
# opts.add_argument("--headless")  # Если нужно запускать в headless режиме

# Инициализация веб-драйвера
driver = webdriver.Firefox(service=service, options=opts)

try:
    # Шаг 1: Открытие веб-страницы
    print("Шаг 1: Открытие веб-страницы")
    driver.get("https://example.com")
    driver.implicitly_wait(10)  # Даем время странице загрузиться

    # Шаг 2: Работа с LocalStorage
    print("Шаг 2: Работа с LocalStorage")
    # Установка значения в LocalStorage
    print("Установка значения в LocalStorage")
    driver.execute_script("window.localStorage.setItem('myKey', 'myValue');")
    # Получение значения из LocalStorage
    local_storage_value = driver.execute_script("return window.localStorage.getItem('myKey');")
    print("Полученное значение из LocalStorage:", local_storage_value)
    # Удаление значения из LocalStorage
    print("Удаление значения из LocalStorage")
    driver.execute_script("window.localStorage.removeItem('myKey');")
    local_storage_value = driver.execute_script("return window.localStorage.getItem('myKey');")
    print("Значение из LocalStorage после удаления:", local_storage_value)

    # Шаг 3: Работа с Cookies
    print("Шаг 3: Работа с Cookies")
    # Установка значения в cookies
    print("Установка значения в Cookies")
    driver.add_cookie({"name": "myCookie", "value": "myCookieValue"})
    # Получение значения из cookies
    cookie_value = driver.get_cookie("myCookie")
    print("Полученное значение из Cookies:", cookie_value)
    # Удаление значения из cookies
    print("Удаление значения из Cookies")
    driver.delete_cookie("myCookie")
    cookie_value = driver.get_cookie("myCookie")
    print("Значение из Cookies после удаления:", cookie_value)

finally:
    # Шаг 4: Закрытие браузера
    print("Шаг 4: Закрытие браузера")
    driver.quit()
