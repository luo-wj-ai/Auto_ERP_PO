from selenium.webdriver.common.by import By
from GZ2023test.testguosai.ERP_PO.Website.test_case.page_object.BasePage import BasePage
import time
class AddPage(BasePage):
    text1 = (By.PARTIAL_LINK_TEXT, "商品分类")
    text2 = (By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > div.mb8.el-row > div:nth-child(3) > button")
    text3 = (By.XPATH, "//input[@placeholder='请输入商品分类名称']")
    text4 = (By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium")
    text5 = (By.CLASS_NAME, "el-message__content")
    text6 = (By.CLASS_NAME, "el-form-item__error")
    def click_brand(self):
        self.find_element(self.text1).click()
    def click_add(self):
        self.find_element(self.text2).click()
    def send_input(self,content):
        self.find_element(self.text3).send_keys(content)
    def click_save(self):
        self.find_element(self.text4).click()
    def success_text(self):
        return self.find_element(self.text5).text
    def fail_text(self):
        return self.find_element(self.text6).text
def test_add(driver,content):
    db = AddPage(driver)
    time.sleep(2)
    db.click_brand()
    time.sleep(2)
    db.click_add()
    time.sleep(2)
    db.send_input(content)
    time.sleep(2)
    db.click_save()
    time.sleep(2)
    try:
        result = db.success_text()
    except:
        result = db.fail_text()
    return result