from pages.swag_labs import SwagLabs

def testCheckIcon(browser):

    swag_lab = SwagLabs(browser)
    swag_lab.exist_icon()
    swag_lab.exist_login()
    swag_lab.exist_password()

