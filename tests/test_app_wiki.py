from qa_guru_python_21.models.pages.mobile.search_page import search_page


def test_search():
    search_page.search('Appium')
    search_page.should_results('Appium')


def test_open_page():
    search_page.search('Python')
    search_page.open_page()
