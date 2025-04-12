from selenium.webdriver.common.by import By
from GZ2023test.testguosai.ERP_PO.Website.test_case.page_object.BasePage import BasePage
class LogingPage(BasePage):
    yhm_loc = (By.CLASS_NAME, "username")
    mm_loc = (By.NAME, "password")
    dl_loc = (By.ID, "signIn")
    def send_yhm(self,username):
        self.find_element(self.yhm_loc).send_keys(username)
    def send_mm(self,password):
        self.find_element(self.mm_loc).send_keys(password)
    def click_dl(self):
        self.find_element(self.dl_loc).click()
def test_denglu(driver,username,password):
    db = LogingPage(driver)
    db.get_url()
    db.send_yhm(username)
    db.send_mm(password)
    db.click_dl()