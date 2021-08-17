from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time


class Bot:
    """
    A class that represents a bot registering courses.
    """
    def __init__(self, user, password):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome("C:\\WebDrivers\\chromedriver.exe", options=options)
        self.user = user
        self.password = password

    def get_login_page(self):
        """
        Creates the login page to logon from.
        """
        url = 'https://www.reg.uci.edu/cgi-bin/webreg-redirect.sh'
        self.driver.get(url)

        while 'Login with your UCInetID' not in self.driver.page_source:
            print('Unsuccessful reaching the login page.')
            self.driver.get(url)
            time.sleep(5)

        print('Successful reaching the login page!')
        return self.login()

    def login(self):
        """
        Logons the login page with the given username and password.
        """
        username_textbox = self.driver.find_element_by_id("ucinetid")
        username_textbox.send_keys(self.user)

        password_textbox = self.driver.find_element_by_id("password")
        password_textbox.send_keys(self.password)

        login_button = self.driver.find_element_by_name("login_button")
        ActionChains(self.driver).click(login_button).perform()

        return self.login_check()

    def login_check(self):
        """
        Checks if we have properly logged in and reached the enrollment menu page.
        """
        if 'Enrollment Menu' in self.driver.page_source:
            print('Login successful.')
            return True
        else:
            print('Login failed.')
            return False

    def get_enroll_page(self):
        """
        Navigates to the enrollment page from the enrollment menu page.
        """
        try:
            self.driver.find_element_by_xpath("//input[@value='Enrollment Menu']").click()
            return True
        except NoSuchElementException:
            print("Unable to reach the enrollment page.")
            return False

    def enroll(self, code: str):
        """
        Attempts to enroll into the course.
        """
        try:
            print(f'Attempting to enroll in {code}.')
            self.driver.find_element_by_xpath("//input[@value='Enrollment Menu']").click()
            time.sleep(0.5)
            self.driver.find_element_by_id('add').click()
            self.driver.find_element_by_name('courseCode').send_keys(code)
            self.driver.find_element_by_xpath("//input[@value='Send Request']").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//input[@value='Show Study List']").click()
            if code in self.driver.page_source:
                print(f'{code} successfully added.')
            else:
                print(f'{code} failed to be added.')
        except NoSuchElementException as e:
            print("Enrollment failed.")
            raise e

    def logout(self):
        """
        Safely logs out to avoid any login session bugs.
        """
        self.driver.find_element_by_xpath("//input[@value='Logout']").click()
        self.driver.close()
