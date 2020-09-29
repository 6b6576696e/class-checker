from checker import Check
from time import sleep
from random import randint


def get_courses(file):
    courses = dict()
    with open(file, 'r') as f:
        info = f.read().splitlines()
        for course in info:
            codes = course.split()
            courses[codes[0]] = codes[1:]
    return courses


def run():
    class_dict = get_courses("courses.txt")
    print("Grabbed codes.")
    checker = Check(class_dict)
    while True:
        print("Checking courses...")
        checker.check_all_courses()
        sleep(randint(25, 30))


run()
