from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YandexPage:
    SEARCH_FIELD = (By.XPATH, '//*[@id="text"]')
    SEARCH_SUGGESTIONS_TABLE = (By.CSS_SELECTOR, '.search3')
    SEARCH_RESULTS_PAGE = (By.CSS_SELECTOR, '.main__content')
    FIRST_SEARCH_RESULT_LINK = (By.XPATH, '/html/body/main/div[2]/div[2]/div/div[1]/ul/li[1]/div/div[1]/a')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("https://ya.ru/")

    def is_element_present(self, locator):
        return len(self.browser.find_elements(*locator)) > 0

    def is_search_field_present(self):
        return self.is_element_present(self.SEARCH_FIELD)

    def is_search_suggestions_table_present(self):
        return self.is_element_present(self.SEARCH_SUGGESTIONS_TABLE)

    def is_search_results_page_present(self):
        return self.is_element_present(self.SEARCH_RESULTS_PAGE)

    def enter_search_query(self, query):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(query)

    def press_enter(self):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(Keys.RETURN)

    def get_first_search_result_url(self):
        first_result_link = self.browser.find_element(*self.FIRST_SEARCH_RESULT_LINK)
        return first_result_link.get_attribute("href")