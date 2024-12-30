# Assignment
Elastiq.AI - QA Take-Home Assessment
Description : This project consists an Automation Script of a Website in which we are checking on few functionalities and Automating those functionalities using Python Selenium.
I have written some very easy to understand Script in Python

#Prerequisite
-python updated version
-Pycharm or any IDE for code
-Selenium Webdriver
-Easily can run on any driver(Chrome,Firefox,Edge)

Summary of Code

Firstly with the help of drivers open Webdriver on chrome or any other web browser now with the help of driver open the given website for automation, now as per instruction we want to locate search button
and we have to search for "New York" City , so we are searching for it using find_elements and XPATH. Now we have to check the result table showing 5 entries out of 24 , so for this validation 
I am putting a check statement as per given table one row is for the table header so in total 6 rows are there, if there count matches 6 than showing correct result else not correct. 
