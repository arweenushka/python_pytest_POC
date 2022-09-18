from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver

    results_locator = (By.XPATH, "//div[contains(@id,'search_resultsRows')]//a")
    search_input_locator = (By.XPATH, "//input[contains(@id,'realterm')]")

    def get_results_amount(self):
        return len(self.driver.find_elements(*ResultsPage.results_locator))

    def get_search_input_text(self):
        search_input = self.driver.find_element(*ResultsPage.search_input_locator)
        search_input_text = search_input.get_attribute("value")
        return search_input_text
