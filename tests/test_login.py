from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Url, ValidData
from locators import TestLocators


class TestLogin:
    # Вход по внопке "Войти в аккаунт" на главной странице
    def test_login_on_main_page(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))
        button_order = driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        assert driver.current_url == Url.MAIN_PAGE_URL and button_order.text == 'Оформить заказ'

    # Вход через кнопку «Личный кабинет»
    def test_login_by_personal_area(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))
        button_order = driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        assert driver.current_url == Url.MAIN_PAGE_URL and button_order.text == 'Оформить заказ'

    # Вход через кнопку в форме регистрации
    def test_login_on_register_page(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.REGISTER_PAGE_URL))
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH_REG).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))
        button_order = driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        assert driver.current_url == Url.MAIN_PAGE_URL and button_order.text == 'Оформить заказ'

    # Вход через кнопку в форме восстановления пароля
    def test_login_on_forgot_password_page(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.LINK_TO_RECOVER_PASSWORD).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_RECOVER_PASSWORD))
        driver.find_element(*TestLocators.BUTTON_LOGIN_ON_RECOVER_PASSWORD_PAGE).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))
        button_order = driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        assert driver.current_url == Url.MAIN_PAGE_URL and button_order.text == 'Оформить заказ'
