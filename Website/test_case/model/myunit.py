import unittest
from GZ2023test.testguosai.ERP_PO.driver.driver import get_driver
class Myunit(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()