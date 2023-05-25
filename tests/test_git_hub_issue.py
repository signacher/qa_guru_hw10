import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

'''
Чистый Selene(без шагов)
'''
def test_github():
    browser.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("signacher/qa_guru_hw8")
    s(".header-search-input").submit()

    s(by.link_text("signacher/qa_guru_hw8")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)


'''
Лямбда шаги через with allure.step
'''
def test_dynamic_steps():
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем вкладку Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue #81'):
        s(by.partial_text('#81')).should(be.visible)


'''
C декоратором @allure.step
'''
def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_issue_with_number('#81')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').type(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем вкладку Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue {number}')
def should_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)


'''
Разметка тестов всеми аннотациями
'''
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Telnov')
@allure.feature('Repo issues')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Github')
def test_decorator_steps_issue():
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем вкладку Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue #81'):
        s(by.partial_text('#81')).should(be.visible)