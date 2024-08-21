from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_ORDER_BUTTON = (By.XPATH, f"//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    HOME_ORDER_BUTTON = (By.XPATH, f"//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
