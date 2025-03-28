# Webscraper using Selenium
## Introduction
This project is a simple python webscraper built using selenium inorder to extract the text content of the entirepage. It can manage basic url-handling, check for connectivity errors, and file handling that makes it useful for collecting  text data from websites.
## Features
- URL Validation: Checks to make sure that the url provided is of the correct format
- Headless Chrome Browser: To make sure selenium runs efficiently
- Error Handling: Catches common errors like invalid urls and network problems
- File Management: Scrapes the data and stores it in a file
## Project Files
1. scraper.py\
It has the source code for the web scraper and writing the data to a file. It contains the follow functions:
 - check_url: It makes sure that the url is of valid format
 - connect: It is used to connect to the webpage and scrape all the text data using selenium
 - write_to_file: It writes the extracted data to a file called `scraper_data.txt` and also prompts if the file is to be overwritten
 - main: It takes in the input and calls all the other functions
2. requirements.txt\
It has all the requirements needed to run the project which can be installed using 
>pip install -r requirements.txt
3. test_webscraper.py\
This file contains the code to test the different functions that are coded in the scapper.py file. It correctly test all the functions and make sures it is working properly.
## Design Choices
1. Using Selenium Over Requests
  - Almost all websites are dynamically rendered using javascript. Requests cannot be used to render javascript so we use selenium that can do so.

2. Headless mode
  - The program runs in headless mode so that it is more efficient and fast.
3. Error Handling
  - The program handles:
    - Invalid URLS: It uses regex to check validity of the links provided
    - Network Issues: It alerts the user if he is offline.
    - Website Access Issues: It also catches Selenium WebDriver exceptions
## Conclusion
This project provides a simple and efficient way to scrape text from web pages using Selenium. With proper error handling and file management, it ensures a smooth user experience. Future improvements could make it even more powerful for data extraction tasks.