from selenium.webdriver.common.by import By
from config import Config


class Locators:

    HEADER_ORDER_BUTTON = (By.XPATH, f"//div[contains(@class, 'Header_Nav')]/button[text()='{Config.ORDER_TEXT}']")
    HOME_ORDER_BUTTON = (By.XPATH, f"//div[contains(@class, 'Home_FinishButton')]/button[text()='{Config.ORDER_TEXT}']")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    ORDER_BUTTON = (By.XPATH, f"//div[contains(@class, 'Order_Buttons')]/button[text()= '{Config.ORDER_TEXT}']")
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()= 'Далее']")
    RENT_FORM = (By.XPATH,  "//div[text()='Про аренду'")
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    LEASE_TERM = (By.XPATH, "//div[text()='* Срок аренды']")
    SCOOTER_COLOR = (By.XPATH, "//label[text()='чёрный жемчуг']")
    ORDER_POP_UP = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_CONFIRM_POP_UP = (By.XPATH, "//div[text()='Заказ оформлен']")
