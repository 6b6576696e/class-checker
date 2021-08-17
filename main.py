from checker import *
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

    # Continuously checks whether or not every course has been registered for.
    while class_dict:
        open_courses = check_courses(class_dict)
        print_courses(open_courses)

        # If there aren't any course openings, pause before checking again.
        if not open_courses:
            time.sleep(5)
            continue

        # There are course openings, register for the course.
        class_bot = Bot(USER, PASS)
        while True:
            if not class_bot.get_login_page():
                if not class_bot.get_enroll_page():
                    time.sleep(5)
                    print("Retrying login...")
                    continue

            # The website could crash during heavy traffic.
            try:
                for lec in open_courses:
                    if class_bot.enroll(lec):
                        for disc in open_courses[lec]:
                            if class_bot.enroll(disc):
                                # There can be at most a single enrolled discussion for a single lecture.
                                break
                        del class_dict[lec]
            except NoSuchElementException:
                print("Something went wrong when registering for classes.")
                continue

            class_bot.logout()
            break


if __name__ == "__main__":
    run()
