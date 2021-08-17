from bs4 import BeautifulSoup
import requests

YEAR_TERM = ""


def check_courses(class_dict) -> dict:
    """
    Checks through the given courses and returns a dictionary of the open courses and their labs/discussions.
    """
    open_courses = dict()

    for lec in class_dict:
        if check_availability(lec):
            open_courses[lec] = []
            for disc in class_dict[lec]:
                if check_availability(disc):
                    open_courses[lec].append(disc)
    return open_courses


def check_availability(class_code: str) -> bool:
    """
    Checks the availability of a class given the class code, returns a bool value.
    """
    headers = {'user-agent': 'Chrome/84.0.4147.105'}
    url = 'https://www.reg.uci.edu/perl/WebSoc'
    params = {'CourseCodes': class_code, 'YearTerm': YEAR_TERM, 'Submit': 'XML'}
    request = requests.get(url, params=params, headers=headers)
    page = BeautifulSoup(request.content, 'lxml')
    if '/' in page.find('sec_enrolled').text:
        enrolled, max_enroll = [i.strip() for i in page.find('sec_enrolled').text.split('/')]
    else:
        max_enroll = page.find('sec_max_enroll').text
        enrolled = page.find('sec_enrolled').text

    status = str(page.find('sec_status').text)

    if int(enrolled) < int(max_enroll) and status == 'OPEN':
        print(f'{class_code} is open.')
        return True
    else:
        print(f'{class_code} is not open.')
        return False
