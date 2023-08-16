import pytest
from selenium import webdriver
from pages.yandex_page import YandexPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_yandex_search(browser):
    yandex_page = YandexPage(browser)
    
    yandex_page.open()
    assert yandex_page.is_search_field_present(), "Поле поиска не найдено"
    
    yandex_page.enter_search_query("Тензор")
    assert yandex_page.is_search_suggestions_table_present(), "Таблица с подсказками не найдена"
    
    yandex_page.press_enter()
    assert yandex_page.is_search_results_page_present(), "Страница результатов поиска не найдена"
    
    assert yandex_page.get_first_search_result_url() == "https://tensor.ru/", "Первая ссылка не ведет на tensor.ru"




