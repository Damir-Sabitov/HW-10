import allure
from selene import browser,have,by
from selene.support.shared.jquery_style import s

def test_find_issue_with_decorator():
    open_main_page()
    search_repo("Damir-Sabitov/home_work_7")
    click_repo("Damir-Sabitov/home_work_7")
    click_issues()
    check_issue()


@allure.step("Открываем главную страницу")
def open_main_page():
     browser.open("https://github.com")

@allure.step("Ищем репозиторий {repo}")
def search_repo(repo):
    s('.search-input').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()

@allure.step("Переходим по ссылке репозитория {repo}")
def click_repo(repo):
    s(by.link_text(repo)).click()

@allure.step("Переходим на вкладку issues")
def click_issues():
    browser.element('#issues-tab').click()

@allure.step("Проверка наличия issue с именем Test issue for HW10")
def check_issue():
    browser.element('.ListView-module__ul--A_8jF').should(have.text('Test issue for HW10'))


