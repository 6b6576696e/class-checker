from checker import Check
from bot import Bot, NoSuchElementException
import time


USER = ""
PASS = ""


def get_courses(file: str):
    """
    Fetches the courses from the text file and returns an organized dictionary of the courses and their labs/discussions.
    """
    courses = dict()
    with open(file, 'r') as f:
        info = f.read().splitlines()
        for course in info:
            codes = course.split()
            courses[codes[0]] = codes[1:]
    return courses


def print_courses(courses: dict):
    """
    Prints the courses and the labs/discussions that are open.
    """
    for lec, disc in courses.items():
        print(f'{lec} and {disc} are open.')


def run():
    """
    The driver that runs all the functions together.
    """
    class_dict = get_courses("courses.txt")
    print('Grabbed codes.')

    checker = Check(class_dict)

    while class_dict:
        open_courses = checker.check_courses()
        print_courses(open_courses)

        if not open_courses:
            time.sleep(5)
            continue

        class_bot = Bot(USER, PASS)
        while True:
            if not class_bot.get_login_page():
                if not class_bot.get_enroll_page():
                    time.sleep(5)
                    print("Retrying login...")
                    continue

            try:
                for lec in open_courses:
                    if class_bot.enroll(lec):
                        for disc in open_courses[lec]:
                            if class_bot.enroll(disc):
                                break
                        del class_dict[lec]
            except NoSuchElementException:
                print("Something went wrong when registering for classes.")
                continue

            class_bot.logout()
            break


if __name__ == "__main__":
    run()
