# uci-class-checker
A bot that registers for classes at UCI. The program will parse WebSoc using BS4 to determine whether a course is open. The bot will attempt to register for the course through WebReg using Selenium. 

This bot was built and structured after UCI's registrar website in 2020. As it is dependent on parsing the HTML, any changes to UCI's website will affect the usability of this program.

The intention of this project was to practice making HTTP requests and using external libraries.

## Usage

The following explanation will demonstrate ONLY the program's ability to check for course availability.

`courses.txt` will contain the desired course code(s) in the following format. Each line will represent a different course followed by co-courses.
```
[Lecture] [Discussion] [Discussion]
35470 35471 35472 35473
26860 26861
26845
```

Example output after running for 30 seconds.

![Screenshot](images/example.png)

## Disclaimer
Educational purposes only. Bots violate OAISC standards. I am not responsible for misuse of this program.
