from bs4 import BeautifulSoup
import requests


class Check:
    def __init__(self, class_dict):
        self.headers = {'user-agent': 'Chrome/84.0.4147.105'}
        self.url = 'https://www.reg.uci.edu/perl/WebSoc'
        self.class_dict = class_dict

    def check_all_courses(self):
        open_courses = dict()
        for lec in self.class_dict:
            if self.check_course(lec):
                open_courses[lec] = []
                for disc in self.class_dict[lec]:
                    if self.check_course(disc):
                        open_courses[lec].append(disc)
        return open_courses

    def check_course(self, course_code):
        page = self.search_course_page(course_code)
        availability = self.check_course_page(course_code, page)
        return availability

    def search_course_page(self, course_code):
        params = {'CourseCodes': course_code, 'YearTerm': '2020-92', 'Submit': 'XML'}
        request = requests.get(self.url, params=params, headers=self.headers)
        page = BeautifulSoup(request.content, 'lxml')
        return page

    def check_course_page(self, course_code, page):
        if '/' in page.find('sec_enrolled').text:
            enrolled, max_enroll = [i.strip() for i in page.find('sec_enrolled').text.split('/')]
        else:
            max_enroll = page.find('sec_max_enroll').text
            enrolled = page.find('sec_enrolled').text

        status = str(page.find('sec_status').text)
        if int(enrolled) < int(max_enroll) and status == 'OPEN':
            print(f'{course_code} is open.')
            return True
        else:
            print(f'{course_code} is not open.')
            return False
