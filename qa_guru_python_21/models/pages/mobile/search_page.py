from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:

    with step('Type search'):

        def search(self, text):
            browser.element(
                (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element(
                (AppiumBy.ID,
                 "org.wikipedia.alpha:id/search_src_text")).type(text)

    with step('open page'):

        def open_page(self):
            browser.element(
                (AppiumBy.ID,
                 "org.wikipedia.alpha:id/page_list_item_title")).click()

        def should_results(self, text):
            results = browser.all(
                (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(text))


search_page = SearchPage()
