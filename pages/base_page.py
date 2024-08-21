from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def open_page(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_and_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_and_click(self, by, value):
        locator = (by, value)
        self.scroll_to_element(locator)
        self.wait_and_find_element(locator).click()

    def get_text_from_element(self, by, value):
        locator = (by, value)
        element = self.wait_and_find_element(locator)
        return element.text

    def switch_to_new_tab_and_wait_for_url(self, expected_url):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        # Ждем, пока URL не станет равен ожидаемому
        WebDriverWait(self.driver, 15).until(ec.url_to_be(expected_url))

    def scroll_and_click(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator)
        ).click()


