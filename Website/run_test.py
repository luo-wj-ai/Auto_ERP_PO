import unittest
from HTMLTestRunner import HTMLTestRunner
test_dir = r'C:\Users\KobeBryant\PycharmProjects\pythonProject\GZ2023test\testguosai\ERP_PO\Website\test_case'
discover = unittest.defaultTestLoader.discover(test_dir,'test_*.py')
if __name__ == "__main__":
    with open('D://testguosai.html','wb')as file:
        runner = HTMLTestRunner(stream=file,title='Test Report',description='erp test')
        runner.run(discover)