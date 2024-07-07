from Utility.Baseclass import BaseClass
from PageObjects.cameraPage import CameraPage
from PageObjects.HomePage import HomePage


class Test_CameraPage(BaseClass):

    def test_navigation(self):
        homePage = HomePage(self.driver)
        cameraPageobj = homePage.cameraClick()
        print("test_navigation test case")
        title = self.driver.title
        assert title == "Cameras", "Window Title doesnt match"


