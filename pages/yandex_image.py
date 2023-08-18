from selenium.webdriver.common.by import By
import time


class YandexImage:
    SERVICES = (By.XPATH, '/html/body/main/div[2]/form/nav/ul/li[10]')
    SEARCH_FIELD = (By.XPATH, '//*[@id="text"]')
    SERVICE_IMAGES = (By.XPATH, '/html/body/main/div[4]/div/div[1]/div/div[3]/div[1]/span[9]/a')
    IMAGES_PATH = (By.CSS_SELECTOR, 'head > link:nth-child(6)')
    FIRST_CATEGORY = (By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div[1]/a')
    FIRST_CATEGORY_NAME = (By.CSS_SELECTOR, '.serp-header')
    FIRST_IMAGE = (By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/a')
    FIRST_IMAGE_FULL_SCREEN = (By.CSS_SELECTOR, '.MMImageContainer')
    PUSH_FORWARD = (By.XPATH, '/html/body/div[14]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[4]/i')
    PUSH_BACK = (By.XPATH, '/html/body/div[14]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/i')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("https://ya.ru/")

    def is_element_present(self, locator):
        return len(self.browser.find_elements(*locator)) > 0

    def services_button_present(self):
        return self.is_element_present(self.SERVICES)
    
    def click_services(self):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        time.sleep(2)
        search_field.click()
        services = self.browser.find_element(*self.SERVICES)
        time.sleep(2)
        services.click()
        service_images = self.browser.find_element(*self.SERVICE_IMAGES)
        time.sleep(2)
        service_images.click()

    def is_images_link(self):
        return self.is_element_present(self.IMAGES_PATH)
        #return self.browser.current_url (проверка не проходила)
    
    def click_first_category(self):
        first_category = self.browser.find_element(*self.FIRST_CATEGORY)
        time.sleep(2)
        first_category.click()

    def is_first_category_name(self):
        return self.is_element_present(self.FIRST_CATEGORY_NAME)
    
    def click_first_image(self):
        first_image = self.browser.find_element(*self.FIRST_IMAGE)
        time.sleep(2)
        first_image.click()

    def is_first_image_full_screen(self):
        return self.is_element_present(self.FIRST_IMAGE_FULL_SCREEN)
    
    def push(self):
        push_forward = self.browser.find_element(*self.PUSH_FORWARD)
        time.sleep(2)
        push_forward.click()
        push_back = self.browser.find_element(*self.PUSH_BACK)
        time.sleep(2)
        push_back.click()
