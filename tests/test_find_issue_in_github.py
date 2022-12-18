from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
import allure
from allure_commons.types import Severity
from allure import attachment_type


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "szaytsev")
@allure.feature("Задачи в репозитории")
@allure.story("Поиск issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_find_name_issue(set_window_size):
    browser.open("https://github.com")

    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "szaytsev")
@allure.feature("Задачи в репозитории")
@allure.story("Пример лямбда шагов")
@allure.link("https://github.com", name="Testing")
def test_lambda_steps(set_window_size):
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)
    allure.attach("Это пример лямбда шагов allure", name="Text", attachment_type=attachment_type.TEXT)

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "szaytsev")
@allure.feature("Задачи в репозитории")
@allure.story("Пример шагов с декоратором")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps(set_window_size):
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")
    allure.attach("Это пример шагов с декоратором allure", name="Text", attachment_type=attachment_type.TEXT)


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).click()
