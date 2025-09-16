import allure
from selene import browser,have,by
from selene.support.shared.jquery_style import s

def test_find_issue_with_allure_step():
    with allure.step("Открываем главую страницу GitHub"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий Damir-Sabitov/home_work_7"):
        s('.search-input').click()
        s('#query-builder-test').send_keys("Damir-Sabitov/home_work_7")
        s('#query-builder-test').submit()

    with allure.step("Ищем репозиторий"):
        s(by.link_text('Damir-Sabitov/home_work_7')).click()

    with allure.step("Переходим на вкладку issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверка наличия issue с именем Test issue for HW10"):
        browser.element('.ListView-module__ul--A_8jF').should(have.text('Test issue for HW10'))


