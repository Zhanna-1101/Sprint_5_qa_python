from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Url, ValidData
from locators import TestLocators


class TestMovePersonalArea:
    # Переход в личный кабинет при нажатии кнопки "Личный Кабинет" на главной странице
    def test_move_to_personal_area(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.MAIN_PAGE_URL))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.PROFILE_PAGE_URL))
        user_profile = driver.find_element(*TestLocators.BLOCK_USER_PROFILE)
        assert driver.current_url == Url.PROFILE_PAGE_URL and user_profile.text == 'Профиль'

    # Переход в конструктор из личного кабинета при нажатии на кнопку "Конструктор"
    def test_move_to_constructor_from_personal_area(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.MAIN_PAGE_URL))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.PROFILE_PAGE_URL))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))
        button_order = driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        assert driver.current_url == Url.MAIN_PAGE_URL and button_order.text == 'Оформить заказ'

    # Переход в конструктор из личного кабинета при нажатии на логотип
    def test_move_to_constructor_by_logo_from_personal_area(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.MAIN_PAGE_URL))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.PROFILE_PAGE_URL))
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))
        button_order = driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        assert driver.current_url == Url.MAIN_PAGE_URL and button_order.text == 'Оформить заказ'

    # Выход из личного кабинета пользователя
    def test_logout_from_personal_area(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        driver.find_element(*TestLocators.INPUT_EMAIL_TO_ENTER).send_keys(ValidData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_TO_ENTER).send_keys(ValidData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.MAIN_PAGE_URL))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.PROFILE_PAGE_URL))
        driver.find_element(*TestLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Url.LOGIN_PAGE_URL))
        login_button =  driver.find_element(*TestLocators.BUTTON_LOGIN_AUTH)
        assert driver.current_url == Url.LOGIN_PAGE_URL and login_button.text == 'Войти'
