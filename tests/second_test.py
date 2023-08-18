import pytest
from selenium import webdriver
from pages.yandex_image import YandexImage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()

def test_yandex_images(browser):
    yandex_page = YandexImage(browser)
    
    yandex_page.open()
    assert yandex_page.services_button_present(), "Кнопка меню не найдена"
    
    yandex_page.click_services()
    assert yandex_page.is_images_link(), "Текущий адрес не соответствует https://ya.ru/images/"

    yandex_page.click_first_category()
    assert yandex_page.is_first_category_name(), "Имя категории не отображается"

    yandex_page.click_first_image()
    assert yandex_page.is_first_image_full_screen(), "Картинка не отобразилась"

    yandex_page.push()
    assert yandex_page.is_first_image_full_screen(), "Отображается не первая картинка"

