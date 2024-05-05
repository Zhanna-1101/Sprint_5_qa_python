import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Url
import data_creator
from locators import TestLocators


class TestRegistration:
    # Успешная регистрация при заполнении имени, логина (e-mail), пароля
    def test_success_registration_with_name_login_password(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA_LINK).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REGISTRATION).send_keys(data_creator.create_name())
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_REGISTRATION).send_keys(data_creator.create_email())
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REGISTRATION).send_keys(data_creator.create_password())
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        assert driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).is_displayed()

    # Тест с незаполненным именем
    def test_fail_registration_without_name(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA_LINK).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_REGISTRATION).send_keys(data_creator.create_email())
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REGISTRATION).send_keys(data_creator.create_password())
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert driver.current_url == Url.REGISTER_PAGE_URL and driver.find_element(*TestLocators.BUTTON_REGISTRATION).is_displayed()

    # Тест с незаполненным логином
    @pytest.mark.parametrize('login', ["", "test_test@", "test_test@y a.ru"])
    def test_fail_registration_with_wrong_login(self, driver, login):
        driver.find_element(*TestLocators.PERSONAL_AREA_LINK).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REGISTRATION).send_keys(data_creator.create_name())
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REGISTRATION).send_keys(login)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REGISTRATION).send_keys(data_creator.create_password())
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert driver.current_url == Url.REGISTER_PAGE_URL and driver.find_element(*TestLocators.BUTTON_REGISTRATION).is_displayed()

    # Тест без ввода пароля
    def test_fail_registration_without_password(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA_LINK).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REGISTRATION).send_keys(data_creator.create_name())
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_REGISTRATION).send_keys(data_creator.create_email())
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert driver.current_url == Url.REGISTER_PAGE_URL and driver.find_element(*TestLocators.BUTTON_REGISTRATION).is_displayed()

    # Тест с паролем менее 6-ти символов
    def test_fail_registration_with_password_from_5_symbols(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA_LINK).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REGISTRATION).send_keys(data_creator.create_name())
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_REGISTRATION).send_keys(data_creator.create_email())
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REGISTRATION).send_keys(data_creator.create_password_from_5_symbols())
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        message_error = driver.find_element(*TestLocators.MESSAGE_ERROR_PASSWORD)
        assert driver.find_element(*TestLocators.BUTTON_REGISTRATION).is_displayed() and message_error.text == 'Некорректный пароль'
