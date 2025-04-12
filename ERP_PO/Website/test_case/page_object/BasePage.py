class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.url = r'http://192.168.46.5:28945/login?redirect=%2Fsystem%2Fuser'
    def get_url(self):
        self.driver.get(self.url)
    def find_element(self,args):
        return self.driver.find_element(*args)