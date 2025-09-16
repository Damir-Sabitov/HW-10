from selene import browser,have,by
from selene.support.shared.jquery_style import s
import allure
from allure import severity_level

@allure.tag("web")
@allure.severity(severity_level.CRITICAL)
@allure.label("owner", "Sabitov-Damir")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com/Damir-Sabitov/home_work_7", name="Репозиторий HW7")

def test_find_issue_annotation():
    browser.open("https://github.com")
    s('.search-input').click()
    s('#query-builder-test').send_keys("Damir-Sabitov/home_work_7")
    s('#query-builder-test').submit()
    s(by.link_text('Damir-Sabitov/home_work_7')).click()
    browser.element('#issues-tab').click()
    browser.element('.ListView-module__ul--A_8jF').should(have.text('Test issue for HW10'))