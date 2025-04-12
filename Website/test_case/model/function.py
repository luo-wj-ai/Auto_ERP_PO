import csv
from datetime import datetime
def read_data_csv():
    with open(r'C:\Users\KobeBryant\PycharmProjects\pythonProject\GZ2023test\testguosai\ERP_PO\Website\test_data\test_csv.csv','r',encoding='utf-8')as file:
        reader = csv.reader(file)
        next(reader,None)
        rows = []
        for row in reader:
            rows.append(row)
        return rows
def take_screenshot(driver):
    filename = datetime.now().strftime("%Y%m%d%H%M%S")
    file = r'C:\Users\KobeBryant\PycharmProjects\pythonProject\GZ2023test\testguosai\ERP_PO\Website\test_report\srceenshot//'+filename+'.png'
    driver.get_screenshot_as_file(file)