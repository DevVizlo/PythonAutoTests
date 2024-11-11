from pages.base_page import BasePage
from selenium.common import NoSuchFrameException

class SwagLabs(BasePage):

    def ExistIcon(self):
        try:
            self.findElement(locator='div.login_logo')
        except NoSuchFrameException:
            return False
        return True

    def ExistLogin(self):
        try:
            self.findElement(locator='#user-name')
        except NoSuchFrameException:
            return False
        return True

    def ExistPassword(self):
        try:
            self.findElement(locator='#password')
        except NoSuchFrameException:
            return False
        return True