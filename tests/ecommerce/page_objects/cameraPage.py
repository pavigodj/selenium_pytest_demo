from selenium.webdriver.common.by import By

class CameraPage:

    def __init__(self,driver):
        self.driver = driver

    cameraNames = (By.XPATH,"//div[@class='caption']")

    def camerasName(self):
        return self.driver.find_elements(*CameraPage.cameraNames)

    