from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    search_input_locator = (By.ID, "store_nav_search_term")
    common_menu_bar_locator = "//div[@class='store_nav']//a[contains(text(),'{}')]"
    list_of_sub_menu_bar_elements_locator = (By.CLASS_NAME, "popup_menu_item")

    def search(self, search_value):
        self.driver.find_element(*MainPage.search_input_locator).send_keys(search_value)
        self.driver.find_element(*MainPage.search_input_locator).send_keys(Keys.RETURN)

    def get_menu_bar_element(self, element_name):
        menu_bar_locator = self.common_menu_bar_locator.format(element_name)
        store_menu_bar_element = self.driver.find_element(By.XPATH, menu_bar_locator)
        return store_menu_bar_element

    def get_sub_menu_bar_elements_list(self, element_name):
        element = self.get_menu_bar_element(element_name)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        list_of_sub_menu_bar_elements = self.driver.find_elements(*MainPage.list_of_sub_menu_bar_elements_locator)
        menu_bar_sub_element_list = []
        for element_name in list_of_sub_menu_bar_elements:
            text = element_name.text
            menu_bar_sub_element_list.append(text)
        return menu_bar_sub_element_list
