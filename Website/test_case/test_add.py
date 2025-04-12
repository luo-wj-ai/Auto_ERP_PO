import unittest
import ddt
from GZ2023test.testguosai.ERP_PO.Website.test_case.model.function import read_data_csv, take_screenshot
from GZ2023test.testguosai.ERP_PO.Website.test_case.model.myunit import Myunit
from GZ2023test.testguosai.ERP_PO.Website.test_case.page_object.AddPage import test_add
from GZ2023test.testguosai.ERP_PO.Website.test_case.page_object.LogingPage import test_denglu
@ddt.ddt
class Test_case(Myunit):
    @ddt.data(read_data_csv()[0])
    def test_01(self,data):
        test_denglu(self.driver,data[0],data[1])
        result = test_add(self.driver,data[2])
        take_screenshot(self.driver)
        try:
            self.assertIn(result,data[3])
        except:
            print(result)

    @ddt.data(read_data_csv()[1])
    def test_02(self, data):
        test_denglu(self.driver, data[0], data[1])
        result = test_add(self.driver, data[2])
        take_screenshot(self.driver)
        try:
            self.assertIn(result, data[3])
        except:
            print(result)

    @ddt.data(read_data_csv()[2])
    def test_03(self, data):
        test_denglu(self.driver, data[0], data[1])
        result = test_add(self.driver, data[2])
        take_screenshot(self.driver)
        try:
            self.assertIn(result, data[3])
        except:
            print(result)

    @ddt.data(read_data_csv()[3])
    def test_04(self, data):
        test_denglu(self.driver, data[0], data[1])
        result = test_add(self.driver, data[2])
        take_screenshot(self.driver)
        try:
            self.assertIn(result, data[3])
        except:
            print(result)

    @ddt.data(read_data_csv()[4])
    def test_05(self, data):
        test_denglu(self.driver, data[0], data[1])
        result = test_add(self.driver, data[2])
        take_screenshot(self.driver)
        try:
            self.assertIn(result, data[3])
        except:
            print(result)

    @ddt.data(read_data_csv()[5])
    def test_06(self, data):
        test_denglu(self.driver, data[0], data[1])
        result = test_add(self.driver, data[2])
        take_screenshot(self.driver)
        try:
            self.assertIn(result, data[3])
        except:
            print(result)
if __name__ == '__main__':
    unittest.main()