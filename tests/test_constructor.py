from locators import TestLocators


class TestConstructor:
    # Переход на вкладку "Соусы"
    def test_move_to_sauses(self, driver):
        driver.find_element(*TestLocators.TAB_SAUSES).click()
        data_sauses = driver.find_element(*TestLocators.TAB_SAUSES)
        assert 'tab_tab_type_current__2BEPc' in data_sauses.get_attribute("class")

    # Переход на вкладку "Начинки"
    def test_move_to_fillings(self, driver):
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        data_fillings = driver.find_element(*TestLocators.TAB_FILLINGS)
        assert 'tab_tab_type_current__2BEPc' in data_fillings.get_attribute("class")

    # Переход с вкладки "Булки" и возврат на эту вкладку
    def test_move_to_buns(self, driver):
        driver.find_element(*TestLocators.TAB_SAUSES).click()
        driver.find_element(*TestLocators.TAB_BUNS).click()
        data_buns = driver.find_element(*TestLocators.TAB_BUNS)
        assert 'tab_tab_type_current__2BEPc' in data_buns.get_attribute("class")
