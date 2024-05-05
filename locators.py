from selenium.webdriver.common.by import By


class TestLocators:
    # Ссылка "Личный кабинет" на главной странице
    PERSONAL_AREA_LINK = By.XPATH, "//p[text()='Личный Кабинет']"

    # Ссылка "Зарегистрироваться" на странице авторизации
    REGISTRATION_LINK = By.XPATH, "//a[text()='Зарегистрироваться']"

    # Поле "Имя" на странице регистрации
    INPUT_NAME_FOR_REGISTRATION = By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']"

    # Поле "Email" на странице регистрации
    INPUT_EMAIL_FOR_REGISTRATION = By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"

    # Поле "Пароль" на странице регистрации
    INPUT_PASSWORD_FOR_REGISTRATION = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

    # Кнопка "Зарегистрироваться" на странице регистрации
    BUTTON_REGISTRATION = By.XPATH, "//button[text()='Зарегистрироваться']"

    # Кнопка "Вход" на странице авторизации
    BUTTON_LOGIN_AUTH = By.CSS_SELECTOR, ".button_button__33qZ0"

    # Сообщение об ошибке при неверном пароле на странице регистрации
    MESSAGE_ERROR_PASSWORD = By.CSS_SELECTOR, ".input__error"

    # Кнопка "Войти в аккаунт" на главной странице
    BUTTON_ENTER_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']"

    # Поле "Email" на странице авторизации
    INPUT_EMAIL_TO_ENTER = By.XPATH, "//input[@type='text' and @name='name']"

    # Поле "Пароль" на странице авторизации
    INPUT_PASSWORD_TO_ENTER = By.XPATH, "//input[@type='password' and @name='Пароль']"

    # Кнопка "Оформить заказ" на главной странице
    BUTTON_MAKE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"

    # Кнопка-ссылка "Личный кабинет" на главной странице
    PERSONAL_AREA = By.XPATH, "//a[.='Личный Кабинет']"

    # Кнопка "Войти" на странице регистрации
    BUTTON_LOGIN_AUTH_REG = By.CSS_SELECTOR, ".Auth_link__1fOlj"

    # Ссылка "Восстановить пароль" на странице авторизации
    LINK_TO_RECOVER_PASSWORD = By.XPATH, "//a[.='Восстановить пароль']"

    # Кнопка "Войти" на странице восстановления пароля
    BUTTON_LOGIN_ON_RECOVER_PASSWORD_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj"

    # Кнопка "Восстановить" на странице восстановления пароля
    BUTTON_RECOVER_PASSWORD = By.XPATH, "//button[text()='Восстановить']"

    # Раздел "Профиль" в личном кабинете пользователя
    BLOCK_USER_PROFILE = By.CSS_SELECTOR, ".Account_link__2ETsJ"

    # Кнопка "Конструктор" на шапке сайта
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"

    # Логотип Stellars burgers
    LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"

    # Кнопка "Выход" в личном кабинете пользователя
    BUTTON_EXIT = By.XPATH, "//button[@type='button' and text()='Выход']"

    # Вкладка "Булки" в конструкторе
    TAB_BUNS = By.XPATH, "//div[.='Булки']"

    # Вкладка "Соусы" в конструкторе
    TAB_SAUSES = By.XPATH, "//div[.='Соусы']"

    # Вкладка "Начинки" в конструкторе
    TAB_FILLINGS = By.XPATH, "//div[.='Начинки']"
