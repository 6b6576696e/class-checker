# uci-class-checker
A bot that registers for classes at UCI. The bot parses WebSoc using BS4 to determine whether a class is open. Attempts will be made to register for the course through WebReg using Selenium. 

This bot was built in 2020. As it is dependent on parsing HTML, any changes to UCI's website will affect the usability of this program.

The intention of this project was to practice making HTTP requests and using external libraries.

## Usage

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
