from selenium.webdriver.common.by import By

class OrderPageLocators:
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = lambda station: (By.XPATH, f"//div[text()='{station}']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()= 'Далее']")
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    LEASE_TERM = (By.XPATH, "//div[text()='* Срок аренды']")
    TERM_OPTION = lambda term: (By.XPATH, f"//div[text()='{term}']")
    SCOOTER_COLOR = (By.XPATH, "//label[text()='чёрный жемчуг']")
    ORDER_POP_UP = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_CONFIRM_POP_UP = (By.XPATH, "//div[text()='Заказ оформлен']")
    BODY = (By.XPATH, "//body")
    ORDER_BUTTON = (By.XPATH, f"//div[contains(@class, 'Order_Buttons')]/button[text()= 'Заказать']")


